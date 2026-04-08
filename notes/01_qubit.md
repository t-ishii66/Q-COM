# 01: 量子ビット（Qubit）

## 古典ビットとの対比

古典コンピュータの基本単位は **ビット（bit）** であり、0 または 1 のどちらか一方の値を取る。

量子コンピュータの基本単位は **量子ビット（qubit）** である。量子ビットは 0 と 1 の **重ね合わせ状態** を取ることができる。

## 量子ビットの状態

量子ビットの一般的な状態は次のように書ける：

$$
\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle
$$

ここで：
- $\vert 0\rangle$ と $\vert 1\rangle$ は **計算基底（computational basis）** と呼ばれる基本状態
- $\alpha, \beta$ は **複素数** の確率振幅（probability amplitude）
- **正規化条件** $\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1$ を満たす

### ディラック記法（ブラケット記法）

量子力学では **ディラック記法** を用いる：

- $\vert\ \rangle$：**ケット（ket）** — 列ベクトルに対応する
- $\langle\ \vert$：**ブラ（bra）** — 行ベクトル（ケットの随伴）に対応する

具体的にベクトルで書くと：

$$
\vert 0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad
\vert 1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

したがって一般の量子ビット状態は：

$$
\vert\psi\rangle = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
$$

## 測定（Measurement）

量子ビットを計算基底で **測定** すると：
- 確率 $\lvert\alpha\rvert^2$ で $\vert 0\rangle$ が得られる
- 確率 $\lvert\beta\rvert^2$ で $\vert 1\rangle$ が得られる

測定後、量子ビットの状態は測定結果に対応する基底状態に **射影（collapse）** される。これは不可逆な操作であり、測定前の重ね合わせ状態は失われる。

### 例

状態 $\vert\psi\rangle = \frac{1}{\sqrt{2}}\vert 0\rangle + \frac{1}{\sqrt{2}}\vert 1\rangle$ を測定すると：
- 確率 $\left\lvert\frac{1}{\sqrt{2}}\right\rvert^2 = \frac{1}{2}$ で $\vert 0\rangle$
- 確率 $\left\lvert\frac{1}{\sqrt{2}}\right\rvert^2 = \frac{1}{2}$ で $\vert 1\rangle$

が得られる。これは「公平なコイン投げ」に相当する。

## ブロッホ球（Bloch Sphere）

正規化条件と全体位相の自由度を考慮すると、1量子ビットの状態は2つの実数パラメータで記述できる：

$$
\vert\psi\rangle = \cos\frac{\theta}{2}\vert 0\rangle + e^{i\phi}\sin\frac{\theta}{2}\vert 1\rangle
$$

ここで $0 \le \theta \le \pi$、 $0 \le \phi \lt 2\pi$ である。

これは単位球面上の点と一対一に対応し、この球面を **ブロッホ球** と呼ぶ：
- 北極 ($\theta = 0$): $\vert 0\rangle$
- 南極 ($\theta = \pi$): $\vert 1\rangle$
- 赤道上 ($\theta = \pi/2$): $\vert 0\rangle$ と $\vert 1\rangle$ の等しい重ね合わせ

ブロッホ球は1量子ビットの状態を視覚的に理解するための強力なツールである。

## 複数量子ビット

$n$ 個の量子ビットの状態は $2^n$ 次元の複素ベクトル空間で記述される。

### 2量子ビットの場合

2量子ビットの計算基底は $\vert 00\rangle, \vert 01\rangle, \vert 10\rangle, \vert 11\rangle$ の4つであり、一般の状態は：

$$
\vert\psi\rangle = \alpha_{00}\vert 00\rangle + \alpha_{01}\vert 01\rangle + \alpha_{10}\vert 10\rangle + \alpha_{11}\vert 11\rangle
$$

正規化条件は $\lvert\alpha_{00}\rvert^2 + \lvert\alpha_{01}\rvert^2 + \lvert\alpha_{10}\rvert^2 + \lvert\alpha_{11}\rvert^2 = 1$ である。

### テンソル積

2つの独立な量子ビットの合成系は **テンソル積** $\otimes$ で表される。

#### 定義

$\vert\psi_1\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle$ と $\vert\psi_2\rangle = \gamma\vert 0\rangle + \delta\vert 1\rangle$ のテンソル積は：

$$
\vert\psi_1\rangle \otimes \vert\psi_2\rangle = \alpha\gamma\vert 00\rangle + \alpha\delta\vert 01\rangle + \beta\gamma\vert 10\rangle + \beta\delta\vert 11\rangle
$$

ここで $\vert 00\rangle$ は $\vert 0\rangle \otimes \vert 0\rangle$ の省略記法である。 $\vert\psi_1\rangle\vert\psi_2\rangle$ や $\vert\psi_1 \psi_2\rangle$ とも書く。

#### ベクトル表現

テンソル積はベクトルの **クロネッカー積** に対応する：

$$
\vert 0\rangle \otimes \vert 0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\ 0 \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

同様に：

$$
\vert 01\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \quad
\vert 10\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad
\vert 11\rangle = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

これらが $2^2 = 4$ 次元空間の計算基底を成す。

#### 具体例

$\vert\psi_1\rangle = \vert +\rangle = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}}$ と $\vert\psi_2\rangle = \vert 0\rangle$ のテンソル積：

