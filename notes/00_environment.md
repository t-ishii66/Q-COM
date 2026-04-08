# 環境構築メモ

## 前提

- macOS (Apple Silicon)
- Homebrew 導入済み
- `uv` 導入済み（`brew install uv`）
- Python 3.10 が `/opt/homebrew/bin/python3.10` にある

## 手順

### 1. 仮想環境の作成

プロジェクトルートで:

```bash
uv venv
```

`uv` が利用可能な Python を自動検出し、`.venv/` を作成する。
今回は Python 3.10.18 が選択された。

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
# → 2.3.1

python3 -c "import qiskit_aer; print(qiskit_aer.__version__)"
# → 0.17.2
```

### 4. Jupyter Notebook の起動

```bash
source .venv/bin/activate
jupyter notebook
```

ブラウザが開き、Notebook 一覧が表示される。

## バージョン情報（2026-04-08 時点）

- Python: 3.10.18
- uv: 0.9.26
- qiskit: 2.3.1
- qiskit-aer: 0.17.2
- matplotlib: 3.10.8
- numpy: 2.2.6
- scipy: 1.15.3

## 備考

- `.venv/` は `.gitignore` に追加すること
- `uv pip freeze > requirements.txt` でパッケージ一覧をエクスポートできる
- `uv` は pip より大幅に高速（今回は全パッケージ数秒でインストール完了）
