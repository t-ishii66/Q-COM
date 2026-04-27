# 03: 量子テレポーテーション（Quantum Teleportation）

## 量子テレポーテーションとは

量子テレポーテーションは、エンタングルメントと古典通信を利用して、ある量子ビットの状態を離れた場所にある別の量子ビットに転送するプロトコルである。

重要な点を先に整理する：

- 物質やエネルギーが移動するわけではない。転送されるのは **量子状態（情報）** である
- 光速を超える通信にはならない。プロトコルの途中で **古典通信（2ビット）** が必要であり、これが光速の制約を受ける
- 転送元の量子状態は **破壊される**。これは量子複製不可能定理（ノート01参照）と矛盾しない

### 前提知識

本ノートでは以下を既知とする：

- 量子ビットの状態表現、測定、エンタングルメント、ベル状態（ノート01）
- パウリゲート $X$, $Z$、アダマールゲート $H$、CNOT ゲート（ノート02）

---

## プロトコルの設定

### 登場人物と役割

- **Alice**: 量子状態 $\vert\psi\rangle$ を持っており、これを Bob に送りたい
- **Bob**: Alice から量子状態を受け取りたい

Alice と Bob は物理的に離れた場所にいる。

### 使用するリソース

1. **エンタングルされた量子ビット対（ベル対）**: Alice と Bob が1つずつ持つ
2. **古典通信路**: Alice から Bob へ2ビットの古典情報を送る手段
3. **量子ビット**: 合計3つ（Alice が2つ、Bob が1つ）

### 量子ビットの割り当て

3つの量子ビットを $q_1, q_2, q_3$ とする（ノート01の慣習に従い左から番号を振る）：

| 量子ビット | 所持者 | 役割 |
|-----------|--------|------|
| $q_1$ | Alice | 転送したい未知の量子状態 $\vert\psi\rangle$ |
| $q_2$ | Alice | ベル対の Alice 側 |
| $q_3$ | Bob | ベル対の Bob 側 |

---

## プロトコルの手順

### 初期状態の準備

転送したい状態を一般的な1量子ビット状態とする：

$$
\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle
$$

ここで $\alpha, \beta$ は Alice にも未知の複素数であり、 $\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1$ を満たす。

Alice と Bob はあらかじめベル状態 $\vert\Phi^+\rangle = \frac{\vert 00\rangle + \vert 11\rangle}{\sqrt{2}}$ を共有している（ $q_2$ が Alice、 $q_3$ が Bob）。

3量子ビット系の初期状態は：

$$
\vert\Psi_0\rangle = \vert\psi\rangle_{q_1} \otimes \vert\Phi^+\rangle_{q_2 q_3}
$$

これを展開する：

$$
\vert\Psi_0\rangle = (\alpha\vert 0\rangle + \beta\vert 1\rangle) \otimes \frac{\vert 00\rangle + \vert 11\rangle}{\sqrt{2}}
$$

$$
= \frac{\alpha}{\sqrt{2}}(\vert 000\rangle + \vert 011\rangle) + \frac{\beta}{\sqrt{2}}(\vert 100\rangle + \vert 111\rangle)
$$

ここで $\vert abc\rangle = \vert a\rangle_{q_1} \vert b\rangle_{q_2} \vert c\rangle_{q_3}$ である。

### ステップ 1: CNOT ゲート

Alice が $q_1$（制御）と $q_2$（標的）に CNOT ゲートを適用する。

CNOT の動作は $\vert a, b\rangle \to \vert a, a \oplus b\rangle$ である（ノート02参照）。 $q_3$ には何もしないので $\text{CNOT}_{12} \otimes I_3$ を適用する：

$$
\vert 000\rangle \overset{ \text{CNOT}_{12} }{\longrightarrow} \vert 000\rangle, \quad \vert 011\rangle \overset{ \text{CNOT}_{12} }{\longrightarrow} \vert 011\rangle
$$

