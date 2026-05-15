import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pytest

from quantum_core import (
    to_density_matrix,
    is_valid_density_matrix,
    is_pure_state,
    is_entangled_pure_state,
    is_entangled_mixed_state,
)


def test_bell_phi_plus_is_entangled():
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho = to_density_matrix(bell)
    is_pure, _ = is_pure_state(rho)
    assert is_pure
    assert is_entangled_pure_state(rho)


def test_ket00_not_entangled():
    ket00 = np.array([1, 0, 0, 0], dtype=complex)
    rho = to_density_matrix(ket00)
    is_pure, _ = is_pure_state(rho)
    assert is_pure
    assert not is_entangled_pure_state(rho)


def test_maximally_mixed_is_valid():
    rho = np.eye(4, dtype=complex) / 4
    assert is_valid_density_matrix(rho)
    is_pure, purity = is_pure_state(rho)
    assert not is_pure
    assert np.isclose(purity, 0.25)


def test_trace_equals_one():
    bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho = to_density_matrix(bell)
    assert np.isclose(np.trace(rho).real, 1.0)
