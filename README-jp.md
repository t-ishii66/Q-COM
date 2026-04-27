# 量子ビットからショアのアルゴリズムへ

![Alice and Bob](images/alice-bob-top.png)

量子コンピュータの基礎を、理論ノートと Qiskit による実装の両面から学ぶプロジェクトです。

## 構成

### `notes/jp/` — 理論ノート

教科書的な記述で、量子コンピュータの物理・数学を解説します。

| ファイル | 内容 |
|---|---|
| [01_qubit.md](notes/jp/01_qubit.md) | 量子ビット |
| [02_quantum_gates.md](notes/jp/02_quantum_gates.md) | 量子ゲート |
| [03_quantum_teleportation.md](notes/jp/03_quantum_teleportation.md) | 量子テレポーテーション |
| [04_discrete_fourier_transform.md](notes/jp/04_discrete_fourier_transform.md) | 離散フーリエ変換 |
| [05_quantum_phase_estimation.md](notes/jp/05_quantum_phase_estimation.md) | 量子位相推定 (QPE) |
| [06_shor_algorithm.md](notes/jp/06_shor_algorithm.md) | ショアのアルゴリズム |

### `notebooks/jp/` — Qiskit 実装

理論ノートの内容を Qiskit で実装・検証する Jupyter ノートブックです。Qiskit の API や Python の構文についても解説しています。

| ファイル | 内容 |
|---|---|
| [00_environment.md](notebooks/jp/00_environment.md) | 環境構築 |
| [01_qubit_ordering.ipynb](notebooks/jp/01_qubit_ordering.ipynb) | 量子ビットの順序（教科書と Qiskit の規約の違い） |
| [02_qiskit_basics.ipynb](notebooks/jp/02_qiskit_basics.ipynb) | Qiskit の基本操作（ゲート、測定、制御、逆操作など） |
| [03_quantum_teleportation.ipynb](notebooks/jp/03_quantum_teleportation.ipynb) | 量子テレポーテーションの実装と検証 |
| [04_quantum_fourier_transform.ipynb](notebooks/jp/04_quantum_fourier_transform.ipynb) | 量子フーリエ変換 (QFT) |
| [05_quantum_phase_estimation.ipynb](notebooks/jp/05_quantum_phase_estimation.ipynb) | 量子位相推定 (QPE) |
| [06_shor_algorithm.ipynb](notebooks/jp/06_shor_algorithm.ipynb) | ショアのアルゴリズム |

## ビット順の規約

`notes/` と `notebooks/` ではビット順が異なります。

- **`notes/`（教科書）**: ビッグエンディアン、1始まり — $\vert q_1 q_2 q_3\rangle$
- **`notebooks/`（Qiskit）**: リトルエンディアン、0始まり — $\vert q_2 q_1 q_0\rangle$

詳しくは [notebooks/jp/01_qubit_ordering.ipynb](notebooks/jp/01_qubit_ordering.ipynb) を参照してください。

## 環境構築

[notebooks/jp/00_environment.md](notebooks/jp/00_environment.md) を参照してください。

# クレジット

- 企画: t-ishii66（大学で物理を学ぶ。システムエンジニア。英会話奮闘中。）
- 制作: Claude Opus 4.6, t-ishii66
- notesレビュー: t-ishii66
- notebooksレビュー: t-ishii66
- 発行日: 2026/4/28
- バージョン: 1.0.0
- Copyright(C) 2026 t-ishii66. All rights reserved.