$$
\vert 100\rangle \overset{ \text{CNOT}_{12} }{\longrightarrow} \vert 110\rangle, \quad \vert 111\rangle \overset{ \text{CNOT}_{12} }{\longrightarrow} \vert 101\rangle
$$

したがって：

$$
\vert\Psi_1\rangle = \frac{\alpha}{\sqrt{2}}(\vert 000\rangle + \vert 011\rangle) + \frac{\beta}{\sqrt{2}}(\vert 110\rangle + \vert 101\rangle)
$$

### ステップ 2: アダマールゲート

Alice が $q_1$ にアダマールゲート $H$ を適用する。 $q_2, q_3$ には何もしないので $H_1 \otimes I_2 \otimes I_3$ を適用する。

$H$ の動作は $\vert 0\rangle \to \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$、 $\vert 1\rangle \to \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}}$ である（ノート02参照）。

各項に $H$ を適用する：

$$
\vert 0\rangle \vert 00\rangle \overset{ H_1 }{\longrightarrow} \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \vert 00\rangle, \quad \vert 0\rangle \vert 11\rangle \overset{ H_1 }{\longrightarrow} \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \vert 11\rangle
$$

$$
\vert 1\rangle \vert 10\rangle \overset{ H_1 }{\longrightarrow} \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}} \vert 10\rangle, \quad \vert 1\rangle \vert 01\rangle \overset{ H_1 }{\longrightarrow} \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}} \vert 01\rangle
$$

これを代入して整理する：

$$
\vert\Psi_2\rangle = \frac{\alpha}{2}(\vert 0\rangle + \vert 1\rangle)(\vert 00\rangle + \vert 11\rangle) + \frac{\beta}{2}(\vert 0\rangle - \vert 1\rangle)(\vert 10\rangle + \vert 01\rangle)
$$

展開すると：

$$
\vert\Psi_2\rangle = \frac{1}{2}\Big[\vert 00\rangle(\alpha\vert 0\rangle + \beta\vert 1\rangle) + \vert 01\rangle(\alpha\vert 1\rangle + \beta\vert 0\rangle) + \vert 10\rangle(\alpha\vert 0\rangle - \beta\vert 1\rangle) + \vert 11\rangle(\alpha\vert 1\rangle - \beta\vert 0\rangle)\Big]
$$

ここで左の2量子ビットは $q_1 q_2$（Alice 側）、右の1量子ビットは $q_3$（Bob 側）である。

---

## 展開の導出（詳細）

上の整理は量子テレポーテーションの核心なので、省略なく示す。

$\vert\Psi_2\rangle$ の展開を $q_1 q_2$ の状態でグループ化する。まず全8項を書き出す：

$$
\vert\Psi_2\rangle = \frac{\alpha}{2}\vert 000\rangle + \frac{\alpha}{2}\vert 011\rangle + \frac{\alpha}{2}\vert 100\rangle + \frac{\alpha}{2}\vert 111\rangle + \frac{\beta}{2}\vert 010\rangle + \frac{\beta}{2}\vert 001\rangle - \frac{\beta}{2}\vert 110\rangle - \frac{\beta}{2}\vert 101\rangle
$$

$q_1 q_2$ の値ごとに分類する：

**$q_1 q_2 = 00$ の項：**

$$
\frac{\alpha}{2}\vert 000\rangle + \frac{\beta}{2}\vert 001\rangle = \frac{1}{2}\vert 00\rangle \otimes (\alpha\vert 0\rangle + \beta\vert 1\rangle)
$$

**$q_1 q_2 = 01$ の項：**

$$
\frac{\alpha}{2}\vert 011\rangle + \frac{\beta}{2}\vert 010\rangle = \frac{1}{2}\vert 01\rangle \otimes (\beta\vert 0\rangle + \alpha\vert 1\rangle)
$$

**$q_1 q_2 = 10$ の項：**

$$
\frac{\alpha}{2}\vert 100\rangle - \frac{\beta}{2}\vert 101\rangle = \frac{1}{2}\vert 10\rangle \otimes (\alpha\vert 0\rangle - \beta\vert 1\rangle)
$$

