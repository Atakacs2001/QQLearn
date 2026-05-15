
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import math
import cmath
import os
import sys
from PIL.Image import Resampling

from quantum_core import (
    to_density_matrix,
    is_valid_density_matrix,
    is_pure_state,
    is_entangled_pure_state,
    is_entangled_mixed_state,
)

# --- Helper function to handle file paths---
def resource_path(relative_path):
    try:
        # PyInstaller sets this attribute when running a bundled app
        base_path = sys._MEIPASS
    except Exception:
        # Fallback to the current directory during development
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def parse_expression(expr):
    """Evaluate a mathematical expression safely, allowing complex numbers."""
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    allowed_names.update({k: getattr(cmath, k) for k in dir(cmath) if not k.startswith("__")})
    allowed_names.update({"pi": math.pi, "e": math.e, "i": 1j, "j": 1j})
    try:
        return eval(expr.strip(), {"__builtins__": None}, allowed_names)
    except Exception as e:
        raise ValueError(f"Invalid expression: {expr}\n{e}")

# --- Splash screen logic and GUI initialization ---

def show_splash_and_start(main_root):
    """Display a splash screen animation before launching the main app window."""
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("500x400+450+250")
    splash.configure(bg="white")

    original_img = Image.open(logo_path).resize((350, 350))
    logo_label = tk.Label(splash, bg="white")
    logo_label.pack(expand=True)

    # Build animation sequence: spin and pulse
    sequence = []
    for i in range(60):
        sequence.append((i * 5, int(100 * math.exp(-i / 15))))
    for i in range(1, 21):
        sequence.append((300 + i * 5, 10 + i * 2))
    for i in range(1, 9):
        sequence.append((400 - i * 5, 20 + i * 5))

    def run_animation(index=0):
        if index >= len(sequence):
            run_pulse()
            return
        angle, delay = sequence[index]
        rotated = original_img.rotate(angle, resample=Resampling.BICUBIC)
        photo = ImageTk.PhotoImage(rotated)
        logo_label.config(image=photo)
        logo_label.image = photo
        splash.after(delay, lambda: run_animation(index + 1))

    def run_pulse():
        sizes = [360, 390, 430, 390, 360, 340]
        delays = [30] * len(sizes)

        def pulse_step(i=0):
            if i >= len(sizes):
                splash.after(1000, finish)
                return
            img = original_img.resize((sizes[i], sizes[i]), resample=Resampling.BICUBIC)
            photo = ImageTk.PhotoImage(img)
            logo_label.config(image=photo)
            logo_label.image = photo
            splash.after(delays[i], lambda: pulse_step(i + 1))

        pulse_step()

    def finish():
        splash.destroy()
        create_main_window(main_root)

    run_animation()

# --- Main application window ---

