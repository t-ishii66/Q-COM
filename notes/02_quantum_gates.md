# 02: 量子ゲート（Quantum Gates）

## 量子ゲートとは

古典コンピュータではビットを操作する論理ゲート（AND, OR, NOT など）を用いる。量子コンピュータではこれに対応するものとして **量子ゲート** を用いる。

量子ゲートは量子ビットの状態ベクトルに作用する **ユニタリ行列** $U$ で表される：

$$
|\psi'\rangle = U|\psi\rangle
$$

### ユニタリ行列の条件

行列 $U$ がユニタリであるとは、次を満たすことである：

$$
U^\dagger U = U U^\dagger = I
$$

ここで $U^\dagger$ は $U$ の随伴行列（転置して複素共役を取ったもの）、$I$ は単位行列である。

この条件により：
- **状態ベクトルの正規化が保存される**（確率の合計が常に 1）
- **可逆性が保証される**（$U^{-1} = U^\dagger$ なので、逆操作が常に存在する）

古典の論理ゲート（例えば AND）は不可逆な場合があるが、量子ゲートは必ず可逆である。

---

## 1量子ビットゲート

### パウリゲート（Pauli Gates）

パウリゲートは最も基本的な量子ゲートであり、ブロッホ球上での回転に対応する。

#### パウリ X ゲート（NOT ゲート）

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

$|0\rangle$ と $|1\rangle$ を入れ替える。古典の NOT ゲートに相当する。

$$
X|0\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |1\rangle
$$

$$
X|1\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = |0\rangle
$$

**ブロッホ球上の解釈：** X 軸まわりの $\pi$ 回転。北極 $|0\rangle$ と南極 $|1\rangle$ が入れ替わる。

#### パウリ Y ゲート

$$
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
$$

$$
Y|0\rangle = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ i \end{pmatrix} = i|1\rangle
$$

$$
Y|1\rangle = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} -i \\ 0 \end{pmatrix} = -i|0\rangle
$$

**ブロッホ球上の解釈：** Y 軸まわりの $\pi$ 回転。

#### パウリ Z ゲート

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

$$
Z|0\rangle = |0\rangle, \quad Z|1\rangle = -|1\rangle
$$

$|0\rangle$ はそのまま、$|1\rangle$ の位相が反転する。ビットの値は変わらないが **位相** が変わる。

**具体例：** 重ね合わせ状態に Z を作用させる：

$$
Z\left(\frac{|0\rangle + |1\rangle}{\sqrt{2}}\right) = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

測定確率は変わらない（どちらも $1/2$）が、位相が変化している。この差は他のゲートとの組み合わせで観測可能な効果を生む。

**ブロッホ球上の解釈：** Z 軸まわりの $\pi$ 回転。赤道上の点が反対側に移る。

#### パウリ行列の性質

3つのパウリ行列は以下の重要な性質を持つ：

- **エルミート性：** $X^\dagger = X$, $Y^\dagger = Y$, $Z^\dagger = Z$（自分自身が逆行列）
- **自乗が恒等：** $X^2 = Y^2 = Z^2 = I$（2回作用させると元に戻る）
- **交換関係：** $XY = iZ$, $YZ = iX$, $ZX = iY$

---

### アダマールゲート（Hadamard Gate）

量子計算で最も頻繁に使われるゲートの一つ。重ね合わせ状態を作り出す。

$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

#### 計算基底への作用

$$
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \equiv |+\rangle
$$

$$
H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \equiv |-\rangle
$$

$|0\rangle$ から均等な重ね合わせ $|+\rangle$ が生まれ、$|1\rangle$ からは位相の異なる重ね合わせ $|-\rangle$ が生まれる。

$|+\rangle$ と $|-\rangle$ は **アダマール基底**（あるいは $\pm$ 基底）と呼ばれる。

#### 重ね合わせ基底への作用

