import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest

from examples import EXAMPLES, partially_entangled, werner_state, get_example_data
from quantum_core import (
    to_density_matrix,
    is_valid_density_matrix,
    is_pure_state,
    is_entangled_pure_state,
    is_entangled_mixed_state,
)


# ── Segédfüggvény ────────────────────────────────────────────────────────────

def load_rho(name: str) -> np.ndarray:
    ex = EXAMPLES[name]
    return to_density_matrix(ex["data"])


# ── Érvényesség: minden statikus példa valid sűrűségmátrix ───────────────────

@pytest.mark.parametrize("name", list(EXAMPLES.keys()))
def test_all_examples_are_valid_density_matrices(name):
    rho = load_rho(name)
    assert is_valid_density_matrix(rho), f"Érvénytelen sűrűségmátrix: {name}"


# ── Tisztaság ────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("name", ["|00⟩", "|01⟩",
                                   "Szeparábilis szuperpozíció |+⟩⊗|+⟩",
                                   "Bell Φ+", "Bell Φ-",
                                   "Bell Ψ+", "Bell Ψ- (szinglet)"])
def test_vector_examples_are_pure(name):
    rho = load_rho(name)
    is_pure, _ = is_pure_state(rho)
    assert is_pure, f"Tiszta állapotnak kellene lennie: {name}"


def test_maximally_mixed_is_not_pure():
    rho = load_rho("Teljesen kevert (I/4)")
    is_pure, purity = is_pure_state(rho)
    assert not is_pure
    assert np.isclose(purity, 0.25)


# ── Összefonódás: szeparábilis állapotok ─────────────────────────────────────

@pytest.mark.parametrize("name", ["|00⟩", "|01⟩",
                                   "Szeparábilis szuperpozíció |+⟩⊗|+⟩"])
def test_product_states_not_entangled(name):
    rho = load_rho(name)
    assert not is_entangled_pure_state(rho), f"Nem kellene összefonódottnak lennie: {name}"


def test_maximally_mixed_not_entangled():
    rho = load_rho("Teljesen kevert (I/4)")
    assert not is_entangled_mixed_state(rho)


# ── Összefonódás: Bell-állapotok ─────────────────────────────────────────────

@pytest.mark.parametrize("name", ["Bell Φ+", "Bell Φ-", "Bell Ψ+", "Bell Ψ- (szinglet)"])
def test_bell_states_are_entangled(name):
    rho = load_rho(name)
    assert is_entangled_pure_state(rho), f"Bell-állapotnak összefonódottnak kellene lennie: {name}"


# ── Részlegesen összefonódott állapot ────────────────────────────────────────

def test_partially_entangled_at_pi_over_4_is_entangled():
    vec = partially_entangled(math.pi / 4)
    rho = to_density_matrix(vec)
    assert is_valid_density_matrix(rho)
    assert is_entangled_pure_state(rho)


def test_partially_entangled_at_zero_is_not_entangled():
    # theta=0 → |00⟩, szorzatállapot
    vec = partially_entangled(0.0)
    rho = to_density_matrix(vec)
    assert not is_entangled_pure_state(rho)


def test_partially_entangled_at_pi_over_2_is_not_entangled():
    # theta=π/2 → |11⟩, szorzatállapot
    vec = partially_entangled(math.pi / 2)
    rho = to_density_matrix(vec)
    assert not is_entangled_pure_state(rho)


# ── Werner-szerű állapot ──────────────────────────────────────────────────────

def test_werner_entangled_above_threshold():
    # p = 0.5 > 1/3 → összefonódott
    rho = werner_state(0.5)
    assert is_valid_density_matrix(rho)
    assert is_entangled_mixed_state(rho)


def test_werner_separable_below_threshold():
    # p = 0.2 < 1/3 → szeparábilis
    rho = werner_state(0.2)
    assert is_valid_density_matrix(rho)
    assert not is_entangled_mixed_state(rho)


def test_werner_at_zero_equals_maximally_mixed():
    rho = werner_state(0.0)
    assert np.allclose(rho, np.eye(4) / 4)


def test_werner_at_one_equals_bell_phi_plus():
    rho_werner = werner_state(1.0)
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_bell = to_density_matrix(bell)
    assert np.allclose(rho_werner, rho_bell, atol=1e-10)


def test_werner_invalid_p_raises():
    with pytest.raises(ValueError):
        werner_state(1.5)


# ── get_example_data ─────────────────────────────────────────────────────────

def test_get_example_data_returns_correct_entry():
    entry = get_example_data("Bell Φ+")
    assert entry["type"] == "vector"
    assert len(entry["data"]) == 4


def test_get_example_data_raises_on_unknown_name():
    with pytest.raises(KeyError):
        get_example_data("Nem létező példa")
