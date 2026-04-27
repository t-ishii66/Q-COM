# Environment Setup

## Prerequisites

- Linux (Ubuntu, etc.) or macOS
- Python 3.10 or later
- `uv` (Python package manager)

If `uv` is not installed:

```bash
# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS (Homebrew)
brew install uv
```

## Procedure

### 1. Creating the Virtual Environment

In the project root:

```bash
uv venv
```

`uv` automatically detects the available Python and creates `.venv/`.

### 2. Installing Packages

```bash
source .venv/bin/activate
uv pip install qiskit jupyter qiskit-aer matplotlib pylatexenc
```

| Package | Purpose |
|-----------|------|
| `qiskit` | Quantum circuit construction and simulation (core) |
| `qiskit-aer` | High-performance simulator backend |
| `jupyter` | Notebook environment |
| `matplotlib` | Drawing circuit diagrams and histograms |
| `pylatexenc` | LaTeX rendering in circuit diagrams |

### 3. Verifying Installation

```bash
python3 -c "import qiskit; print(qiskit.__version__)"
python3 -c "import qiskit_aer; print(qiskit_aer.__version__)"
```

### 4. Launching Jupyter Notebook

```bash
source .venv/bin/activate
jupyter notebook
```

Open and run `.ipynb` files in the `notebooks/` directory. Run cells with `Shift + Enter` (one at a time) or via `Cell → Run All` in the top menu (all cells at once).

## Notes

- Add `.venv/` to `.gitignore`
- `uv pip freeze > requirements.txt` exports the list of packages