**$q_1 q_2 = 11$ の項：**

$$
\frac{\alpha}{2}\vert 111\rangle - \frac{\beta}{2}\vert 110\rangle = \frac{1}{2}\vert 11\rangle \otimes (-\beta\vert 0\rangle + \alpha\vert 1\rangle)
$$

まとめると：

$$
\vert\Psi_2\rangle = \frac{1}{2}\Big[\vert 00\rangle(\alpha\vert 0\rangle + \beta\vert 1\rangle) + \vert 01\rangle(\beta\vert 0\rangle + \alpha\vert 1\rangle) + \vert 10\rangle(\alpha\vert 0\rangle - \beta\vert 1\rangle) + \vert 11\rangle(-\beta\vert 0\rangle + \alpha\vert 1\rangle)\Big]
$$

---

## ステップ 3: Alice の測定

Alice が $q_1$ と $q_2$ を計算基底で測定する。4つの結果が等確率 $1/4$ で得られる。

測定結果に応じて、Bob の $q_3$ の状態は次のようになる：

| Alice の測定結果 ($q_1 q_2$) | Bob の $q_3$ の状態 | $\vert\psi\rangle$ との関係 |
|---|---|---|
| $\vert 00\rangle$ | $\alpha\vert 0\rangle + \beta\vert 1\rangle$ | $\vert\psi\rangle$ そのもの |
| $\vert 01\rangle$ | $\beta\vert 0\rangle + \alpha\vert 1\rangle$ | $X\vert\psi\rangle$ |
| $\vert 10\rangle$ | $\alpha\vert 0\rangle - \beta\vert 1\rangle$ | $Z\vert\psi\rangle$ |
| $\vert 11\rangle$ | $-\beta\vert 0\rangle + \alpha\vert 1\rangle$ | $ZX\vert\psi\rangle$（全体位相を除く） |

ここで $X$（ビット反転）と $Z$（位相反転）はパウリゲートである（ノート02参照）：

$$
X = \begin{pmatrix} 0 & 1 \\\\ 1 & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\\\ 0 & -1 \end{pmatrix}
$$

### 関係の確認

$\vert 01\rangle$ の場合を確認する：

$$
X\vert\psi\rangle = X(\alpha\vert 0\rangle + \beta\vert 1\rangle) = \alpha\vert 1\rangle + \beta\vert 0\rangle = \beta\vert 0\rangle + \alpha\vert 1\rangle \quad \checkmark
$$

$\vert 10\rangle$ の場合：

$$
Z\vert\psi\rangle = Z(\alpha\vert 0\rangle + \beta\vert 1\rangle) = \alpha\vert 0\rangle - \beta\vert 1\rangle \quad \checkmark
$$

$\vert 11\rangle$ の場合（$ZX = -XZ$ なので全体位相 $-1$ を除いて同じ）：

$$
ZX\vert\psi\rangle = Z(\beta\vert 0\rangle + \alpha\vert 1\rangle) = \beta\vert 0\rangle - \alpha\vert 1\rangle = -(\alpha\vert 1\rangle - \beta\vert 0\rangle) = -(-\beta\vert 0\rangle + \alpha\vert 1\rangle)
$$

全体位相 $-1$ は観測に影響しないので、Bob の状態は $-\beta\vert 0\rangle + \alpha\vert 1\rangle$ と同等である。$\checkmark$

---

## ステップ 4: 古典通信と補正操作

Alice は測定結果（2ビットの古典情報）を古典通信路で Bob に送る。

Bob は受け取った情報に基づいて、 $q_3$ に補正ゲートを適用する：