$$
\vert +\rangle \otimes \vert 0\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) \otimes \vert 0\rangle = \frac{\vert 00\rangle + \vert 10\rangle}{\sqrt{2}}
$$

この状態を測定すると、 $\vert 00\rangle$ と $\vert 10\rangle$ がそれぞれ確率 $1/2$ で得られる。第2ビットは必ず 0 であり、2つのビットは **独立** に振る舞っている。

#### テンソル積の性質

- **双線形性：** $(\alpha\vert\psi\rangle) \otimes \vert\phi\rangle = \alpha(\vert\psi\rangle \otimes \vert\phi\rangle)$
- **分配法則：** $(\vert\psi_1\rangle + \vert\psi_2\rangle) \otimes \vert\phi\rangle = \vert\psi_1\rangle \otimes \vert\phi\rangle + \vert\psi_2\rangle \otimes \vert\phi\rangle$
- **非可換：** 一般に $\vert\psi\rangle \otimes \vert\phi\rangle \neq \vert\phi\rangle \otimes \vert\psi\rangle$（ビットの順序が意味を持つ）

### 量子もつれ（エンタングルメント）の導入

2量子ビットの状態には、テンソル積で書けるものと書けないものがある。

#### 積状態（テンソル積で書ける状態）

$$
\vert\psi\rangle = \frac{\vert 00\rangle + \vert 10\rangle}{\sqrt{2}} = \frac{\vert 0\rangle + \vert 1\rangle}{\sqrt{2}} \otimes \vert 0\rangle = \vert +\rangle\vert 0\rangle
$$

この状態では、第1ビットと第2ビットを独立に記述できる。一方を測定しても、もう一方の状態に影響しない。

#### エンタングル状態（テンソル積で書けない状態）

次の状態を考える：

$$
\vert\Phi^+\rangle = \frac{\vert 00\rangle + \vert 11\rangle}{\sqrt{2}}
$$

これを $(\alpha\vert 0\rangle + \beta\vert 1\rangle) \otimes (\gamma\vert 0\rangle + \delta\vert 1\rangle)$ の形に書こうとすると：

$$
\alpha\gamma = \frac{1}{\sqrt{2}}, \quad \alpha\delta = 0, \quad \beta\gamma = 0, \quad \beta\delta = \frac{1}{\sqrt{2}}
$$

$\alpha\delta = 0$ より $\alpha = 0$ または $\delta = 0$ だが、どちらの場合も $\alpha\gamma$ と $\beta\delta$ の両方を $\frac{1}{\sqrt{2}}$ にすることはできない。よってこの状態はテンソル積に分解できない。

このような状態を **エンタングル状態（量子もつれ状態）** と呼ぶ。

#### ベル状態

エンタングル状態の最も重要な例が **ベル状態**（Bell states）であり、「最大限にもつれた」2量子ビット状態である：

$$
\vert\Phi^+\rangle = \frac{\vert 00\rangle + \vert 11\rangle}{\sqrt{2}}, \quad \vert\Phi^-\rangle = \frac{\vert 00\rangle - \vert 11\rangle}{\sqrt{2}}
$$

$$
\vert\Psi^+\rangle = \frac{\vert 01\rangle + \vert 10\rangle}{\sqrt{2}}, \quad \vert\Psi^-\rangle = \frac{\vert 01\rangle - \vert 10\rangle}{\sqrt{2}}
$$

4つのベル状態は2量子ビット空間の正規直交基底を成す（**ベル基底**）。

#### 部分測定とエンタングルメントの効果

$\vert\Phi^+\rangle = \frac{\vert 00\rangle + \vert 11\rangle}{\sqrt{2}}$ の第1ビットを測定する：

- **$\vert 0\rangle$ が出た場合（確率 $1/2$）：** 全体の状態は $\vert 00\rangle$ に射影される。第2ビットは確実に $\vert 0\rangle$。
- **$\vert 1\rangle$ が出た場合（確率 $1/2$）：** 全体の状態は $\vert 11\rangle$ に射影される。第2ビットは確実に $\vert 1\rangle$。

つまり、第1ビットの測定結果が第2ビットの状態を **即座に決定する**。測定前は第2ビット単独の状態が定まっておらず、第1ビットの測定によって初めて確定する。これがエンタングルメントの本質的な特徴である。

積状態 $\vert +\rangle\vert 0\rangle = \frac{\vert 00\rangle + \vert 10\rangle}{\sqrt{2}}$ と比較すると違いが明確になる。この場合：

- **$\vert 0\rangle$ が出た場合（確率 $1/2$）：** 第2ビットは $\vert 0\rangle$。
- **$\vert 1\rangle$ が出た場合（確率 $1/2$）：** 第2ビットは $\vert 0\rangle$。

どちらの場合でも第2ビットは $\vert 0\rangle$ であり、第1ビットの測定結果に **依存しない**。

> エンタングルメントの物理的意味や応用（量子テレポーテーション、ベルの不等式など）は後のノートで詳しく扱う。

## まとめ

| 概念 | 古典ビット | 量子ビット |
|------|-----------|-----------|
| 取りうる値 | 0 または 1 | $\alpha\vert 0\rangle + \beta\vert 1\rangle$ |
| 情報量 | 1ビット | 測定で得られるのは1ビット |
| 状態空間 | $\{0, 1\}$（離散） | ブロッホ球（連続） |
| 複製 | 自由にコピー可能 | 不可能（量子複製不可能定理） |
