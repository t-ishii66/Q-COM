# 05: Quantum Phase Estimation (QPE)

## Why Learn Phase Estimation?

Quantum Phase Estimation (QPE) is one of the most important subroutines in quantum computing. Shor's factoring algorithm, quantum chemistry simulations, and many other quantum algorithms use QPE internally.

The essence of QPE is "reading the eigenvalue of a unitary operator using a quantum circuit," and it is a direct application of the Quantum Fourier Transform (Note 04).

---

## Problem Setup

### Eigenvalues and Eigenvectors

Suppose we are given a unitary operator $U$ and its eigenvector $\vert u\rangle$:

$$
U\vert u\rangle = e^{2\pi i \varphi}\vert u\rangle
$$

Here $e^{2\pi i \varphi}$ is the eigenvalue, and $\varphi$ is a real number with $0 \le \varphi < 1$.

Since eigenvalues of a unitary operator are always complex numbers with absolute value 1 ($\vert e^{2\pi i \varphi}\vert = 1$), all the information is contained in the phase $\varphi$.

### Goal

**Given $U$ and $\vert u\rangle$, estimate the phase $\varphi$.**

Specifically, we find an $n$-bit approximation $\tilde{\varphi}$ of $\varphi$. $n$-bit precision means $\tilde{\varphi} = 0.j_1 j_2 \cdots j_n$ (binary fraction), and the error is $\lvert\varphi - \tilde{\varphi}\rvert \le 2^{-n}$ with high probability (the success probability can be increased by adding more bits to the counting register).

### Binary Fraction Notation

The binary fraction $0.j_1 j_2 \cdots j_n$ represents the following value:

$$
0.j_1 j_2 \cdots j_n = \frac{j_1}{2} + \frac{j_2}{4} + \cdots + \frac{j_n}{2^n} = \sum_{k=1}^{n} \frac{j_k}{2^k}
$$

where each $j_k \in \{0, 1\}$.

**Example:** $0.101_2 = \frac{1}{2} + \frac{0}{4} + \frac{1}{8} = \frac{5}{8} = 0.625$

---

## QPE Circuit Structure

### Registers

The QPE circuit consists of two registers:

| Register | Number of qubits | Initial state | Role |
|---------|------------|---------|------|
| First register (counting register) | $n$ | $\vert 0\rangle^{\otimes n}$ | Stores the estimated value of phase $\varphi$ |
| Second register (eigenstate register) | $m$ | $\vert u\rangle$ | Eigenvector of $U$ |

$m$ is the number of qubits in the space on which $U$ acts, and depends on the problem.

### Circuit Overview

The QPE circuit consists of four steps:

1. **Hadamard transform**: Apply $H$ to all qubits of the first register
2. **Controlled unitary operations**: Using each bit of the first register as a control bit, apply $U^{2^k}$ to the second register
3. **Inverse Quantum Fourier Transform**: Apply $\text{QFT}^{-1}$ to the first register
4. **Measurement**: Measure the first register in the computational basis

![QPE circuit overview](../../images/05_qpe_general.png)

---

## Controlled Unitary Gate

### Definition

For an $n$-qubit unitary operator $U$, the **controlled-$U$ gate** operates as follows:

$$
CU\vert 0\rangle\vert\psi\rangle = \vert 0\rangle\vert\psi\rangle, \quad CU\vert 1\rangle\vert\psi\rangle = \vert 1\rangle(U\vert\psi\rangle)
$$

If the control bit is $\vert 0\rangle$, nothing happens; if $\vert 1\rangle$, $U$ is applied. CNOT is the special case where $U = X$ (see Note 02).

### Action of Controlled-$U$ on an Eigenvector

When $U\vert u\rangle = e^{2\pi i \varphi}\vert u\rangle$, the action of controlled-$U$ is:

$$
CU\vert 0\rangle\vert u\rangle = \vert 0\rangle\vert u\rangle
$$

$$
CU\vert 1\rangle\vert u\rangle = \vert 1\rangle(U\vert u\rangle) = e^{2\pi i \varphi}\vert 1\rangle\vert u\rangle
$$

Applying this to a general superposition state:

$$
CU\left(\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}\right)\vert u\rangle = \frac{\vert 0\rangle + e^{2\pi i \varphi}\vert 1\rangle}{\sqrt{2}}\vert u\rangle
$$