| Alice の測定結果 | Bob の補正操作 | 補正後の状態 |
|---|---|---|
| $00$ | 何もしない（ $I$） | $\alpha\vert 0\rangle + \beta\vert 1\rangle = \vert\psi\rangle$ |
| $01$ | $X$ を適用 | $X(\beta\vert 0\rangle + \alpha\vert 1\rangle) = \alpha\vert 0\rangle + \beta\vert 1\rangle = \vert\psi\rangle$ |
| $10$ | $Z$ を適用 | $Z(\alpha\vert 0\rangle - \beta\vert 1\rangle) = \alpha\vert 0\rangle + \beta\vert 1\rangle = \vert\psi\rangle$ |
| $11$ | $ZX$ を適用 | $ZX(-\beta\vert 0\rangle + \alpha\vert 1\rangle) = \alpha\vert 0\rangle + \beta\vert 1\rangle = \vert\psi\rangle$ |

### $\vert 01\rangle$ の場合の補正を確認

Bob の状態は $\beta\vert 0\rangle + \alpha\vert 1\rangle$ である。 $X$ を適用すると：

$$
X(\beta\vert 0\rangle + \alpha\vert 1\rangle) = \beta\vert 1\rangle + \alpha\vert 0\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle = \vert\psi\rangle
$$

### $\vert 11\rangle$ の場合の補正を確認

Bob の状態は $-\beta\vert 0\rangle + \alpha\vert 1\rangle$ である。まず $X$ を適用し、次に $Z$ を適用する：

$$
X(-\beta\vert 0\rangle + \alpha\vert 1\rangle) = -\beta\vert 1\rangle + \alpha\vert 0\rangle = \alpha\vert 0\rangle - \beta\vert 1\rangle
$$

$$
Z(\alpha\vert 0\rangle - \beta\vert 1\rangle) = \alpha\vert 0\rangle + \beta\vert 1\rangle = \vert\psi\rangle
$$

どの測定結果であっても、補正後に Bob は $\vert\psi\rangle$ を得る。

---

## 具体例

$\vert\psi\rangle = \vert +\rangle = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$ をテレポーテーションする場合を追跡する。 $\alpha = \beta = \frac{1}{\sqrt{2}}$ である。

### 初期状態（ベル対の準備後）

$q_2$ に $H$、$\text{CNOT}_{23}$ を適用してベル対を生成した後の状態：

$$
\vert\Psi_0\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) \otimes \frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 11\rangle) = \frac{1}{2}(\vert 000\rangle + \vert 011\rangle + \vert 100\rangle + \vert 111\rangle)
$$

### $\text{CNOT}_{12}$ 後

$$
\vert\Psi_1\rangle = \frac{1}{2}(\vert 000\rangle + \vert 011\rangle + \vert 110\rangle + \vert 101\rangle)
$$

### アダマール後

$$
\vert\Psi_2\rangle = \frac{1}{2\sqrt{2}}\Big[(\vert 0\rangle + \vert 1\rangle)\vert 00\rangle + (\vert 0\rangle + \vert 1\rangle)\vert 11\rangle + (\vert 0\rangle - \vert 1\rangle)\vert 10\rangle + (\vert 0\rangle - \vert 1\rangle)\vert 01\rangle\Big]
$$

$q_1 q_2$ でグループ化する：

$$
\vert\Psi_2\rangle = \frac{1}{2}\Big[\vert 00\rangle \cdot \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} + \vert 01\rangle \cdot \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} + \vert 10\rangle \cdot \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}} + \vert 11\rangle \cdot \frac{-\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}\Big]
$$

ここで $\frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} = \vert +\rangle$ であり、 $\frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}} = \vert -\rangle$ である。

| Alice の測定結果 | Bob の状態 | 補正操作 | 補正後 |
|---|---|---|---|
| $00$ | $\vert +\rangle$ | $I$ | $\vert +\rangle$ |
| $01$ | $\vert +\rangle$ | $X$ | $X\vert +\rangle = \vert +\rangle$ |
| $10$ | $\vert -\rangle$ | $Z$ | $Z\vert -\rangle = \vert +\rangle$ |
| $11$ | $\frac{-\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$ | $ZX$ | $\vert +\rangle$ |

$\vert 01\rangle$ の場合、 $X\vert +\rangle = X \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} = \frac{\vert 1\rangle + \vert 0\rangle}{\sqrt{2}} = \vert +\rangle$ である。 $X$ はビットを反転するが、 $\vert +\rangle$ は $\vert 0\rangle$ と $\vert 1\rangle$ の等しい重ね合わせなので反転しても変わらない。

