# MMDA Recitation Code Repository

> Code repository for the **Mathematical Modeling and Data Analysis (MMDA)** recitation sessions at Tsinghua University.

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) [![uv](https://img.shields.io/badge/package%20manager-uv-purple)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)](https://pre-commit.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

中文文档请见 [README_CN.md](README_CN.md)。

## Overview

This repository contains code and notebooks used in the MMDA recitation sessions, covering topics such as numerical linear algebra, scientific computing, finite-volume methods, and finite-element methods with Python.

- `pre_class.ipynb`: pre-class notes and warm-up tasks.
- `recitation1.ipynb` to `recitation6.ipynb`: recitation notebooks for progressive practice.
- `notebook/recitation5.ipynb`: finite-difference continuation and finite-volume prerequisites, including sparse Kronecker-form Poisson solvers.
- `notebook/recitation6.ipynb`: Burgers equation (Godunov/FV), 1D FEM (hat + bubble basis), and heat diffusion on both structured and unstructured meshes.
- `src/lec2_cl1.py`: benchmark script comparing dense/sparse matrix construction and solving.
- `src/generate_mesh.py`: generate the THU-shaped unstructured mesh (`out/thu_mesh.msh`) using Gmsh.

## Repository Structure

```cmd
mmda/
├── notebook/
│   ├── pre_class.ipynb   # Pre-class notes and warm-up
│   ├── recitation1.ipynb # Recitation 1: NumPy / SciPy & Linear Algebra
│   ├── recitation2.ipynb # Recitation 2 notebook
│   ├── recitation3.ipynb # Recitation 3 notebook
│   ├── recitation4.ipynb # Recitation 4 notebook
│   ├── recitation5.ipynb # Recitation 5: FD continuation & FV prerequisites
│   └── recitation6.ipynb # Recitation 6: FV continuation + FEM + heat diffusion
├── res/
│   └── ...               # Static resources used by notebooks/scripts
├── src/
│   ├── generate_mesh.py   # Gmsh mesh generation for THU geometry
│   ├── lec2_cl1.py        # Lecture/recitation experiment script
│   ├── utils.py           # Utility functions (timing & memory analysis)
│   └── __init__.py
├── out/                   # Generated figures/animations/meshes from notebooks & scripts
├── tmp.ipynb              # Temporary notebook for quick experiments
├── LICENSE                # MIT License
├── pyproject.toml         # Project configuration and dependencies
└── uv.lock                # Locked dependency versions (uv)
```

## Getting Started

### Prerequisites

- Python 3.12
- [uv](https://github.com/astral-sh/uv) (recommended package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/guyi2000/mmda.git
cd mmda

# Install dependencies with uv
uv sync
```

### Running Notebooks

Open any `.ipynb` file in VS Code or JupyterLab and select the `.venv` kernel created by `uv`.

### Running Scripts

```bash
# Run the experiment script
uv run python src/lec2_cl1.py

# Generate unstructured mesh used by recitation6
uv run python src/generate_mesh.py
```

Generated outputs are saved to the `out/` directory, including figures, GIF animations, and mesh files.

Typical outputs from `recitation6.ipynb` include:

- `out/heat_diffusion.gif`
- `out/THU_FEM.gif`
- `out/thu_mesh.msh`

### Recitation 6 Workflow

For a clean run of `recitation6.ipynb`, use the following order:

1. Generate the unstructured mesh:

```bash
uv run python src/generate_mesh.py
```

2. Open `notebook/recitation6.ipynb` and run cells from top to bottom.

3. Check generated files under `out/`:

- `thu_mesh.msh`
- `heat_diffusion.gif`
- `THU_FEM.gif`

## Dependencies

| Package                       | Purpose                               |
| ----------------------------- | ------------------------------------- |
| `numpy`                       | Numerical computing                   |
| `scipy`                       | Scientific computing & linear algebra |
| `sympy`                       | Symbolic mathematics                  |
| `pandas`                      | Data handling                         |
| `matplotlib` / `scienceplots` | Plotting                              |
| `plotly`                      | Interactive visualization             |
| `gmsh`                        | Unstructured mesh generation          |
| `scikit-fem`                  | FEM assembly and solving              |
| `threadpoolctl`               | Thread control for benchmarks         |
| `ipykernel` / `ipywidgets`    | Jupyter support                       |

## Code Quality

This project uses [pre-commit](https://pre-commit.com/) hooks to enforce code quality:

```bash
# Install hooks
uv run pre-commit install

# Run manually on all files
uv run pre-commit run --all-files
```

Hooks include: `uv-lock`, `ruff` (linting & formatting), `mypy` (type checking), `codespell` (spell checking), `toml-sort`, and standard file hygiene checks.

## Contact

顾燚 (Yi Gu) — [guy22@mails.tsinghua.edu.cn](mailto:guy22@mails.tsinghua.edu.cn)
