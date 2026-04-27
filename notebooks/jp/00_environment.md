# 環境構築

## 前提

- Linux（Ubuntu 等）または macOS
- Python 3.10 以上
- `uv`（Python パッケージマネージャ）

`uv` が未導入の場合：

```bash
# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS (Homebrew)
brew install uv
```

## 手順

### 1. 仮想環境の作成

プロジェクトルートで：

```bash
uv venv
```

`uv` が利用可能な Python を自動検出し、`.venv/` を作成する。

### 2. パッケージのインストール

```bash
source .venv/bin/activate
uv pip install qiskit jupyter qiskit-aer matplotlib pylatexenc
```

| パッケージ | 用途 |
|-----------|------|
| `qiskit` | 量子回路の構築・シミュレーション（コア） |
| `qiskit-aer` | 高性能シミュレータバックエンド |
| `jupyter` | Notebook 環境 |
| `matplotlib` | 回路図・ヒストグラムの描画 |
| `pylatexenc` | 回路図中の LaTeX レンダリング |

### 3. 動作確認

```bash
python3 -c "import qiskit; print(qiskit.__version__)"
python3 -c "import qiskit_aer; print(qiskit_aer.__version__)"
```

### 4. Jupyter Notebook の起動

```bash
source .venv/bin/activate
jupyter notebook
```

`notebooks/` ディレクトリ内の `.ipynb` ファイルを開いて実行する。セルの実行は `Shift + Enter`（1セルずつ）または上部メニューの `Cell → Run All`（全セル一括）。

## 備考

- `.venv/` は `.gitignore` に追加すること
- `uv pip freeze > requirements.txt` でパッケージ一覧をエクスポートできる
