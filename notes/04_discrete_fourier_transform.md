# 03: 離散フーリエ変換（Discrete Fourier Transform）

## なぜフーリエ変換を学ぶのか

量子コンピュータの重要なアルゴリズムの多くは **量子フーリエ変換（QFT）** を基盤としている。Shor の素因数分解アルゴリズム、位相推定アルゴリズムなどがその代表例である。

量子フーリエ変換は、古典的な **離散フーリエ変換（DFT）** を量子回路で実現したものである。したがって、QFT を理解するにはまず DFT を正確に理解する必要がある。

本ノートでは DFT の定義から具体的な計算例まで、省略なく丁寧に記述する。

---

## フーリエ変換とは

フーリエ変換とは、ある信号を **周波数成分に分解する** 操作である。

日常的な例で言えば、音楽の波形（時間ごとの振幅の変化）をフーリエ変換すると、「どの周波数の音がどれだけ含まれているか」がわかる。

### 連続フーリエ変換

連続的な関数 $f(t)$ に対するフーリエ変換は、積分で定義される：

$$
\hat{f}(\xi) = \int_{-\infty}^{\infty} f(t) \, e^{-2\pi i \xi t} \, dt
$$

入力は連続関数 $f(t)$、出力も連続関数 $\hat{f}(\xi)$ である。$\xi$ は周波数を表し、 $\hat{f}(\xi)$ は「周波数 $\xi$ の成分がどれだけ含まれるか」を与える。核となる仕組みは $e^{-2\pi i \xi t}$（周波数 $\xi$ の複素正弦波）との内積を取ることである。

### 連続から離散へ

実際のデータは有限個の値として与えられる。連続フーリエ変換を有限・離散の設定に置き換えたものが **離散フーリエ変換（DFT）** である：

| | 連続フーリエ変換 | 離散フーリエ変換 |
|--|--|--|
| 入力 | 連続関数 $f(t)$ | $N$ 個の数値 $x_0, x_1, \ldots, x_{N-1}$ |
| 出力 | 連続関数 $\hat{f}(\xi)$ | $N$ 個の数値 $X_0, X_1, \ldots, X_{N-1}$ |
| 演算 | 積分 $\int$ | 有限和 $\sum$ |
| 周波数 | 連続値 $\xi$ | 離散値 $k = 0, 1, \ldots, N-1$ |
| 核 | $e^{-2\pi i \xi t}$ | $\omega_N^{jk} = e^{2\pi i jk/N}$ |

本質的な発想 ── 「複素指数関数との内積で周波数成分を取り出す」── は同じであり、連続を離散に、積分を有限和に置き換えただけである。

量子計算で扱うのは $N = 2^n$ 個の確率振幅（有限個の複素数）なので、離散フーリエ変換で十分である。以降は DFT に絞って議論する。

---

## 1 の N 乗根

DFT の定義に入る前に、重要な数学的道具である **1 の N 乗根** を整理する。

### 定義

$\omega_N$ を次のように定義する：

$$
\omega_N = e^{2\pi i / N}
$$

これは複素平面上の単位円を $N$ 等分する点のうち、反時計回りに最初に現れる点である。

$\omega_N$ の $k$ 乗 $\omega_N^k = e^{2\pi i k / N}$ は、単位円上の $N$ 等分点を順に与える。

### 具体例

**$N = 4$ の場合：**

$$
\omega_4 = e^{2\pi i / 4} = e^{i\pi/2} = i
$$

4つの4乗根は：

$$
\omega_4^0 = 1, \quad \omega_4^1 = i, \quad \omega_4^2 = -1, \quad \omega_4^3 = -i
$$

複素平面上で、これらは単位円を4等分する点（実軸正方向から反時計回りに $1, i, -1, -i$）である。

**$N = 2$ の場合：**

$$
\omega_2 = e^{2\pi i / 2} = e^{i\pi} = -1
$$

2つの2乗根は：

$$
\omega_2^0 = 1, \quad \omega_2^1 = -1
$$

### 重要な性質

1 の N 乗根は以下の性質を持つ。これらは DFT の理論で繰り返し使われる。

#### 周期性

$$
\omega_N^{k+N} = \omega_N^k
$$