def create_main_window(root):
    """Build the main GUI layout and functionality."""
    root.deiconify()
    root.title("QQ Entanglement Tester")
    root.geometry("900x800")
    root.configure(bg="white")

    # Top banner with title and images
    top_frame = tk.Frame(root, bg="white")
    top_frame.pack(pady=10)

    img1 = ImageTk.PhotoImage(Image.open(img1_path).resize((120, 120)))
    img2 = ImageTk.PhotoImage(Image.open(img2_path).resize((120, 120)))
    img3 = ImageTk.PhotoImage(Image.open(img3_path).resize((120, 120)))

    root.img1 = img1
    root.img2 = img2
    root.img3 = img3

    tk.Label(top_frame, image=img1, bg="white").pack(side="left", padx=10)
    tk.Label(top_frame, text="QQ összefonódás tester", font=("Arial", 20, "bold"), bg="white").pack(side="left", padx=10)
    tk.Label(top_frame, image=img2, bg="white").pack(side="left", padx=10)
    tk.Label(top_frame, image=img3, bg="white").pack(side="left", padx=10)

    # User input type selection
    select_frame = tk.Frame(root, bg="white")
    select_frame.pack(pady=10)
    tk.Label(select_frame, text="Bemenet típusa:", font=("Arial", 12), bg="white").pack()

    input_type_slider = tk.Scale(
        select_frame, from_=0, to=1, orient="horizontal",
        showvalue=0, length=200, resolution=1, bg="white",
        troughcolor="#ddd", highlightthickness=0, sliderlength=30,
        command=lambda val: animate_transition(int(val))
    )
    input_type_slider.pack()

    slider_labels = tk.Frame(select_frame, bg="white")
    slider_labels.pack()
    tk.Label(slider_labels, text="Állapotvektor", bg="white").pack(side="left", padx=50)
    tk.Label(slider_labels, text="Sűrűségmátrix", bg="white").pack(side="right", padx=50)

    # Info label to guide the user 
    info_frame = tk.Frame(root, bg="white")
    info_frame.pack(pady=5)
    info_label = tk.Label(info_frame, text="", font=("Arial", 12), bg="white")
    info_label.pack()

    # Input for state vector
    vector_frame = tk.Frame(root, bg="white")
    vector_entries = [tk.Entry(vector_frame, width=10) for _ in range(4)]
    basis_labels = ["|00⟩ +", "|01⟩ +", "|10⟩ +", "|11⟩"]
    tk.Label(vector_frame, text="Ψ =", font=("Arial", 12, "bold"), bg="white").pack(side="left")
    for i in range(4):
        vector_entries[i].pack(side="left", padx=2)
        tk.Label(vector_frame, text=basis_labels[i], bg="white").pack(side="left")

    # Input for density matrix
    matrix_container = tk.Frame(root, bg="white")
    matrix_label = tk.Label(matrix_container, text="ρ =", font=("Arial", 12, "bold"), bg="white")
    matrix_label.pack()
    matrix_frame = tk.Frame(matrix_container, bg="white")
    matrix_frame.pack()
    matrix_entries = [[tk.Entry(matrix_frame, width=10) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            matrix_entries[i][j].grid(row=i, column=j, padx=2, pady=2)

    # Result and warning labels
    result_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
    result_label.pack(pady=15)

    info_warning_label = tk.Label(root, text="", font=("Arial", 10, "italic"), fg="orange", bg="white")
    info_warning_label.pack()

    def animate_transition(target_type):
        """Switch between input modes (vector or matrix)."""
        steps = 5
        delay = 30
        if target_type == 0:
            def step(i=0):
                if i == 0:
                    matrix_container.pack_forget()
                    vector_frame.pack(pady=10)
                    info_label.config(text="Add meg az állapotvektor együtthatóit:")
                if i < steps:
                    vector_frame.update()
                    root.after(delay, lambda: step(i + 1))
            step()
        else:
            def step(i=0):
                if i == 0:
                    vector_frame.pack_forget()
                    matrix_container.pack(pady=10)
                    info_label.config(text="Add meg a sűrűségmátrix elemeit:")
                if i < steps:
                    matrix_container.update()
                    root.after(delay, lambda: step(i + 1))
            step()

    def ellenorzes():
        """Main logic to parse user input and check purity/entanglement."""
        try:
            matrix_text = ""
            info_warning_label.config(text="")
            if input_type_slider.get() == 0:
                coeffs = [parse_expression(e.get()) for e in vector_entries]
                state = np.array(coeffs, dtype=np.complex128)
                norm = np.linalg.norm(state)
                if not np.isclose(norm, 1.0):
                    info_warning_label.config(text="⚠ A vektort automatikusan normalizáltuk.")
                    state = state / norm
            else:
                values = [parse_expression(matrix_entries[i][j].get()) for i in range(4) for j in range(4)]
                state = np.array(values, dtype=np.complex128).reshape((4, 4))
            rho = to_density_matrix(state)
            if not is_valid_density_matrix(rho):
                raise ValueError("Érvénytelen sűrűségmátrix.")
            is_pure, purity = is_pure_state(rho)
            entangled = is_entangled_pure_state(rho) if is_pure else is_entangled_mixed_state(rho)
            result = f"∏: {purity:.4f} — {'Tiszta' if is_pure else 'Kevert'} állapot\n"
            result += f"{'Összefonódott' if entangled else 'Nem összefonódott'}"
            if input_type_slider.get() == 0:
                matrix_lines = [
                    "[" + ", ".join(f"{elem.real:.2f}{'+' if elem.imag >= 0 else '-'}{abs(elem.imag):.2f}i" for elem in row) + "]"
                    for row in rho
                ]
                matrix_text = "\nρ =\n" + "\n".join(matrix_lines)
            result_label.config(text=result + matrix_text, fg="green" if entangled else "blue")
        except Exception as e:
            info_warning_label.config(text=f"Hiba: {e}", fg="red")

    tk.Button(root, text="Ellenőrzés", command=ellenorzes).pack(pady=10)
    animate_transition(0)

# --- Image path ---
logo_path = resource_path("logo_qubit.PNG")
img1_path = resource_path("tokmacsek_removed.PNG")
img2_path = resource_path("menomacsek-removed.png")
img3_path = resource_path("dobozmacsek-removebg-preview.png")

# --- App launch point ---
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_splash_and_start(root)
    root.mainloop()