$$
H|+\rangle = |0\rangle, \quad H|-\rangle = |1\rangle
$$

つまりアダマールゲートは **計算基底とアダマール基底の変換** を行う。2回適用すると元に戻る：

$$
H^2 = I
$$

#### 具体例：行列計算の確認

$$
H|0\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle
$$

**ブロッホ球上の解釈：** X 軸と Z 軸の中間の軸まわりの $\pi$ 回転。北極 $|0\rangle$ が赤道上の $|+\rangle$ に移る。

---

### 位相ゲート（Phase Gates）

$|1\rangle$ 成分に位相を付加するゲート群。$|0\rangle$ 成分は変化しない。

#### 一般の位相ゲート $R_\phi$

$$
R_\phi = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\phi} \end{pmatrix}
$$

$$
R_\phi(\alpha|0\rangle + \beta|1\rangle) = \alpha|0\rangle + \beta e^{i\phi}|1\rangle
$$

#### S ゲート（$\pi/2$ 位相ゲート）

$$
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
$$

$|1\rangle$ に位相 $i = e^{i\pi/2}$ を付ける。$S^2 = Z$ という関係がある。

#### T ゲート（$\pi/4$ 位相ゲート）

$$
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
$$

$T^2 = S$、$T^4 = Z$ という関係がある。

T ゲートは **フォールトトレラント量子計算** において特別な重要性を持つ。多くの誤り訂正符号において、T ゲートの実装が最もコストの高い操作となる。

#### 具体例：S ゲートの作用

$|+\rangle$ に S ゲートを作用させる：

$$
S|+\rangle = S \cdot \frac{|0\rangle + |1\rangle}{\sqrt{2}} = \frac{|0\rangle + i|1\rangle}{\sqrt{2}}
$$

ブロッホ球上では赤道上の点が $\pi/2$ だけ回転した状態に対応する。

---

### 回転ゲート（Rotation Gates）

ブロッホ球の各軸まわりの任意角度の回転を表す。

$$
R_x(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_y(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

#### 具体例：$|0\rangle$ と $|1\rangle$ への作用

$\theta = \pi/2$（90度回転）の場合を計算する。$\cos\frac{\pi}{4} = \sin\frac{\pi}{4} = \frac{1}{\sqrt{2}}$ を用いる。

**$R_x(\pi/2)$ の作用：**

$$
R_x\!\left(\frac{\pi}{2}\right) = \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{-i}{\sqrt{2}} \\ \frac{-i}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix}
$$

$$
R_x\!\left(\frac{\pi}{2}\right)|0\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{i}{\sqrt{2}}|1\rangle
$$

$$
R_x\!\left(\frac{\pi}{2}\right)|1\rangle = -\frac{i}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle
$$

$|0\rangle$（北極）から X 軸まわりに 90 度回転し、赤道上に移る。測定すると $|0\rangle$, $|1\rangle$ が等確率で得られる。

**$R_y(\pi/2)$ の作用：**

$$
R_y\!\left(\frac{\pi}{2}\right) = \begin{pmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix}
$$

$$
R_y\!\left(\frac{\pi}{2}\right)|0\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle = |+\rangle
$$

$$
R_y\!\left(\frac{\pi}{2}\right)|1\rangle = -\frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle
$$

$R_y(\pi/2)|0\rangle$ は $|+\rangle$ と一致する。$R_x$ との違いは、係数が実数のみであること（虚数位相 $i$ が現れない）。

**$R_z(\pi/2)$ の作用：**

$$
R_z\!\left(\frac{\pi}{2}\right) = \begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
$$

$$
R_z\!\left(\frac{\pi}{2}\right)|0\rangle = e^{-i\pi/4}|0\rangle
$$

$$
R_z\!\left(\frac{\pi}{2}\right)|1\rangle = e^{i\pi/4}|1\rangle
$$

$|0\rangle$ と $|1\rangle$ はどちらも全体位相が付くだけで、測定確率は変化しない。Z 軸上の点（北極・南極）は Z 軸まわりの回転で動かないためである。$R_z$ の効果は重ね合わせ状態に作用させたときに現れる。

#### パウリゲートとの関係

パウリゲートは回転ゲートの特殊ケース（全体位相を除く）：

$$
R_x(\pi) = -iX, \quad R_y(\pi) = -iY, \quad R_z(\pi) = -iZ
$$

---

## 2量子ビットゲート

### CNOT ゲート（Controlled-NOT）

量子計算で最も重要な2量子ビットゲート。**制御ビット（control）** と **標的ビット（target）** を持つ。

制御ビットが $|1\rangle$ のとき、標的ビットに X（NOT）を適用する。制御ビットが $|0\rangle$ のときは何もしない。

$$
\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

基底に対する記法は $|\text{制御},\text{標的}\rangle$ の順とする。

#### 計算基底への作用

| 入力 | 出力 | 説明 |
|------|------|------|
| $\vert 00\rangle$ | $\vert 00\rangle$ | 制御=0 → 何もしない |
| $\vert 01\rangle$ | $\vert 01\rangle$ | 制御=0 → 何もしない |
| $\vert 10\rangle$ | $\vert 11\rangle$ | 制御=1 → 標的を反転 |
| $\vert 11\rangle$ | $\vert 10\rangle$ | 制御=1 → 標的を反転 |

古典の XOR に相当する：標的ビットは「制御 XOR 標的」になる。

#### 具体例：エンタングルメントの生成

CNOT ゲートの最も重要な応用は、アダマールゲートと組み合わせた **ベル状態の生成** である。

初期状態 $|00\rangle$ から出発する：

**ステップ1：** 第1量子ビットにアダマールゲートを適用

$$
(H \otimes I)|00\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |0\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}}
$$

