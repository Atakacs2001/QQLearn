import numpy as np
from scipy.linalg import sqrtm


def to_density_matrix(state):
    state = np.asarray(state)
    if state.ndim == 1:
        if len(state) != 4:
            raise ValueError("The state vector must have 4 elements (2 qubits).")
        state = state / np.linalg.norm(state)
        rho = np.outer(state, state.conj())
    elif state.ndim == 2:
        if state.shape != (4, 4):
            raise ValueError("Density matrix must be 4x4.")
        rho = state
    else:
        raise ValueError("Input must be a 1D vector or a 2D matrix.")
    return rho


def is_valid_density_matrix(rho, tol=1e-8):
    if not np.allclose(rho, rho.conj().T, atol=tol):
        return False
    if not np.all(np.linalg.eigvalsh(rho) >= -tol):
        return False
    if not np.isclose(np.trace(rho), 1.0, atol=tol):
        return False
    return True


def is_pure_state(rho, tol=1e-8):
    purity = np.real(np.trace(rho @ rho))
    return np.isclose(purity, 1.0, atol=tol), float(purity)


def partial_trace(rho, traced_out='second'):
    rho = np.asarray(rho).reshape(2, 2, 2, 2)
    if traced_out == 'first':
        return np.einsum('ijik->jk', rho)
    elif traced_out == 'second':
        return np.einsum('ikjk->ij', rho)
    else:
        raise ValueError("traced_out must be 'first' or 'second'")


def partial_transpose(rho, subsystem='second'):
    rho = np.asarray(rho).reshape(2, 2, 2, 2)
    if subsystem == 'first':
        pt = rho.transpose(2, 1, 0, 3)
    elif subsystem == 'second':
        pt = rho.transpose(0, 3, 2, 1)
    else:
        raise ValueError("subsystem must be 'first' or 'second'")
    return pt.reshape(4, 4)


def is_entangled_pure_state(rho, tol=1e-8):
    reduced = partial_trace(rho, traced_out='second')
    reduced_purity = np.real(np.trace(reduced @ reduced))
    return not np.isclose(reduced_purity, 1.0, atol=tol)


def is_entangled_mixed_state(rho, tol=1e-8):
    pt = partial_transpose(rho, subsystem='second')
    eigenvalues = np.linalg.eigvalsh(pt)
    return bool(np.any(eigenvalues < -tol))


def von_neumann_entropy(rho, base=2, tol=1e-12):
    eigenvalues = np.linalg.eigvalsh(rho)
    eigenvalues = eigenvalues[eigenvalues > tol]
    if base == 2:
        return float(-np.sum(eigenvalues * np.log2(eigenvalues)))
    return float(-np.sum(eigenvalues * np.log(eigenvalues)))


def fidelity(rho1, rho2):
    sqrt_rho1 = sqrtm(rho1)
    product = sqrt_rho1 @ rho2 @ sqrt_rho1
    return float(np.real(np.trace(sqrtm(product))) ** 2)


def apply_gate(gate_matrix, state, qubit=None):
    """
    Apply a unitary gate to a 2-qubit state vector or density matrix.
    qubit=0 or qubit=1 for single-qubit gates; qubit=None for 2-qubit gates.
    """
    state = np.asarray(state, dtype=complex)
    gate = np.asarray(gate_matrix, dtype=complex)

    if gate.shape == (4, 4) or qubit is None:
        full_gate = gate
    elif qubit == 0:
        full_gate = np.kron(gate, np.eye(2, dtype=complex))
    elif qubit == 1:
        full_gate = np.kron(np.eye(2, dtype=complex), gate)
    else:
        raise ValueError("qubit must be 0, 1, or None")

    if state.ndim == 1:
        return full_gate @ state
    elif state.ndim == 2:
        return full_gate @ state @ full_gate.conj().T
    else:
        raise ValueError("State must be a 1D vector or 2D density matrix.")


def tensor_product(a, b):
    return np.kron(np.asarray(a), np.asarray(b))


def reduced_density_matrix(rho, keep='first'):
    traced_out = 'second' if keep == 'first' else 'first'
    return partial_trace(rho, traced_out=traced_out)


def T_gate(phi):
    return np.array(
        [[np.exp(-1j * phi / 2), 0],
         [0,                     np.exp(1j * phi / 2)]],
        dtype=complex,
    )


GATES = {
    "I":    np.eye(2, dtype=complex),
    "X":    np.array([[0, 1], [1, 0]], dtype=complex),
    "Y":    np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z":    np.array([[1, 0], [0, -1]], dtype=complex),
    "H":    np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2),
    "CNOT": np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]], dtype=complex),
}
