# 01: 量子ビット（Qubit）

## 古典ビットとの対比

古典コンピュータの基本単位は **ビット（bit）** であり、0 または 1 のどちらか一方の値を取る。

量子コンピュータの基本単位は **量子ビット（qubit）** である。量子ビットは 0 と 1 の **重ね合わせ状態** を取ることができる。

## 量子ビットの状態

量子ビットの一般的な状態は次のように書ける：

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle
$$

ここで：
- $|0\rangle$ と $|1\rangle$ は **計算基底（computational basis）** と呼ばれる基本状態
- $\alpha, \beta$ は **複素数** の確率振幅（probability amplitude）
- **正規化条件** $|\alpha|^2 + |\beta|^2 = 1$ を満たす

### ディラック記法（ブラケット記法）

量子力学では **ディラック記法** を用いる：

- $|\ \rangle$：**ケット（ket）** — 列ベクトルに対応する
- $\langle\ |$：**ブラ（bra）** — 行ベクトル（ケットの随伴）に対応する

具体的にベクトルで書くと：

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad
|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

したがって一般の量子ビット状態は：

$$
|\psi\rangle = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
$$

## 測定（Measurement）

量子ビットを計算基底で **測定** すると：
- 確率 $|\alpha|^2$ で $|0\rangle$ が得られる
- 確率 $|\beta|^2$ で $|1\rangle$ が得られる

測定後、量子ビットの状態は測定結果に対応する基底状態に **射影（collapse）** される。これは不可逆な操作であり、測定前の重ね合わせ状態は失われる。

### 例

状態 $|\psi\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$ を測定すると：
- 確率 $\left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}$ で $|0\rangle$
- 確率 $\left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}$ で $|1\rangle$

が得られる。これは「公平なコイン投げ」に相当する。

## ブロッホ球（Bloch Sphere）

正規化条件と全体位相の自由度を考慮すると、1量子ビットの状態は2つの実数パラメータで記述できる：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

ここで $0 \le \theta \le \pi$、$0 \le \phi < 2\pi$ である。

これは単位球面上の点と一対一に対応し、この球面を **ブロッホ球** と呼ぶ：
- 北極（$\theta = 0$）：$|0\rangle$
- 南極（$\theta = \pi$）：$|1\rangle$
- 赤道上（$\theta = \pi/2$）：$|0\rangle$ と $|1\rangle$ の等しい重ね合わせ

ブロッホ球は1量子ビットの状態を視覚的に理解するための強力なツールである。

## 複数量子ビット

$n$ 個の量子ビットの状態は $2^n$ 次元の複素ベクトル空間で記述される。

### 2量子ビットの場合

2量子ビットの計算基底は $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ の4つであり、一般の状態は：

$$
|\psi\rangle = \alpha_{00}|00\rangle + \alpha_{01}|01\rangle + \alpha_{10}|10\rangle + \alpha_{11}|11\rangle
$$

正規化条件は $|\alpha_{00}|^2 + |\alpha_{01}|^2 + |\alpha_{10}|^2 + |\alpha_{11}|^2 = 1$ である。

### テンソル積

2つの独立な量子ビットの合成系は **テンソル積** $\otimes$ で表される。

#### 定義

$|\psi_1\rangle = \alpha|0\rangle + \beta|1\rangle$ と $|\psi_2\rangle = \gamma|0\rangle + \delta|1\rangle$ のテンソル積は：

$$
|\psi_1\rangle \otimes |\psi_2\rangle = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle
$$

ここで $|00\rangle$ は $|0\rangle \otimes |0\rangle$ の省略記法である。$|\psi_1\rangle|\psi_2\rangle$ や $|\psi_1 \psi_2\rangle$ とも書く。

#### ベクトル表現

テンソル積はベクトルの **クロネッカー積** に対応する：

$$
|0\rangle \otimes |0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix} \\ 0 \cdot \begin{pmatrix} 1 \\ 0 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

同様に：

$$
|01\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \quad
|10\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad
|11\rangle = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

これらが $2^2 = 4$ 次元空間の計算基底を成す。

#### 具体例

$|\psi_1\rangle = |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$ と $|\psi_2\rangle = |0\rangle$ のテンソル積：