The eigenvector $\vert u\rangle$ is unchanged, and the phase $e^{2\pi i \varphi}$ is **transferred to the control bit**. This is called **phase kickback**. QPE is built on this phenomenon.

### Derivation of Phase Kickback

We carefully derive the above formula. When the control bit is $\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$:

$$
CU\left(\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}\right)\vert u\rangle = \frac{1}{\sqrt{2}}\Big(CU\vert 0\rangle\vert u\rangle + CU\vert 1\rangle\vert u\rangle\Big)
$$

The first term is $\vert 0\rangle\vert u\rangle$ and the second term is $e^{2\pi i \varphi}\vert 1\rangle\vert u\rangle$, so:

$$
= \frac{1}{\sqrt{2}}\Big(\vert 0\rangle\vert u\rangle + e^{2\pi i \varphi}\vert 1\rangle\vert u\rangle\Big) = \frac{\vert 0\rangle + e^{2\pi i \varphi}\vert 1\rangle}{\sqrt{2}} \otimes \vert u\rangle
$$

$\vert u\rangle$ separates as a factor, and the phase $e^{2\pi i\varphi}$ is applied only to the $\vert 1\rangle$ component of the control bit.

### Repeated Application of $U$

Since $U^{2^k}\vert u\rangle = e^{2\pi i \cdot 2^k \varphi}\vert u\rangle$, for controlled-$U^{2^k}$ similarly:

$$
CU^{2^k}\left(\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}\right)\vert u\rangle = \frac{\vert 0\rangle + e^{2\pi i \cdot 2^k \varphi}\vert 1\rangle}{\sqrt{2}}\vert u\rangle
$$

The phase transferred to the control bit is multiplied by $2^k$.

---

## How QPE Works (Mathematical Derivation)

We perform phase estimation with an $n$-bit counting register. The qubits are $q_1, q_2, \ldots, q_n$ (first register) and $\vert u\rangle$ (second register).

### Step 1: Hadamard Transform

Apply $H$ to all qubits of the first register. The initial state is $\vert 0\rangle^{\otimes n}\vert u\rangle$:

$$
H^{\otimes n}\vert 0\rangle^{\otimes n} = (H\vert 0\rangle) \otimes (H\vert 0\rangle) \otimes \cdots \otimes (H\vert 0\rangle) = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \otimes \cdots \otimes \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}
$$

$$
= \left(\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}\right)^{\otimes n} = \frac{1}{\sqrt{2^n}}\sum_{j=0}^{2^n - 1}\vert j\rangle
$$

State after Step 1:

$$
\vert\Psi_1\rangle = \frac{1}{\sqrt{2^n}}\sum_{j=0}^{2^n - 1}\vert j\rangle \otimes \vert u\rangle
$$

### Step 2: Controlled Unitary Operations

Using $q_k$ ($k = 1, 2, \ldots, n$) of the first register as control bits, apply $U^{2^{n-k}}$ to the second register.

First, consider the case $n = 1$ (counting register is 1 bit):

$$
\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}\vert u\rangle \overset{ CU }{\longrightarrow} \frac{\vert 0\rangle + e^{2\pi i \varphi}\vert 1\rangle}{\sqrt{2}}\vert u\rangle
$$

For $n = 2$, $q_1$ controls $U^2$ and $q_2$ controls $U^1$:

$$
\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \otimes \vert u\rangle
\quad \overset{ CU^2,  CU }{\longrightarrow}  \quad
\frac{\vert 0\rangle + e^{2\pi i \cdot 2\varphi}\vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + e^{2\pi i \varphi}\vert 1\rangle}{\sqrt{2}} \otimes \vert u\rangle
$$

For general $n$ bits:

$$
\vert\Psi_2\rangle = \frac{1}{\sqrt{2^n}}\bigotimes_{k=1}^{n}\Big(\vert 0\rangle + e^{2\pi i \cdot 2^{n-k}\varphi}\vert 1\rangle\Big) \otimes \vert u\rangle
$$

Writing out $k = 1, 2, \ldots, n$:

$$
\vert\Psi_2\rangle = \frac{1}{\sqrt{2^n}}\Big(\vert 0\rangle + e^{2\pi i \cdot 2^{n-1}\varphi}\vert 1\rangle\Big) \otimes \Big(\vert 0\rangle + e^{2\pi i \cdot 2^{n-2}\varphi}\vert 1\rangle\Big) \otimes \cdots \otimes \Big(\vert 0\rangle + e^{2\pi i \cdot 2^0 \varphi}\vert 1\rangle\Big) \otimes \vert u\rangle
$$

$q_1$ receives phase $2^{n-1}\varphi$ (largest) and $q_n$ receives phase $2^0\varphi = \varphi$ (smallest). Higher-order bits receive larger phase kickbacks.

### Expansion of the Tensor Product

We verify that the above expression reduces to the form $e^{2\pi i j\varphi}$.

Expanding each factor $(\vert 0\rangle + e^{2\pi i \cdot 2^{n-k}\varphi}\vert 1\rangle)$ with $j_k \in \{0, 1\}$: the $j_k = 0$ term is $\vert 0\rangle$ (no phase), and the $j_k = 1$ term is $e^{2\pi i \cdot 2^{n-k}\varphi}\vert 1\rangle$. That is, each factor can be written as $\sum_{j_k=0}^{1} e^{2\pi i \cdot j_k \cdot 2^{n-k}\varphi}\vert j_k\rangle$ (when $j_k = 0$, $e^0 = 1$).

Expanding the tensor product of $n$ factors sums over all combinations of $j_1, j_2, \ldots, j_n$:

$$
\frac{1}{\sqrt{2^n}}\sum_{j_1=0}^{1}\sum_{j_2=0}^{1}\cdots\sum_{j_n=0}^{1} e^{2\pi i(j_1 \cdot 2^{n-1} + j_2 \cdot 2^{n-2} + \cdots + j_n \cdot 2^0)\varphi}\vert j_1 j_2 \cdots j_n\rangle \otimes \vert u\rangle
$$

The exponent $j_1 \cdot 2^{n-1} + j_2 \cdot 2^{n-2} + \cdots + j_n \cdot 2^0$ is exactly the decimal value when reading $j_1 j_2 \cdots j_n$ as a binary number. Writing this as $j$:

$$
\vert\Psi_2\rangle = \frac{1}{\sqrt{2^n}}\sum_{j=0}^{2^n - 1} e^{2\pi i j\varphi}\vert j\rangle \otimes \vert u\rangle
$$

Because the phase $2^{n-k}\varphi$ applied to each bit corresponds to the binary digit weight $2^{n-k}$, the tensor product collapses into a single exponent $e^{2\pi i j\varphi}$.

**Verification of the expansion (case $n = 2$):**

Writing the binary representation of $j$ as $j = j_1 \cdot 2 + j_2$ ($j_1, j_2 \in \{0,1\}$):

$$
\frac{1}{2}\sum_{j_1, j_2} e^{2\pi i (j_1 \cdot 2 + j_2)\varphi}\vert j_1 j_2\rangle = \frac{1}{2}\sum_{j_1, j_2} e^{2\pi i \cdot 2j_1 \varphi} e^{2\pi i j_2 \varphi}\vert j_1\rangle\vert j_2\rangle
$$

$$
= \frac{1}{2}\left(\sum_{j_1} e^{2\pi i \cdot 2j_1\varphi}\vert j_1\rangle\right)\left(\sum_{j_2} e^{2\pi i j_2\varphi}\vert j_2\rangle\right) = \frac{\vert 0\rangle + e^{2\pi i \cdot 2\varphi}\vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + e^{2\pi i\varphi}\vert 1\rangle}{\sqrt{2}}
$$

This indeed matches the tensor product form.

### Step 3: Inverse Quantum Fourier Transform

The state of the first register after Step 2 (omitting $\vert u\rangle$) is:

$$
\frac{1}{\sqrt{N}}\sum_{j=0}^{N - 1} e^{2\pi i j\varphi}\vert j\rangle \qquad (N = 2^n)
$$

Recall the forward DFT defined in Note 04. The DFT of an input sequence $x_0, \ldots, x_{N-1}$ is:

$$
X_k = \frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} x_j  \omega_N^{jk}, \qquad \omega_N = e^{2\pi i / N}
$$

In the language of quantum states, for $\vert x\rangle = \sum_j x_j \vert j\rangle$, we have $F_N\vert x\rangle = \sum_k X_k \vert k\rangle$.

