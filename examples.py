import numpy as np
import math

# ── Statikus példák ────────────────────────────────────────────────────────
#
# Minden bejegyzés:
#   type        : "vector" | "matrix"
#   data        : numpy tömb (állapotvektor vagy 4x4 sűrűségmátrix)
#   description : rövid magyar leírás
#
# A példákat a GUI betöltheti és átadhatja a quantum_core függvényeinek.

EXAMPLES = {
    "|00⟩": {
        "type": "vector",
        "data": np.array([1, 0, 0, 0], dtype=complex),
        "description": "Alapállapot: mindkét qubit |0⟩.",
    },
    "|01⟩": {
        "type": "vector",
        "data": np.array([0, 1, 0, 0], dtype=complex),
        "description": "Az első qubit |0⟩, a második |1⟩.",
    },
    "Szeparábilis szuperpozíció |+⟩⊗|+⟩": {
        "type": "vector",
        "data": np.array([1, 1, 1, 1], dtype=complex) / 2.0,
        "description": "(|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2  –  nem összefonódott.",
    },
    "Bell Φ+": {
        "type": "vector",
        "data": np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2),
        "description": "(|00⟩ + |11⟩) / √2  –  maximálisan összefonódott.",
    },
    "Bell Φ-": {
        "type": "vector",
        "data": np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2),
        "description": "(|00⟩ − |11⟩) / √2  –  maximálisan összefonódott.",
    },
    "Bell Ψ+": {
        "type": "vector",
        "data": np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2),
        "description": "(|01⟩ + |10⟩) / √2  –  maximálisan összefonódott.",
    },
    "Bell Ψ- (szinglet)": {
        "type": "vector",
        "data": np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2),
        "description": "(|01⟩ − |10⟩) / √2  –  szinglet, maximálisan összefonódott.",
    },
    "Teljesen kevert (I/4)": {
        "type": "matrix",
        "data": np.eye(4, dtype=complex) / 4.0,
        "description": "Maximálisan kevert állapot, nincs összefonódás.",
    },
}

# ── Paraméteres példák ─────────────────────────────────────────────────────

def partially_entangled(theta: float) -> np.ndarray:
    """
    cos(θ)|00⟩ + sin(θ)|11⟩ állapotvektor.

    θ = 0       → |00⟩, nem összefonódott
    θ = π/4     → (|00⟩ + |11⟩)/√2, maximálisan összefonódott
    θ = π/2     → |11⟩, nem összefonódott
    """
    return np.array(
        [math.cos(theta), 0.0, 0.0, math.sin(theta)],
        dtype=complex,
    )


def werner_state(p: float) -> np.ndarray:
    """
    Werner-szerű állapot: p|Φ+⟩⟨Φ+| + (1−p)I/4.

    PPT-kritérium szerint összefonódott, ha p > 1/3.

    p = 0 → teljesen kevert, I/4
    p = 1 → Bell Φ+ tiszta állapot
    """
    if not 0.0 <= p <= 1.0:
        raise ValueError(f"p értéke [0, 1] között kell legyen, kapott: {p}")
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_bell = np.outer(bell, bell.conj())
    return p * rho_bell + (1.0 - p) * np.eye(4, dtype=complex) / 4.0


# ── Segédfüggvény a GUI-hoz ────────────────────────────────────────────────

def list_example_names() -> list:
    """Visszaadja a statikus példák neveit sorban."""
    return list(EXAMPLES.keys())


def get_example_data(name: str):
    """
    Visszaadja az EXAMPLES[name] szótárt.
    Kivételt dob, ha a név nem létezik.
    """
    if name not in EXAMPLES:
        raise KeyError(f"Ismeretlen példa: '{name}'. Elérhető: {list(EXAMPLES.keys())}")
    return EXAMPLES[name]