**ステップ2：** CNOT を適用（第1ビットが制御、第2ビットが標的）

$$
\text{CNOT} \cdot \frac{|00\rangle + |10\rangle}{\sqrt{2}} = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

結果の $\frac{|00\rangle + |11\rangle}{\sqrt{2}}$ は **ベル状態** $|\Phi^+\rangle$ と呼ばれる。この状態はテンソル積に分解できない、すなわちエンタングルした状態である。

> **テンソル積に分解できないことの確認：**
> $(\alpha|0\rangle + \beta|1\rangle) \otimes (\gamma|0\rangle + \delta|1\rangle) = \alpha\gamma|00\rangle + \alpha\delta|01\rangle + \beta\gamma|10\rangle + \beta\delta|11\rangle$
> とおくと、$|00\rangle$ の係数 $\alpha\gamma = 1/\sqrt{2}$、$|01\rangle$ の係数 $\alpha\delta = 0$、$|10\rangle$ の係数 $\beta\gamma = 0$、$|11\rangle$ の係数 $\beta\delta = 1/\sqrt{2}$ を同時に満たす $\alpha, \beta, \gamma, \delta$ は存在しない（$\alpha\delta = 0$ かつ $\beta\gamma = 0$ なら $\alpha\gamma\beta\delta = 0$ だが、$\alpha\gamma \cdot \beta\delta = 1/2 \neq 0$）。

---

### CZ ゲート（Controlled-Z）

制御ビットと標的ビットがともに $|1\rangle$ のとき、位相 $-1$ を付ける。

$$
\text{CZ} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}
$$

| 入力 | 出力 |
|------|------|
| $\vert 00\rangle$ | $\vert 00\rangle$ |
| $\vert 01\rangle$ | $\vert 01\rangle$ |
| $\vert 10\rangle$ | $\vert 10\rangle$ |
| $\vert 11\rangle$ | $-\vert 11\rangle$ |

CZ ゲートは対称性を持ち、制御と標的の区別がない。どちらのビットを制御としても結果は同じである。

#### CNOT との関係