Now, if $\varphi = s/N$ ($s$ is an integer, $0 \le s < N$), then $e^{2\pi i j\varphi} = e^{2\pi i js/N}$. Recalling $\omega_N = e^{2\pi i/N}$, we have $e^{2\pi i js/N} = \omega_N^{js}$, so:

$$
\frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} e^{2\pi i j\varphi}\vert j\rangle = \frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} \omega_N^{js}\vert j\rangle
$$

On the other hand, let us directly compute what state $F_N\vert s\rangle$ becomes from the definition of the DFT matrix.

Multiplying matrix $F_N$ by vector $\vert s\rangle$ means computing the $k$-th component of the output as $\sum_j (F_N)_{kj} (\vert s\rangle)_j$. $\vert s\rangle$ is an $N$-dimensional vector, but since $N = 2^n$, it can be represented with $n = \log_2 N$ qubits. For example, if $N = 4$, $\vert s\rangle$ is a 4-dimensional vector, but only 2 qubits are needed in the circuit. Since $\vert s\rangle$ is a computational basis state, only the $s$-th component is 1 and all others are 0:

$$
\vert s\rangle = \begin{pmatrix} 0 \\\\ \vdots \\\\ 0 \\\\ 1 \\\\ 0 \\\\ \vdots \\\\ 0 \end{pmatrix} \leftarrow s\text{-th position}
$$

Therefore, multiplying $F_N$ by this vector extracts only the $s$-th column of $F_N$:

$$
F_N\vert s\rangle = \frac{1}{\sqrt{N}} \begin{pmatrix} 1 & \cdots & 1 & \cdots & 1 \\\\ 1 & \cdots & \omega_N^{s} & \cdots & \omega_N^{N-1} \\\\ \vdots & & \vdots & & \vdots \\\\ 1 & \cdots & \omega_N^{s(N-1)} & \cdots & \omega_N^{(N-1)^2} \end{pmatrix} \begin{pmatrix} 0 \\\\ \vdots \\\\ 1 \\\\ \vdots \\\\ 0 \end{pmatrix} = \frac{1}{\sqrt{N}} \begin{pmatrix} 1 \\\\ \omega_N^{s} \\\\ \omega_N^{2s} \\\\ \vdots \\\\ \omega_N^{(N-1)s} \end{pmatrix}
$$

Rewriting in ket notation:

$$
F_N\vert s\rangle = \sum_{k=0}^{N-1} (F_N)_{ks} \vert k\rangle
$$

Substituting $j = s$ into the definition $(F_N)_ {kj} = \frac{1}{\sqrt{N}} \omega_N^{jk}$ from Note 04 gives $(F_N)_ {ks} = \frac{1}{\sqrt{N}} \omega_N^{sk}$, so:

$$
F_N\vert s\rangle = \sum_{k=0}^{N-1} \frac{1}{\sqrt{N}} \omega_N^{sk} \vert k\rangle = \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} \omega_N^{sk} \vert k\rangle
$$

The input is a single basis state $\vert s\rangle$, but applying $F_N$ transforms it into a superposition of $N$ basis states $\vert k\rangle$. This is the essence of the Fourier transform — an operation where the information of a single "position" spreads across all "frequencies."

Relabeling the summation index as $k \to j$, this becomes $\frac{1}{\sqrt{N}}\sum_j \omega_N^{js}\vert j\rangle$, which exactly matches the state of the first register after Step 2. Therefore:

$$
\frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} \omega_N^{js}\vert j\rangle = F_N \vert s\rangle
$$

That is, the state of the first register after Step 2 is $F_N\vert s\rangle$ itself.

The overall state after Step 2 is:

$$
\vert\Psi_2\rangle = \frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} e^{2\pi i j\varphi}\vert j\rangle \otimes \vert u\rangle = F_N\vert s\rangle \otimes \vert u\rangle
$$

Applying the inverse quantum Fourier transform $F_N^\dagger$ (see Note 04) to the first register, only the first register changes while the second register $\vert u\rangle$ remains unchanged:

$$
\vert\Psi_3\rangle = (F_N^\dagger \otimes I)\vert\Psi_2\rangle = F_N^\dagger F_N\vert s\rangle \otimes \vert u\rangle = \vert s\rangle \otimes \vert u\rangle
$$