$$
|+\rangle \otimes |0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |0\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}}
$$

この状態を測定すると、$|00\rangle$ と $|10\rangle$ がそれぞれ確率 $1/2$ で得られる。第2ビットは必ず 0 であり、2つのビットは **独立** に振る舞っている。

#### テンソル積の性質

- **双線形性：** $(\alpha|\psi\rangle) \otimes |\phi\rangle = \alpha(|\psi\rangle \otimes |\phi\rangle)$
- **分配法則：** $(|\psi_1\rangle + |\psi_2\rangle) \otimes |\phi\rangle = |\psi_1\rangle \otimes |\phi\rangle + |\psi_2\rangle \otimes |\phi\rangle$
- **非可換：** 一般に $|\psi\rangle \otimes |\phi\rangle \neq |\phi\rangle \otimes |\psi\rangle$（ビットの順序が意味を持つ）

### 量子もつれ（エンタングルメント）の導入

2量子ビットの状態には、テンソル積で書けるものと書けないものがある。

#### 積状態（テンソル積で書ける状態）

$$
|\psi\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}} = \frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |0\rangle = |+\rangle|0\rangle
$$

この状態では、第1ビットと第2ビットを独立に記述できる。一方を測定しても、もう一方の状態に影響しない。

#### エンタングル状態（テンソル積で書けない状態）

次の状態を考える：

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

これを $(\alpha|0\rangle + \beta|1\rangle) \otimes (\gamma|0\rangle + \delta|1\rangle)$ の形に書こうとすると：

$$
\alpha\gamma = \frac{1}{\sqrt{2}}, \quad \alpha\delta = 0, \quad \beta\gamma = 0, \quad \beta\delta = \frac{1}{\sqrt{2}}
$$

$\alpha\delta = 0$ より $\alpha = 0$ または $\delta = 0$ だが、どちらの場合も $\alpha\gamma$ と $\beta\delta$ の両方を $\frac{1}{\sqrt{2}}$ にすることはできない。よってこの状態はテンソル積に分解できない。

このような状態を **エンタングル状態（量子もつれ状態）** と呼ぶ。

#### ベル状態

エンタングル状態の最も重要な例が **ベル状態**（Bell states）であり、「最大限にもつれた」2量子ビット状態である：

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}, \quad |\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}
$$

$$
|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}, \quad |\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}
$$

4つのベル状態は2量子ビット空間の正規直交基底を成す（**ベル基底**）。

#### 部分測定とエンタングルメントの効果

$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$ の第1ビットを測定する：

- **$|0\rangle$ が出た場合（確率 $1/2$）：** 全体の状態は $|00\rangle$ に射影される。第2ビットは確実に $|0\rangle$。
- **$|1\rangle$ が出た場合（確率 $1/2$）：** 全体の状態は $|11\rangle$ に射影される。第2ビットは確実に $|1\rangle$。

つまり、第1ビットの測定結果が第2ビットの状態を **即座に決定する**。測定前は第2ビット単独の状態が定まっておらず、第1ビットの測定によって初めて確定する。これがエンタングルメントの本質的な特徴である。

積状態 $|+\rangle|0\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}}$ と比較すると違いが明確になる。この場合：

- **$|0\rangle$ が出た場合（確率 $1/2$）：** 第2ビットは $|0\rangle$。
- **$|1\rangle$ が出た場合（確率 $1/2$）：** 第2ビットは $|0\rangle$。

どちらの場合でも第2ビットは $|0\rangle$ であり、第1ビットの測定結果に **依存しない**。

> エンタングルメントの物理的意味や応用（量子テレポーテーション、ベルの不等式など）は後のノートで詳しく扱う。

## まとめ

| 概念 | 古典ビット | 量子ビット |
|------|-----------|-----------|
| 取りうる値 | 0 または 1 | $\alpha\|0\rangle + \beta\|1\rangle$ |
| 情報量 | 1ビット | 測定で得られるのは1ビット |
| 状態空間 | $\{0, 1\}$（離散） | ブロッホ球（連続） |
| 複製 | 自由にコピー可能 | 不可能（量子複製不可能定理） |
