"""
量子フーリエ変換（QFT）— ノート03 の具体例を Qiskit で確認する

ノート03 では DFT 行列 F_N を定義し、N=2, N=4 の場合を手計算した。
このスクリプトでは、同じ変換を量子回路として構成し、
状態ベクトルシミュレータで結果がノートの計算と一致することを確認する。

- N=2 (1量子ビット): QFT = アダマールゲート H
- N=4 (2量子ビット): QFT = H, 制御位相ゲート, SWAP の組み合わせ

注意: Qiskit はリトルエンディアン（q_0 が最下位ビット）を採用しており、
ノートのベクトル表記（ビッグエンディアン）とはビット順が逆になる。
QFT 回路は上位ビット（q_{n-1}）から処理を開始することで、
回路のユニタリ行列がノートの DFT 行列 F_N と一致するように構成する。
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator


# ========================================
# QFT 回路の構成
# ========================================

def qft_circuit(n: int) -> QuantumCircuit:
    """n 量子ビットの QFT 回路を構成する。

    QFT の回路は以下のパターンで構成される:
      1. 上位ビットから順に処理する（Qiskit では q_{n-1} から q_0 へ）:
         - H ゲートを適用
         - より下位の各量子ビットから制御位相ゲート CP(2π/2^m) を適用
      2. 最後にビット順を反転する SWAP
    """
    qc = QuantumCircuit(n, name=f"QFT({n})")

    for j in reversed(range(n)):
        qc.h(j)
        for k in reversed(range(j)):
            angle = 2 * np.pi / (2 ** (j - k + 1))
            qc.cp(angle, k, j)

    # ビット順の反転
    for i in range(n // 2):
        qc.swap(i, n - 1 - i)

    return qc


def show_statevector(label: str, sv: Statevector) -> None:
    """状態ベクトルを見やすく表示する。"""
    n = int(np.log2(len(sv)))
    print(f"  {label}:")
    for i, amp in enumerate(sv):
        if abs(amp) > 1e-10:
            real = amp.real if abs(amp.real) > 1e-10 else 0
            imag = amp.imag if abs(amp.imag) > 1e-10 else 0
            basis = format(i, f"0{n}b")
            print(f"    |{basis}⟩: {real:+.4f} {imag:+.4f}i")


# ========================================
# N=2 (1量子ビット): QFT = アダマールゲート
# ========================================

print("=" * 56)
print("N=2 (1量子ビット) の QFT")
print("=" * 56)
print()

qft1 = qft_circuit(1)
print("回路:")
print(qft1.draw())
print()

# --- ノート03「N=2 の計算例」に対応 ---

# |0⟩ → (1/√2)(|0⟩ + |1⟩)  ... F_2 (1,0)^T = (1,1)^T / √2
print("計算例 1: |0⟩ に QFT を適用")
qc = QuantumCircuit(1)
qc.append(qft1, [0])
sv = Statevector.from_instruction(qc)
show_statevector("QFT|0⟩", sv)
print(f"  期待値: (1/√2)(|0⟩ + |1⟩)")
print()

# |+⟩ → |0⟩  ... F_2 (1,1)^T / √2 = (1,0)^T
print("計算例 2: |+⟩ に QFT を適用")
qc = QuantumCircuit(1)
qc.h(0)
qc.append(qft1, [0])
sv = Statevector.from_instruction(qc)
show_statevector("QFT|+⟩", sv)
print(f"  期待値: |0⟩")
print()


# ========================================
# N=4 (2量子ビット) の QFT
# ========================================

print("=" * 56)
print("N=4 (2量子ビット) の QFT")
print("=" * 56)
print()

qft2 = qft_circuit(2)
print("回路:")
print(qft2.draw())
print()

# --- ノート03「N=4 の計算例」に対応 ---

# 計算例 1: 一様分布 → 第0成分に集中
# (1/2)(1,1,1,1)^T → (1,0,0,0)^T
print("計算例 1: (1/2)(|00⟩+|01⟩+|10⟩+|11⟩) に QFT を適用")
sv_in = Statevector([0.5, 0.5, 0.5, 0.5])
sv_out = sv_in.evolve(qft2)
show_statevector("結果", sv_out)
print(f"  期待値: |00⟩")
print()

# 計算例 2: 交互パターン → 最高周波数成分
# (1/2)(1,-1,1,-1)^T → (0,0,1,0)^T
print("計算例 2: (1/2)(|00⟩-|01⟩+|10⟩-|11⟩) に QFT を適用")
sv_in = Statevector([0.5, -0.5, 0.5, -0.5])
sv_out = sv_in.evolve(qft2)
show_statevector("結果", sv_out)
print(f"  期待値: |10⟩")
print()

# 計算例 3: 単一成分 → 一様分布
# (1,0,0,0)^T → (1/2)(1,1,1,1)^T
print("計算例 3: |00⟩ に QFT を適用")
sv_in = Statevector([1, 0, 0, 0])
sv_out = sv_in.evolve(qft2)
show_statevector("結果", sv_out)
print(f"  期待値: すべて +0.5000")
print()


# ========================================
# QFT 行列と DFT 行列 F_N の比較
# ========================================

print("=" * 56)
print("QFT 回路のユニタリ行列と DFT 行列 F_N の比較")
print("=" * 56)
print()

for n in [1, 2]:
    N = 2 ** n
    qft = qft_circuit(n)

    # QFT 回路からユニタリ行列を取得
    U_qft = Operator(qft).data

    # DFT 行列 F_N をノートの定義どおりに構成
    # (F_N)_{kj} = (1/√N) * ω_N^{jk},  ω_N = e^{2πi/N}
    omega = np.exp(2j * np.pi / N)
    F_N = np.array([
        [omega ** (j * k) for j in range(N)] for k in range(N)
    ]) / np.sqrt(N)

    match = np.allclose(U_qft, F_N)
    print(f"N={N} (n={n}量子ビット):")
    print(f"  QFT回路のユニタリ行列 = DFT行列 F_{N}？ → {match}")
    if match:
        print(f"  F_{N} =")
        for row in F_N:
            entries = []
            for val in row:
                r = val.real if abs(val.real) > 1e-10 else 0
                im = val.imag if abs(val.imag) > 1e-10 else 0
                entries.append(f"{r:+.4f}{im:+.4f}i")
            print(f"    [{', '.join(entries)}]")
    else:
        print(f"  最大誤差: {np.max(np.abs(U_qft - F_N)):.2e}")
    print()