### Step 4: Measurement

Measuring the first register in the computational basis yields $s$. Since $\varphi = s / N = s / 2^n$:

$$
\varphi = \frac{s}{2^n} = 0.j_1 j_2 \cdots j_n \quad \text{(binary representation of } s \text{)}
$$

This gives the phase $\varphi$ exactly with $n$-bit precision.

---

## Concrete Example: 2-Bit QPE ($n = 2$)

### Setup

Let $U$ be a single-qubit phase gate (see Note 02):

$$
U = R_\varphi = \begin{pmatrix} 1 & 0 \\\\ 0 & e^{2\pi i \varphi} \end{pmatrix}
$$

The eigenvector is $\vert 1\rangle$, and $U\vert 1\rangle = e^{2\pi i \varphi}\vert 1\rangle$.

Let $\varphi = 1/4$. Then $N = 2^n = 2^2 = 4$ and $s = \varphi \cdot N = 1$.

![2-bit QPE circuit](../../images/05_qpe_2bit.png)

### Initial State

$$
\vert\Psi_0\rangle = \vert 00\rangle \otimes \vert 1\rangle
$$

The first register is $q_1 q_2$ (counting register), and the second register is $\vert u\rangle = \vert 1\rangle$ (eigenstate).

### Step 1: Hadamard

Apply $H$ to $q_1, q_2$ of the first register. Since $H\vert 0\rangle = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$:

$$
H\vert 0\rangle \otimes H\vert 0\rangle = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} = \frac{1}{2}(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle)
$$

Including the second register $\vert 1\rangle$, the overall state is:

$$
\vert\Psi_1\rangle = \frac{1}{2}(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle) \otimes \vert 1\rangle
$$

### Step 2: Controlled Unitary

$q_1$ controls $U^2$ and $q_2$ controls $U^1$. Since $\varphi = 1/4$:

- $e^{2\pi i \cdot 2 \cdot 1/4} = e^{i\pi} = -1$ (phase kickback from $q_1$)
- $e^{2\pi i \cdot 1 \cdot 1/4} = e^{i\pi/2} = i$ (phase kickback from $q_2$)

**Apply controlled-$U^2$ ($q_1$ is control).**

The controlled unitary "applies $U$ to the second register only when the control bit is $\vert 1\rangle$." For each of the four terms in $\vert\Psi_1\rangle$, we check the value of $q_1$:

- $\vert 00\rangle\vert 1\rangle$: $q_1 = 0$ → do not apply $U^2$ → $\vert 00\rangle\vert 1\rangle$ (no change)
- $\vert 01\rangle\vert 1\rangle$: $q_1 = 0$ → do not apply $U^2$ → $\vert 01\rangle\vert 1\rangle$ (no change)
- $\vert 10\rangle\vert 1\rangle$: $q_1 = 1$ → apply $U^2$ to second register → $\vert 10\rangle(U^2\vert 1\rangle) = \vert 10\rangle \cdot e^{i\pi}\vert 1\rangle = -\vert 10\rangle\vert 1\rangle$
- $\vert 11\rangle\vert 1\rangle$: $q_1 = 1$ → apply $U^2$ to second register → $\vert 11\rangle(U^2\vert 1\rangle) = \vert 11\rangle \cdot e^{i\pi}\vert 1\rangle = -\vert 11\rangle\vert 1\rangle$

In the third and fourth terms, $U^2\vert 1\rangle = e^{2\pi i \cdot 2\varphi}\vert 1\rangle = e^{i\pi}\vert 1\rangle = -\vert 1\rangle$ was used. The second register remains the eigenvector $\vert 1\rangle$, but the phase $-1$ is applied to the whole (phase kickback).

Summarizing:

$$
\frac{1}{2}(\vert 00\rangle + \vert 01\rangle - \vert 10\rangle - \vert 11\rangle) \otimes \vert 1\rangle
$$

**Apply controlled-$U^1$ ($q_2$ is control).**

Similarly, we check the value of $q_2$:

- $\vert 00\rangle\vert 1\rangle$: $q_2 = 0$ → no change → $\vert 00\rangle\vert 1\rangle$
- $\vert 01\rangle\vert 1\rangle$: $q_2 = 1$ → $U\vert 1\rangle = e^{i\pi/2}\vert 1\rangle = i\vert 1\rangle$ → $i\vert 01\rangle\vert 1\rangle$
- $-\vert 10\rangle\vert 1\rangle$: $q_2 = 0$ → no change → $-\vert 10\rangle\vert 1\rangle$
- $-\vert 11\rangle\vert 1\rangle$: $q_2 = 1$ → $U\vert 1\rangle = i\vert 1\rangle$ → $-i\vert 11\rangle\vert 1\rangle$

Summarizing:

$$
\vert\Psi_2\rangle = \frac{1}{2}(\vert 00\rangle + i\vert 01\rangle - \vert 10\rangle - i\vert 11\rangle) \otimes \vert 1\rangle
$$

Rewriting in tensor product form:

$$
\vert\Psi_2\rangle = \frac{\vert 0\rangle + (-1)\vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + i\vert 1\rangle}{\sqrt{2}} \otimes \vert 1\rangle = \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}} \otimes \frac{\vert 0\rangle + i\vert 1\rangle}{\sqrt{2}} \otimes \vert 1\rangle
$$

### Step 3: Inverse QFT

Recall the $F_4$ DFT matrix from Note 04. The inverse QFT is $F_4^\dagger$.

The state of the first register (omitting the second register $\vert 1\rangle$) is:

$$
\frac{1}{2}(\vert 00\rangle + i\vert 01\rangle - \vert 10\rangle - i\vert 11\rangle)
$$

Written as a vector, this is $(1, i, -1, -i)^T / 2$.

Let us verify that this state has the form $F_4\vert s\rangle$. We reproduce the $F_4$ matrix from Note 04 and its action on each computational basis state:

$$
F_4 = \frac{1}{2}\begin{pmatrix} 1 & 1 & 1 & 1 \\\\ 1 & i & -1 & -i \\\\ 1 & -1 & 1 & -1 \\\\ 1 & -i & -1 & i \end{pmatrix}
$$

| Input | $j$ (decimal) | $F_4\vert j\rangle$ |
|------|-----------|---------------------|
| $\vert 00\rangle$ | 0 | $\frac{1}{2}(1, 1, 1, 1)^T$ |
| $\vert 01\rangle$ | 1 | $\frac{1}{2}(1, i, -1, -i)^T$ |
| $\vert 10\rangle$ | 2 | $\frac{1}{2}(1, -1, 1, -1)^T$ |
| $\vert 11\rangle$ | 3 | $\frac{1}{2}(1, -i, -1, i)^T$ |

Each row reads off a column of $F_4$. For example, $F_4\vert 01\rangle$ is the 1st column (0-indexed) of $F_4$:

$$
F_4\vert 01\rangle = \frac{1}{2}\begin{pmatrix} 1 \\\\ i \\\\ -1 \\\\ -i \end{pmatrix} = \frac{1}{2}(\vert 00\rangle + i\vert 01\rangle - \vert 10\rangle - i\vert 11\rangle)
$$

This exactly matches the state of the first register after Step 2, $(1, i, -1, -i)^T / 2$. That is:

$$
\frac{1}{2}(\vert 00\rangle + i\vert 01\rangle - \vert 10\rangle - i\vert 11\rangle) = F_4\vert 01\rangle
$$

Therefore, applying the inverse QFT $F_4^\dagger$:

$$
F_4^\dagger \cdot \frac{1}{2}(\vert 00\rangle + i\vert 01\rangle - \vert 10\rangle - i\vert 11\rangle) = F_4^\dagger \cdot F_4\vert 01\rangle = \vert 01\rangle
$$

### Step 4: Measurement

Measuring the first register yields $01$ (decimal $s = 1$) with probability 1.

$$
\varphi = \frac{s}{N} = \frac{1}{4}
$$

The correct phase $\varphi = 1/4$ has been exactly recovered.

---

## When $\varphi$ Cannot Be Exactly Represented with $n$ Bits

So far we considered the case $\varphi = s/2^n$ ($s$ an integer). In this case, $\vert s\rangle$ was obtained with probability 1 after the inverse QFT.

However, in general $\varphi$ cannot be exactly represented with $n$ bits. For example, when estimating $\varphi = 1/3$ with $n = 3$ bits, $\varphi \cdot 2^3 = 8/3 \approx 2.67$ is not an integer.

