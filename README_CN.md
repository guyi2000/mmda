# MMDA 习题课代码仓库

> 清华大学**数学建模与数据分析（MMDA）**课程习题课代码仓库。

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) [![uv](https://img.shields.io/badge/包管理器-uv-purple)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-已启用-brightgreen)](https://pre-commit.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

English documentation: [README.md](README.md)

## 简介

本仓库收录 MMDA 课程习题课所用的代码与 Notebook，涵盖数值线性代数、科学计算、数据分析等主题的 Python 实现。

- `pre_class.ipynb`：课前内容与热身练习。
- `recitation1.ipynb` 至 `recitation4.ipynb`：习题课递进式 Notebook。
- `src/lec2_cl1.py`：对稠密/稀疏矩阵构造与求解进行性能对比的脚本。

## 目录结构

```cmd
mmda/
├── notebook/
│   ├── pre_class.ipynb   # 课前内容与预备练习
│   ├── recitation1.ipynb # 习题课 1：NumPy / SciPy 与线性代数
│   ├── recitation2.ipynb # 习题课 2 Notebook
│   ├── recitation3.ipynb # 习题课 3 Notebook
│   └── recitation4.ipynb # 习题课 4 Notebook
├── res/
│   └── ...               # Notebook/脚本使用的静态资源
├── src/
│   ├── lec2_cl1.py        # 课堂/习题实验脚本
│   ├── utils.py           # 工具函数（计时与内存分析）
│   └── __init__.py
├── out/                   # 脚本生成的图表/PDF 输出
├── tmp.ipynb              # 临时实验 Notebook
├── LICENSE                # MIT 许可证
├── pyproject.toml         # 项目配置与依赖
└── uv.lock                # 依赖锁定文件（uv）
```

## 快速开始

### 环境要求

- Python 3.12
- [uv](https://github.com/astral-sh/uv)（推荐的包管理器）

### 安装

```bash
# 克隆仓库
git clone https://github.com/guyi2000/mmda.git
cd mmda

# 使用 uv 安装依赖
uv sync
```

### 运行 Notebook

在 VS Code 或 JupyterLab 中打开任意 `.ipynb` 文件，选择由 `uv` 创建的 `.venv` 内核即可运行。

### 运行脚本

```bash
# 运行实验脚本
uv run python src/lec2_cl1.py
```

脚本会将对比图保存到 `out/` 目录。

## 主要依赖

| 包                            | 用途               |
| ----------------------------- | ------------------ |
| `numpy`                       | 数值计算           |
| `scipy`                       | 科学计算与线性代数 |
| `sympy`                       | 符号数学           |
| `pandas`                      | 数据处理           |
| `matplotlib` / `scienceplots` | 绘图               |
| `plotly`                      | 交互式可视化       |
| `threadpoolctl`               | 基准测试线程控制   |
| `ipykernel` / `ipywidgets`    | Jupyter 支持       |

## 代码规范

本项目使用 [pre-commit](https://pre-commit.com/) 钩子保证代码质量：

```bash
# 安装钩子
uv run pre-commit install

# 手动对所有文件运行检查
uv run pre-commit run --all-files
```

包含的钩子：`ruff`（代码检查与格式化）、`mypy`（类型检查）、`codespell`（拼写检查）以及文件基础规范检查。

## 联系方式

顾燚（Yi Gu）— [guy22@mails.tsinghua.edu.cn](mailto:guy22@mails.tsinghua.edu.cn)