CZ の標的ビットの前後にアダマールゲートを挟むと CNOT になる：

$$
\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

これは $HZH = X$ という関係に基づいている。

---

### SWAP ゲート

2つの量子ビットの状態を入れ替える。

$$
\text{SWAP} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

$$
\text{SWAP}|ab\rangle = |ba\rangle
$$

SWAP は3つの CNOT で実装できる：

$$
\text{SWAP} = \text{CNOT}_{12} \cdot \text{CNOT}_{21} \cdot \text{CNOT}_{12}
$$

ここで $\text{CNOT}_{ij}$ は第 $i$ ビットが制御、第 $j$ ビットが標的の CNOT を意味する。

---

## 3量子ビットゲート

### トフォリゲート（Toffoli Gate / CCNOT）

2つの制御ビットと1つの標的ビットを持つ。両方の制御ビットが $|1\rangle$ のときだけ、標的ビットに NOT を適用する。

| 入力 | 出力 |
|------|------|
| $\vert 110\rangle$ | $\vert 111\rangle$ |
| $\vert 111\rangle$ | $\vert 110\rangle$ |
| その他 | 変化なし |

トフォリゲートは **古典的に万能** である。すなわち、AND、OR、NOT などの古典論理ゲートをすべてトフォリゲートで構成できる。

#### 具体例：AND の実現

標的ビットの初期値を $|0\rangle$ にすると：

$$
\text{Toffoli}|ab0\rangle = |ab(a \cdot b)\rangle
$$

第3ビットに $a$ AND $b$ の結果が書き込まれる。

---

## ユニバーサルゲートセット

有限個のゲートの組み合わせで任意のユニタリ変換を（任意の精度で）近似できるとき、そのゲートの集合を **ユニバーサルゲートセット** と呼ぶ。

よく用いられるユニバーサルゲートセットの例：

- $\{H, T, \text{CNOT}\}$
- $\{H, S, T, \text{CNOT}\}$（冗長だが実用的）

任意の1量子ビットゲートは $H$ と $T$ の組み合わせで近似でき、CNOT を加えることで任意の多量子ビットゲートも近似できる。これは **ソロヴェイ・キタエフの定理** によって保証されている。

---

## ゲートの恒等式

量子回路の簡約化や理解に役立つ基本的な恒等式：

| 恒等式 | 説明 |
|--------|------|
| $HXH = Z$ | X と Z はアダマールで入れ替わる |
| $HZH = X$ | 上の逆 |
| $HYH = -Y$ | Y は符号が反転する |
| $H = \frac{X + Z}{\sqrt{2}}$ | H は X と Z の「中間」 |
| $S = T^2$ | S は T の2乗 |
| $Z = S^2 = T^4$ | Z は T の4乗 |
| $X = HZH$ | X は Z の基底変換 |

---

## まとめ

| ゲート | 量子ビット数 | 行列サイズ | 主な役割 |
|--------|------------|-----------|---------|
| X, Y, Z | 1 | $2 \times 2$ | 基本的な回転（パウリ演算） |
| H | 1 | $2 \times 2$ | 重ね合わせの生成・基底変換 |
| S, T | 1 | $2 \times 2$ | 位相操作 |
| $R_x, R_y, R_z$ | 1 | $2 \times 2$ | 任意角度の回転 |
| CNOT | 2 | $4 \times 4$ | 条件付き反転・エンタングルメント生成 |
| CZ | 2 | $4 \times 4$ | 条件付き位相反転 |
| SWAP | 2 | $4 \times 4$ | 状態の入れ替え |
| Toffoli | 3 | $8 \times 8$ | 古典計算の可逆実現 |

量子ゲートの本質は **ユニタリ変換** であり、確率の保存と可逆性が保証される。$\{H, T, \text{CNOT}\}$ のようなユニバーサルゲートセットがあれば、原理的に任意の量子計算を実行できる。
