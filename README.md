# MMDA Recitation Code Repository

> Code repository for the **Mathematical Modeling and Data Analysis (MMDA)** recitation sessions at Tsinghua University.

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) [![uv](https://img.shields.io/badge/package%20manager-uv-purple)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)](https://pre-commit.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

中文文档请见 [README_CN.md](README_CN.md)。

## Overview

This repository contains code and notebooks used in the MMDA recitation sessions, covering topics such as numerical linear algebra, scientific computing, and data analysis with Python.

## Repository Structure

```cmd
mmda/
├── notebook/
│   ├── pre_class_intro_to_jupyter.ipynb  # Pre-class: Introduction to Jupyter Notebook
│   └── recitation1.ipynb                 # Recitation 1: NumPy / SciPy & Linear Algebra
├── src/
│   ├── utils.py           # Utility functions (timing & memory analysis)
│   └── time_memory.py     # Time and memory benchmarking helpers
├── LICENSE                # MIT License
└── pyproject.toml         # Project configuration and dependencies
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

## Dependencies

| Package                       | Purpose                               |
| ----------------------------- | ------------------------------------- |
| `numpy`                       | Numerical computing                   |
| `scipy`                       | Scientific computing & linear algebra |
| `sympy`                       | Symbolic mathematics                  |
| `matplotlib` / `scienceplots` | Plotting                              |
| `plotly`                      | Interactive visualization             |
| `ipykernel` / `ipywidgets`    | Jupyter support                       |

## Code Quality

This project uses [pre-commit](https://pre-commit.com/) hooks to enforce code quality:

```bash
# Install hooks
uv run pre-commit install

# Run manually on all files
uv run pre-commit run --all-files
```

Hooks include: `ruff` (linting & formatting), `mypy` (type checking), `codespell` (spell checking), and standard file hygiene checks.

## Contact

顾燚 (Yi Gu) — [guy22@mails.tsinghua.edu.cn](mailto:guy22@mails.tsinghua.edu.cn)
