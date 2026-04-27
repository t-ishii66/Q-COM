# From Qubits to Shor's Algorithm

![Alice and Bob](images/alice-bob-top.png)

A project to learn the fundamentals of quantum computing from both sides — theoretical notes and Qiskit implementations.

日本語版: [README-jp.md](README-jp.md)

## Structure

### `notes/en/` — Theoretical Notes

Textbook-style descriptions of the physics and mathematics of quantum computing.

| File | Content |
|---|---|
| [01_qubit.md](notes/en/01_qubit.md) | Qubit |
| [02_quantum_gates.md](notes/en/02_quantum_gates.md) | Quantum Gates |
| [03_quantum_teleportation.md](notes/en/03_quantum_teleportation.md) | Quantum Teleportation |
| [04_discrete_fourier_transform.md](notes/en/04_discrete_fourier_transform.md) | Discrete Fourier Transform |
| [05_quantum_phase_estimation.md](notes/en/05_quantum_phase_estimation.md) | Quantum Phase Estimation (QPE) |
| [06_shor_algorithm.md](notes/en/06_shor_algorithm.md) | Shor's Algorithm |

### `notebooks/en/` — Qiskit Implementations

Jupyter notebooks that implement and verify the content of the theoretical notes in Qiskit. Also explains the Qiskit API and Python syntax.

| File | Content |
|---|---|
| [00_environment.md](notebooks/en/00_environment.md) | Environment setup |
| [01_qubit_ordering.ipynb](notebooks/en/01_qubit_ordering.ipynb) | Qubit ordering (differences between textbook and Qiskit conventions) |
| [02_qiskit_basics.ipynb](notebooks/en/02_qiskit_basics.ipynb) | Basic Qiskit operations (gates, measurement, control, inverse, etc.) |
| [03_quantum_teleportation.ipynb](notebooks/en/03_quantum_teleportation.ipynb) | Implementation and verification of quantum teleportation |
| [04_quantum_fourier_transform.ipynb](notebooks/en/04_quantum_fourier_transform.ipynb) | Quantum Fourier Transform (QFT) |
| [05_quantum_phase_estimation.ipynb](notebooks/en/05_quantum_phase_estimation.ipynb) | Quantum Phase Estimation (QPE) |
| [06_shor_algorithm.ipynb](notebooks/en/06_shor_algorithm.ipynb) | Shor's Algorithm |

## Bit Ordering Convention

The bit ordering differs between `notes/` and `notebooks/`.

- **`notes/` (textbook):** Big-endian, 1-indexed — $\vert q_1 q_2 q_3\rangle$
- **`notebooks/` (Qiskit):** Little-endian, 0-indexed — $\vert q_2 q_1 q_0\rangle$

See [notebooks/en/01_qubit_ordering.ipynb](notebooks/en/01_qubit_ordering.ipynb) for details.

## Environment Setup

See [notebooks/en/00_environment.md](notebooks/en/00_environment.md).

# Credits

- Planning: t-ishii66 (Studying physics in university. Systems engineer. Working hard on English conversation.)
- Production: Claude Opus 4.6, t-ishii66
- Notes review: t-ishii66
- Notebooks review: t-ishii66
- Publication date: 2026/4/28
- Version: 1.0.0
- Copyright(C) 2026 t-ishii66. All rights reserved.
