---
title: "From Qubits to Shor's Algorithm"
description: "Learn the fundamentals of quantum computing — qubits, gates, teleportation, QFT, QPE, and Shor's algorithm — with textbook-style notes and Qiskit notebooks."
keywords: "quantum computing, quantum algorithm, Shor's algorithm, Qiskit, quantum Fourier transform, QFT, quantum phase estimation, QPE, quantum teleportation, qubit, entanglement, Bell state, quantum gate, Hadamard, CNOT, Pauli, factoring, period finding, tutorial, documentation, open source, GitHub, Q-COM"
permalink: /
---

# From Qubits to Shor's Algorithm

![Alice and Bob](images/alice-bob-top.png)

A project to learn the fundamentals of quantum computing from both sides — theoretical notes and Qiskit implementations.

<!-- SEO intro added by setup-github-pages; review and adjust -->

If you have ever wanted to **build your own understanding of quantum computing** from the ground up — work through **qubits**, **quantum gates**, and **entanglement** step by step, see how the **quantum Fourier transform** and **quantum phase estimation** lead into **Shor's algorithm**, and verify every idea with runnable **Qiskit** code — this bilingual project is for you. Topics covered include **quantum teleportation**, **Bell states**, **Hadamard** and **CNOT** gates, the **QFT**, **QPE**, and **integer factoring** via period finding.

<!-- /SEO intro -->

日本語版: [README-jp.md](README-jp.md)

## Structure

### `docs/en/` — Theoretical Notes

Textbook-style descriptions of the physics and mathematics of quantum computing.

| File | Content |
|---|---|
| [01_qubit.md](docs/en/01_qubit.md) | Qubit |
| [02_quantum_gates.md](docs/en/02_quantum_gates.md) | Quantum Gates |
| [03_quantum_teleportation.md](docs/en/03_quantum_teleportation.md) | Quantum Teleportation |
| [04_discrete_fourier_transform.md](docs/en/04_discrete_fourier_transform.md) | Discrete Fourier Transform |
| [05_quantum_phase_estimation.md](docs/en/05_quantum_phase_estimation.md) | Quantum Phase Estimation (QPE) |
| [06_shor_algorithm.md](docs/en/06_shor_algorithm.md) | Shor's Algorithm |

### `notebooks/en/` — Qiskit Implementations

Jupyter notebooks that implement and verify the content of the theoretical notes in Qiskit. Also explains the Qiskit API and Python syntax.

| File | Content |
|---|---|
| [00_environment.md](notebooks/en/00_environment.md) | Environment setup |
| [01_qubit_ordering.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/01_qubit_ordering.ipynb) | Qubit ordering (differences between textbook and Qiskit conventions) |
| [02_qiskit_basics.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/02_qiskit_basics.ipynb) | Basic Qiskit operations (gates, measurement, control, inverse, etc.) |
| [03_quantum_teleportation.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/03_quantum_teleportation.ipynb) | Implementation and verification of quantum teleportation |
| [04_quantum_fourier_transform.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/04_quantum_fourier_transform.ipynb) | Quantum Fourier Transform (QFT) |
| [05_quantum_phase_estimation.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/05_quantum_phase_estimation.ipynb) | Quantum Phase Estimation (QPE) |
| [06_shor_algorithm.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/06_shor_algorithm.ipynb) | Shor's Algorithm |

## Bit Ordering Convention

The bit ordering differs between `docs/` and `notebooks/`.

- **`docs/` (textbook):** Big-endian, 1-indexed — $\vert q_1 q_2 q_3\rangle$
- **`notebooks/` (Qiskit):** Little-endian, 0-indexed — $\vert q_2 q_1 q_0\rangle$

See [notebooks/en/01_qubit_ordering.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/en/01_qubit_ordering.ipynb) for details.

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