### Accuracy of the Approximation

When $\varphi$ cannot be exactly represented, the state after the inverse QFT becomes a superposition of $\vert s\rangle$ states. The measurement result becomes probabilistic, but the $s/2^n$ closest to $\varphi$ appears with the highest probability.

Specifically, it can be shown that the $n$-bit value $\tilde{\varphi}$ closest to $\varphi$ is obtained with probability at least $4/\pi^2 \approx 0.405$.

---

## Overall Picture of QPE

Let us organize the entire protocol again.

### Input

- A quantum circuit implementing the unitary operator $U$ (controlled versions of $U, U^2, U^4, \ldots, U^{2^{n-1}}$ are needed)
- An eigenvector $\vert u\rangle$ of $U$
- The number of qubits $n$ in the counting register (determines the precision)

### Procedure

$$
\vert 0\rangle^{\otimes n}\vert u\rangle
 \overset{ H^{\otimes n} }{\longrightarrow} 
\frac{1}{\sqrt{N}}\sum_j \vert j\rangle\vert u\rangle
 \overset{ CU^{2^k} }{\longrightarrow} 
\frac{1}{\sqrt{N}}\sum_j e^{2\pi ij\varphi}\vert j\rangle\vert u\rangle
 \overset{ \text{QFT}^{-1} }{\longrightarrow} 
\vert s\rangle\vert u\rangle
$$

### Output

From the measurement result $s$ of the counting register, $\varphi \approx s/2^n$ is taken as the estimated value of the phase.

### Computational Complexity

- Gate count: $O(n^2)$ (inverse QFT part) $+ O(n)$ (controlled unitary, depends on the implementation cost of $U^{2^k}$)
- Number of qubits: $n + m$ (counting register $n$ bits + eigenstate register $m$ bits)

---

## When the Eigenvector is Unknown

In practice, the eigenvector $\vert u\rangle$ is often not precisely known. However, QPE works correctly even when a superposition of eigenvectors is input to the second register.

Let the eigenvectors of $U$ be $\vert u_0\rangle, \vert u_1\rangle, \ldots$ with corresponding phases $\varphi_0, \varphi_1, \ldots$. If the input state is:

$$
\vert\phi\rangle = \sum_l c_l \vert u_l\rangle
$$

then the state after QPE is:

$$
\sum_l c_l \vert\tilde{s}_l\rangle\vert u_l\rangle
$$

Measuring the counting register yields $\tilde{s}_l$ (the estimate of $\varphi_l$) with probability $\lvert c_l\rvert^2$. Simultaneously, the second register is projected onto the corresponding eigenvector $\vert u_l\rangle$.

In other words, QPE functions as an operation that **simultaneously determines eigenvalues and eigenvectors**.

---

## Summary

### QPE Setup and Variable Relationships

QPE estimates the phase $\varphi$ from $U\vert u\rangle = e^{2\pi i\varphi}\vert u\rangle$. The phase $\varphi$ is restricted to $0 \le \varphi < 1$.

Let the number of bits in the counting register be $n$ and set $N = 2^n$. When $\varphi = s/N$ ($s$ an integer), QPE returns $s$ as the measurement result with probability 1. The phase is recovered from the measured $s$ as $\varphi = s/2^n$.

When $\varphi$ cannot be exactly represented in the form $s/2^n$, the closest $s$ is obtained with the highest probability (approximation).

### Overview

| Concept | Content |
|------|------|
| Goal | Estimate the phase $\varphi$ from $U\vert u\rangle = e^{2\pi i\varphi}\vert u\rangle$ |
| Core idea | Phase kickback + inverse Quantum Fourier Transform |
| Circuit structure | $H^{\otimes n}$ → controlled $U^{2^k}$ → $\text{QFT}^{-1}$ → measurement |
| Measurement result | Integer $s$. The estimated phase is $\varphi \approx s/2^n$ |
| Exact case | If $\varphi = s/2^n$, the correct $s$ is obtained with probability 1 |
| Approximate case | The nearest $s$ is obtained with high probability |
| When eigenvector is unknown | Input a superposition to simultaneously obtain eigenvalues and eigenvectors |
| Applications | Shor's algorithm (Note 06), quantum chemistry, quantum simulation |