$\vert 10\rangle$ の場合、 $Z\vert -\rangle = Z \frac{\vert 0\rangle - \vert 1\rangle}{\sqrt{2}} = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} = \vert +\rangle$ である。 $Z$ は $\vert 1\rangle$ の符号を反転するので、 $-$ の符号が $+$ に変わる。

すべての場合で Bob は $\vert +\rangle$ を得る。

---

## プロトコルの回路表現

量子テレポーテーションの回路を図示する。時間は左から右に進む：

> **注意：** 本文では量子ビットを $q_1, q_2, q_3$（1始まり）で記述しているが、回路図では $q_0, q_1, q_2$（0始まり）で表示される。インデックスが1つずれている点に注意。対応は $q_1 \to q_0$、$q_2 \to q_1$、$q_3 \to q_2$ である。

![量子テレポーテーション回路](../../images/03_teleportation.png)

回路は3つのフェーズからなる：

**準備フェーズ（図の前段、省略）：** $q_2$ と $q_3$ にベル対を生成する（ $H$ + CNOT）。

**Alice の操作：** $q_1$ と $q_2$ に CNOT、 $q_1$ に $H$、その後 $q_1$ と $q_2$ を測定。

**Bob の補正：** 測定結果 $m_2$（ $q_2$ の測定結果）に応じて $X^{m_2}$、 $m_1$（ $q_1$ の測定結果）に応じて $Z^{m_1}$ を $q_3$ に適用。二重線（ $=$）は古典ビットの伝送を表す。

---

## ベル対の生成

ベル状態 $\vert\Phi^+\rangle = \frac{\vert 00\rangle + \vert 11\rangle}{\sqrt{2}}$ は、 $q_2$ にアダマールゲートを適用して重ね合わせを作り、 $\text{CNOT}_{23}$ でエンタングルメントを生成することで得られる（ノート01, 02参照）。

---

## 量子複製不可能定理との整合性

量子テレポーテーションは量子状態を「コピー」しているように見えるかもしれないが、そうではない。

**量子複製不可能定理（No-Cloning Theorem）** は、任意の未知の量子状態を複製する操作は存在しないことを示す（ノート01参照）。

テレポーテーションでは、ステップ3の測定によって Alice の $q_1$ の状態は **破壊** される。測定後、 $q_1$ は $\vert 0\rangle$ か $\vert 1\rangle$ のどちらかに射影されており、元の $\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle$ は Alice 側にもう存在しない。

つまり、テレポーテーションは量子状態の「コピー」ではなく「移動」である。状態は一方から消え、他方に現れる。これは量子複製不可能定理と完全に整合する。

---

## 古典通信の必要性

Alice の測定が終わった時点で、Bob の $q_3$ は4つの状態のうちどれかになっている。しかし、Bob はどの状態かを知らない。古典通信で測定結果を受け取らなければ、どの補正ゲートを適用すべきかわからず、元の状態を復元できない。

このことは、量子テレポーテーションが超光速通信に使えないことを意味する。Alice から Bob への情報伝送は、古典通信路の速度に制約される。

---

## まとめ

| 概念 | 内容 |
|------|------|
| 転送されるもの | 量子状態（物質ではない） |
| 必要なリソース | ベル対1組 + 古典通信2ビット |
| 使用するゲート | CNOT, $H$, $X$, $Z$ |
| 量子ビット数 | 3（Alice: $q_1, q_2$、Bob: $q_3$） |
| 測定回数 | 2（ $q_1$ と $q_2$ を計算基底で測定） |
| 補正操作 | 測定結果 $m_1 m_2$ に応じて $Z^{m_1} X^{m_2}$ |
| 複製不可能定理 | 矛盾しない（元の状態は測定で破壊される） |
| 超光速通信 | 不可能（古典通信が必須） |