これは $e^{2\pi i (k+N)/N} = e^{2\pi i k/N} \cdot e^{2\pi i} = e^{2\pi i k/N} \cdot 1$ から従う。指数の肩が $N$ だけ増えても値は変わらない。

#### 直交関係（最重要）

$$
\frac{1}{N} \sum_{j=0}^{N-1} \omega_N^{j(k - k')} = \frac{1}{N} \sum_{j=0}^{N-1} e^{2\pi i \, j(k - k') / N} = \delta_{k,k'}
$$

ここで $\delta_{k,k'}$ はクロネッカーのデルタであり、 $k \equiv k' \pmod{N}$ のとき 1、それ以外のとき 0 である。中辺は $\omega_N = e^{2\pi i/N}$ の定義を代入したものである。

直感的には、$k \neq k'$ のとき $\omega_N^{j(k-k')}$ は単位円を等間隔に $N$ 等分した点を順にたどる。これらの点は円周上に対称に配置されているので、複素数として足し合わせるとちょうど打ち消し合って 0 になる。

**証明：**

$k = k'$ の場合、 $\omega_N^{j \cdot 0} = 1$ なので和は $N$ となり、 $1/N$ を掛けて 1 になる。

$k \neq k'$ の場合、 $m = k - k' \not\equiv 0 \pmod{N}$ とおくと：
しつｒ
$$
\sum_{j=0}^{N-1} \omega_N^{jm} = \sum_{j=0}^{N-1} (\omega_N^m)^j
$$

これは初項 1、公比 $\omega_N^m$ の等比級数なので：

$$
\sum_{j=0}^{N-1} (\omega_N^m)^j = \frac{1 - (\omega_N^m)^N}{1 - \omega_N^m} = \frac{1 - \omega_N^{mN}}{1 - \omega_N^m} = \frac{1 - (e^{2\pi i})^m}{1 - \omega_N^m} = \frac{1 - 1}{1 - \omega_N^m} = 0
$$

分母 $1 - \omega_N^m \neq 0$ は $m \not\equiv 0 \pmod{N}$ から保証される。

この直交関係は、フーリエ変換が **可逆** であること（逆変換が存在すること）の根拠となる。

---

## 離散フーリエ変換の定義

### 順変換

$N$ 個の複素数の列 $x_0, x_1, \ldots, x_{N-1}$ が与えられたとき、その **離散フーリエ変換** $X_0, X_1, \ldots, X_{N-1}$ を次で定義する：

$$
X_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j \, \omega_N^{jk} \qquad (k = 0, 1, \ldots, N-1)
$$

ここで $\omega_N = e^{2\pi i / N}$ である。

各 $X_k$ は、入力列 $x_j$ の「周波数 $k$ の成分」に対応する。

> **正規化の注意：** DFT の定義には流派がある。工学では $1/N$ を順変換に、物理では $1/\sqrt{N}$ を両方に付けることが多い。本ノートでは量子計算の慣習に合わせ、順変換・逆変換の両方に $1/\sqrt{N}$ を付ける **対称的な正規化** を採用する。

### 逆変換

逆離散フーリエ変換は次で与えられる：

$$
x_j = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} X_k \, \omega_N^{-jk} \qquad (j = 0, 1, \ldots, N-1)
$$

順変換との違いは $\omega_N^{jk}$ が $\omega_N^{-jk}$ に変わっただけである（指数の符号が反転）。

### 逆変換が正しいことの確認

逆変換の式に順変換の定義を代入して、元の $x_j$ が復元されることを確かめる。

