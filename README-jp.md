---
title: "量子ビットからショアのアルゴリズムへ"
description: "量子ビット・量子ゲート・量子テレポーテーション・量子フーリエ変換・量子位相推定・ショアのアルゴリズムを、教科書的な理論ノートと Qiskit ノートブックで段階的に学ぶプロジェクト。"
keywords: "量子コンピュータ, 量子計算, ショアのアルゴリズム, 量子フーリエ変換, QFT, 量子位相推定, QPE, 量子テレポーテーション, 量子ビット, 量子ゲート, エンタングルメント, ベル状態, アダマールゲート, CNOT, パウリゲート, 素因数分解, Qiskit, チュートリアル, ドキュメント, 自作"
lang: ja
---

# 量子ビットからショアのアルゴリズムへ

![Alice and Bob](images/alice-bob-top.png)

量子コンピュータの基礎を、理論ノートと Qiskit による実装の両面から学ぶプロジェクトです。

<!-- SEO intro added by setup-github-pages; review and adjust -->

「**量子コンピュータの基礎を一から自分で組み立てたい**」「**量子ビット** と **量子ゲート** がどう **エンタングルメント** に繋がるのか知りたい」「**量子フーリエ変換 (QFT)** や **量子位相推定 (QPE)** から **ショアのアルゴリズム** までの流れを、**Qiskit** で動かしながら理解したい」── そんな人のための日英バイリンガル教材です。扱うテーマは **量子テレポーテーション**、**ベル状態**、**アダマールゲート**、**CNOT**、**パウリゲート**、**素因数分解**（位数発見）など。

<!-- /SEO intro -->

## 構成

### `docs/jp/` — 理論ノート

教科書的な記述で、量子コンピュータの物理・数学を解説します。

| ファイル | 内容 |
|---|---|
| [01_qubit.md](docs/jp/01_qubit.md) | 量子ビット |
| [02_quantum_gates.md](docs/jp/02_quantum_gates.md) | 量子ゲート |
| [03_quantum_teleportation.md](docs/jp/03_quantum_teleportation.md) | 量子テレポーテーション |
| [04_discrete_fourier_transform.md](docs/jp/04_discrete_fourier_transform.md) | 離散フーリエ変換 |
| [05_quantum_phase_estimation.md](docs/jp/05_quantum_phase_estimation.md) | 量子位相推定 (QPE) |
| [06_shor_algorithm.md](docs/jp/06_shor_algorithm.md) | ショアのアルゴリズム |

### `notebooks/jp/` — Qiskit 実装

理論ノートの内容を Qiskit で実装・検証する Jupyter ノートブックです。Qiskit の API や Python の構文についても解説しています。

| ファイル | 内容 |
|---|---|
| [00_environment.md](notebooks/jp/00_environment.md) | 環境構築 |
| [01_qubit_ordering.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/01_qubit_ordering.ipynb) | 量子ビットの順序（教科書と Qiskit の規約の違い） |
| [02_qiskit_basics.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/02_qiskit_basics.ipynb) | Qiskit の基本操作（ゲート、測定、制御、逆操作など） |
| [03_quantum_teleportation.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/03_quantum_teleportation.ipynb) | 量子テレポーテーションの実装と検証 |
| [04_quantum_fourier_transform.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/04_quantum_fourier_transform.ipynb) | 量子フーリエ変換 (QFT) |
| [05_quantum_phase_estimation.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/05_quantum_phase_estimation.ipynb) | 量子位相推定 (QPE) |
| [06_shor_algorithm.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/06_shor_algorithm.ipynb) | ショアのアルゴリズム |

## ビット順の規約

`docs/` と `notebooks/` ではビット順が異なります。

- **`docs/`（教科書）**: ビッグエンディアン、1始まり — $\vert q_1 q_2 q_3\rangle$
- **`notebooks/`（Qiskit）**: リトルエンディアン、0始まり — $\vert q_2 q_1 q_0\rangle$

詳しくは [notebooks/jp/01_qubit_ordering.ipynb](https://github.com/t-ishii66/Q-COM/blob/main/notebooks/jp/01_qubit_ordering.ipynb) を参照してください。

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