$$
\frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} X_k \, \omega_N^{-jk} = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} \left( \frac{1}{\sqrt{N}} \sum_{j'=0}^{N-1} x_{j'} \, \omega_N^{j'k} \right) \omega_N^{-jk}
$$

和の順序を交換する：

$$
= \frac{1}{N} \sum_{j'=0}^{N-1} x_{j'} \sum_{k=0}^{N-1} \omega_N^{k(j'-j)}
$$

ここで内側の和に直交関係を適用すると：

$$
\frac{1}{N} \sum_{k=0}^{N-1} \omega_N^{k(j'-j)} = \delta_{j',j}
$$

（ここでは $k$ について和を取っているが、直交関係は和を取る添字が何であっても成り立つ。）

よって：

$$
= \sum_{j'=0}^{N-1} x_{j'} \, \delta_{j',j} = x_j
$$

確かに元の列が復元される。

---

## 行列表現

DFT はベクトルに行列を掛ける操作として表現できる。

### DFT 行列

$N$ 次の **DFT 行列** $F_N$ を次のように定義する：

$$
(F_N)_{kj} = \frac{1}{\sqrt{N}} \omega_N^{jk}
$$

すなわち、行列の $(k, j)$ 成分（$k$ 行 $j$ 列、0-indexed）が $\frac{1}{\sqrt{N}} \omega_N^{jk}$ である。

DFT は次のように書ける：

$$
\begin{pmatrix} X_0 \\ X_1 \\ \vdots \\ X_{N-1} \end{pmatrix} = F_N \begin{pmatrix} x_0 \\ x_1 \\ \vdots \\ x_{N-1} \end{pmatrix}
$$

### ユニタリ性

DFT 行列はユニタリ行列である：

$$
F_N^\dagger F_N = F_N F_N^\dagger = I
$$

**証明：**

$(F_N^\dagger F_N)_{k,k'}$ を計算する。$F_N^\dagger$ の $(k,j)$ 成分は $F_N$ の $(j,k)$ 成分の複素共役である。$F_N$ の $(j,k)$ 成分は $\frac{1}{\sqrt{N}} \omega_N^{jk}$ なので、その複素共役は：

$$
\left(\frac{1}{\sqrt{N}} \omega_N^{jk}\right)^* = \frac{1}{\sqrt{N}} (\omega_N^{jk})^* = \frac{1}{\sqrt{N}} \omega_N^{-jk}
$$

となる。ここで $(\omega_N^{jk})^* = \omega_N^{-jk}$ は、 $e^{i\theta}$ の複素共役が $e^{-i\theta}$ であること（指数の符号が反転する）から従う。

これを使って積を計算すると：

$$
(F_N^\dagger F_N)_{k,k'} = \sum_{j=0}^{N-1} \frac{1}{\sqrt{N}} \omega_N^{-jk} \cdot \frac{1}{\sqrt{N}} \omega_N^{jk'} = \frac{1}{N} \sum_{j=0}^{N-1} \omega_N^{j(k'-k)} = \delta_{k,k'}
$$

最後の等号で直交関係を用いた。これは単位行列の $(k, k')$ 成分に一致するので $F_N^\dagger F_N = I$ が示された。

ユニタリ性は2つの重要な意味を持つ：

1. **可逆性：** $F_N^{-1} = F_N^\dagger$ なので逆変換が常に存在する
2. **ノルムの保存：** $\lVert F_N \mathbf{x} \rVert = \lVert \mathbf{x} \rVert$（パーセバルの定理）

量子ゲートもユニタリ行列であった（ノート02参照）。DFT 行列がユニタリであることは、DFT を量子ゲートとして実装できることの前提条件である。

---

## 具体例：$N = 2$ の DFT

### DFT 行列

DFT 行列の定義 $(F_N)_{kj} = \frac{1}{\sqrt{N}} \omega_N^{jk} = \frac{1}{\sqrt{N}} \left(e^{2\pi i / N}\right)^{jk}$ を $N \times N$ の行列として明示的に書くと：

$$
F_N = \frac{1}{\sqrt{N}} \begin{pmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & \omega_N & \omega_N^2 & \cdots & \omega_N^{N-1} \\ 1 & \omega_N^2 & \omega_N^4 & \cdots & \omega_N^{2(N-1)} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & \omega_N^{N-1} & \omega_N^{2(N-1)} & \cdots & \omega_N^{(N-1)^2} \end{pmatrix}
$$

$N = 2$ の場合、$\omega_2 = e^{2\pi i / 2} = -1$ なので：

$$
F_2 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & \omega_2 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

これはアダマールゲート $H$ の行列表現と完全に一致する（ノート02参照）。つまり **1量子ビットに対する量子フーリエ変換はアダマールゲートそのもの** である。

### 計算例

入力 $\mathbf{x} = (1, 0)^T$（1量子ビットの $\vert 0\rangle$ に対応）に DFT を適用する：

$$
\mathbf{X} = F_2 \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

定義に沿って各成分を確認する。$\mathbf{x} = (1, 0)^T$ なので $x_0 = 1,\; x_1 = 0$ である：

$$
X_0 = \frac{1}{\sqrt{2}} (x_0 \cdot \omega_2^{0 \cdot 0} + x_1 \cdot \omega_2^{1 \cdot 0}) = \frac{1}{\sqrt{2}} (1 \cdot 1 + 0 \cdot 1) = \frac{1}{\sqrt{2}}
$$

$$
X_1 = \frac{1}{\sqrt{2}} (x_0 \cdot \omega_2^{0 \cdot 1} + x_1 \cdot \omega_2^{1 \cdot 1}) = \frac{1}{\sqrt{2}} (1 \cdot 1 + 0 \cdot (-1)) = \frac{1}{\sqrt{2}}
$$

行列の計算と一致している。

もう一つ、入力 $\mathbf{x} = (1, 1)^T / \sqrt{2}$（$\vert +\rangle$ に対応）に DFT を適用する：

$$
F_2 \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 2 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$$

$\vert +\rangle$ にアダマールゲートを適用すると $\vert 0\rangle$ に戻る、という事実と一致する。

---

## 具体例：$N = 4$ の DFT

### DFT 行列

$\omega_4 = e^{2\pi i / 4} = i$ なので、 $\omega_4$ のべき乗は：

$$
\omega_4^0 = \left(e^{2\pi i / 4}\right)^0 = 1, \quad \omega_4^1 = \left(e^{2\pi i / 4}\right)^1 = i, \quad \omega_4^2 = \left(e^{2\pi i / 4}\right)^2 = -1, \quad \omega_4^3 = \left(e^{2\pi i / 4}\right)^3 = -i
$$

DFT 行列の $(k, j)$ 成分は $\frac{1}{\sqrt{4}} \omega_4^{jk} = \frac{1}{2} i^{jk}$ なので：

$$
F_4 = \frac{1}{2} \begin{pmatrix} i^{0 \cdot 0} & i^{1 \cdot 0} & i^{2 \cdot 0} & i^{3 \cdot 0} \\ i^{0 \cdot 1} & i^{1 \cdot 1} & i^{2 \cdot 1} & i^{3 \cdot 1} \\ i^{0 \cdot 2} & i^{1 \cdot 2} & i^{2 \cdot 2} & i^{3 \cdot 2} \\ i^{0 \cdot 3} & i^{1 \cdot 3} & i^{2 \cdot 3} & i^{3 \cdot 3} \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{pmatrix}
$$

各成分の計算を明示する（$i^n$ の値は 4 周期で $1, i, -1, -i$ を繰り返す）：

$$
\begin{array}{|c|c|c|}
\hline
jk & jk \mod 4 & i^{jk} \\
\hline
0 & 0 & 1 \\
1 & 1 & i \\
2 & 2 & -1 \\
3 & 3 & -i \\
4 & 0 & 1 \\
6 & 2 & -1 \\
9 & 1 & i \\
\hline
\end{array}
$$

### 計算例 1：一様分布

入力 $\mathbf{x} = \frac{1}{2}(1, 1, 1, 1)^T$（すべての成分が等しい）に DFT を適用する：

$$
F_4 \cdot \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i \end{pmatrix} \cdot \frac{1}{2} \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
$$

各成分を計算する：

$$
X_0 = \frac{1}{4}(1 + 1 + 1 + 1) = 1
$$

$$
X_1 = \frac{1}{4}(1 + i + (-1) + (-i)) = \frac{1}{4}(1 - 1 + i - i) = 0
$$

$$
X_2 = \frac{1}{4}(1 + (-1) + 1 + (-1)) = 0
$$

$$
X_3 = \frac{1}{4}(1 + (-i) + (-1) + i) = 0
$$

結果は $(1, 0, 0, 0)^T$ である。

**解釈：** 入力が一様（すべて同じ値）であるとき、周波数 0 の成分（DC 成分、定数成分）のみが残り、他の周波数成分はすべて 0 になる。一様な信号には「振動」がないので、これは直感に合う。

### 計算例 2：交互のパターン

入力 $\mathbf{x} = \frac{1}{2}(1, -1, 1, -1)^T$（符号が交互に入れ替わる）に DFT を適用する：

$$
X_0 = \frac{1}{4}(1 + (-1) + 1 + (-1)) = 0
$$

$$
X_1 = \frac{1}{4}(1 + (-1) \cdot i + 1 \cdot (-1) + (-1) \cdot (-i)) = \frac{1}{4}(1 - i - 1 + i) = 0
$$

$$
X_2 = \frac{1}{4}(1 + (-1)(-1) + 1 \cdot 1 + (-1)(-1)) = \frac{1}{4}(1 + 1 + 1 + 1) = 1
$$

$$
X_3 = \frac{1}{4}(1 + (-1)(-i) + 1 \cdot (-1) + (-1) \cdot i) = \frac{1}{4}(1 + i - 1 - i) = 0
$$

結果は $(0, 0, 1, 0)^T$ である。

**解釈：** 「$+1, -1, +1, -1$」という交互パターンは、$k = 2$ の成分のみが非零という結果を与えた。$N = 4$ の DFT では、$k = 0, 1, 2, 3$ の4つの周波数成分があるが、$k > N/2$ の成分（ここでは $k = 3$）は負の周波数として解釈される。具体的には $\omega_4^3 = \omega_4^{-1}$ であり、$k = 3$ は $k = 1$ の振動を逆方向に回したものに対応する。したがって独立な正の周波数は $k = 0, 1, 2$ であり、$k = 2 = N/2$ が最高周波数である。この入力は2サンプルごとに1周期の振動、すなわち最高周波数成分のみからなる信号である。

### 計算例 3：単一成分

入力 $\mathbf{x} = (1, 0, 0, 0)^T$（第0成分のみ）に DFT を適用する：

$$
X_k = \frac{1}{2} \sum_{j=0}^{3} x_j \, \omega_4^{jk} = \frac{1}{2} \cdot 1 \cdot \omega_4^{0 \cdot k} = \frac{1}{2}
$$

すべての $k$ で $X_k = 1/2$ である。結果は $\frac{1}{2}(1, 1, 1, 1)^T$ である。

**解釈：** 連続フーリエ変換では、関数 $f(t)$ を周波数成分に分解する。DFT はその離散版であり、$N$ 個の標本点 $j = 0, 1, \dots, N-1$ 上で定義された数列 $x_0, x_1, \dots, x_{N-1}$ を「関数」の代わりに扱う。

入力 $(1, 0, 0, 0)^T$ は、$j = 0$ だけが非零で他がすべてゼロの数列であり、連続の場合のデルタ関数 $\delta(t)$ の離散版にあたる。デルタ関数は1点に集中した「鋭いパルス」だが、このようなパルスを周波数成分の重ね合わせで作るには、すべての周波数を等しい振幅で足し合わせる必要がある。ある周波数が欠けたり偏ったりすれば、パルスは崩れて広がってしまう。だからこそ、1点集中の入力を DFT すると、すべての周波数成分が一様になる。

一方、計算例 1 では逆に、すべての成分が等しい入力 $\frac{1}{2}(1,1,1,1)^T$ が $k = 0$ の周波数成分だけに集中する結果を与えた。成分が一様な数列は振動を含まない「一定値」であり、変化がないので周波数ゼロ（$k = 0$）の成分しか持たない。

このように、入力と出力の役割がちょうど入れ替わっており、DFT の対称性を反映している。

---

## DFT の性質

### 線形性

DFT は線形変換である。入力 $\mathbf{x}$ と $\mathbf{y}$ に対して：

$$
\text{DFT}(\alpha \mathbf{x} + \beta \mathbf{y}) = \alpha \, \text{DFT}(\mathbf{x}) + \beta \, \text{DFT}(\mathbf{y})
$$

これは DFT が行列の積で表されることから自明である。

### パーセバルの定理（ノルム保存）

$$
\sum_{k=0}^{N-1} \lvert X_k \rvert^2 = \sum_{j=0}^{N-1} \lvert x_j \rvert^2
$$

DFT の前後でベクトルのノルム（各成分の絶対値の2乗の和）が保存される。これは DFT 行列のユニタリ性の直接的な帰結である。

量子力学では $\lvert x_j \rvert^2$ は測定確率に対応するので、パーセバルの定理は「確率の総和が保存される」ことを意味する。

### 周期性

$$
X_{k+N} = X_k
$$

これは $\omega_N^{j(k+N)} = \omega_N^{jk} \cdot \omega_N^{jN} = \omega_N^{jk} \cdot 1 = \omega_N^{jk}$ から従う。DFT の出力は周期 $N$ で繰り返す。

### シフト定理

入力を巡回的にシフトすると、DFT の各成分に位相因子が掛かる。

入力列を $m$ だけシフトした $y_j = x_{(j-m) \bmod N}$ の DFT は：

$$
Y_k = \omega_N^{-mk} X_k
$$

各周波数成分の絶対値は変わらず、位相だけが変化する。

---

## 古典コンピュータ上での計算量

$N$ 個のデータに対する DFT を定義どおりに計算すると：

- 各 $X_k$ の計算に $N$ 回の乗算と $N-1$ 回の加算が必要
- $k = 0, 1, \ldots, N-1$ の $N$ 個の出力があるので、合計 $O(N^2)$ の演算

**高速フーリエ変換（FFT）** アルゴリズムを用いると $O(N \log N)$ に削減できる。FFT は現代のデジタル信号処理を支える中核技術である。

量子フーリエ変換はさらに効率的で、$n$ 量子ビット（$N = 2^n$）に対して $O(n^2) = O((\log N)^2)$ 個のゲートで実装できる。ただし、結果の読み出しには測定が必要であり、1回の測定で得られるのは1つの基底状態だけである。この点で古典 FFT と量子フーリエ変換の「速さ」は単純比較できない。

---

## DFT と量子状態の対応

$N = 2^n$ のとき、$N$ 個の複素数の列 $(x_0, x_1, \ldots, x_{N-1})$ は $n$ 量子ビットの状態ベクトルとみなせる：

$$
\vert\psi\rangle = \sum_{j=0}^{N-1} x_j \vert j\rangle
$$

ここで $\vert j\rangle$ は $j$ の2進数表現に対応する計算基底である（例：$N = 4 = 2^2$ なので量子ビットは $n = 2$ 個であり、$\vert 0\rangle = \vert 00\rangle$, $\vert 1\rangle = \vert 01\rangle$, $\vert 2\rangle = \vert 10\rangle$, $\vert 3\rangle = \vert 11\rangle$）。

DFT を適用した結果は：

$$
\vert\tilde{\psi}\rangle = \sum_{k=0}^{N-1} X_k \vert k\rangle = F_N \vert\psi\rangle
$$

つまり、量子状態に DFT 行列を作用させることが **量子フーリエ変換** である。DFT 行列がユニタリであることから、これは正当な量子ゲート操作である。

### $N = 4$（2量子ビット）の場合の対応表

| 計算基底 | $j$（10進） | DFT 後の状態 |
|---------|------------|------------|
| $\vert 00\rangle = (1,0,0,0)^T$ | 0 | $\frac{1}{2}(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle)$ |
| $\vert 01\rangle = (0,1,0,0)^T$ | 1 | $\frac{1}{2}(\vert 00\rangle + i\vert 01\rangle - \vert 10\rangle - i\vert 11\rangle)$ |
| $\vert 10\rangle = (0,0,1,0)^T$ | 2 | $\frac{1}{2}(\vert 00\rangle - \vert 01\rangle + \vert 10\rangle - \vert 11\rangle)$ |
| $\vert 11\rangle = (0,0,0,1)^T$ | 3 | $\frac{1}{2}(\vert 00\rangle - i\vert 01\rangle - \vert 10\rangle + i\vert 11\rangle)$ |

この表は $F_4$ 行列の各列を読んだものである。量子フーリエ変換がどのように基底状態を変換するかを示している。

---

## まとめ

| 概念 | 内容 |
|------|------|
| DFT の本質 | データ列を周波数成分に分解する線形変換 |
| 核心となる数 | $\omega_N = e^{2\pi i/N}$（1 の N 乗根） |
| 行列表現 | $(F_N)_{kj} = \frac{1}{\sqrt{N}} \omega_N^{jk}$ |
| ユニタリ性 | $F_N^\dagger F_N = I$（直交関係から導かれる） |
| ノルム保存 | パーセバルの定理（確率の保存に対応） |
| $N=2$ との関係 | $F_2$ はアダマールゲート $H$ に一致する |
| 計算量 | 古典 DFT: $O(N^2)$, FFT: $O(N \log N)$, QFT: $O((\log N)^2)$ |
| 量子計算との接続 | DFT 行列がユニタリなので量子ゲートとして実装可能 |
