# MMDA 习题课代码仓库

> 清华大学**数学建模与数据分析（MMDA）**课程习题课代码仓库。

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/) [![uv](https://img.shields.io/badge/包管理器-uv-purple)](https://github.com/astral-sh/uv) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-已启用-brightgreen)](https://pre-commit.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

English documentation: [README.md](README.md)

## 简介

本仓库收录 MMDA 课程习题课所用的代码与 Notebook，涵盖数值线性代数、科学计算、数据分析等主题的 Python 实现。

## 目录结构

```cmd
mmda/
├── notebook/
│   ├── pre_class_intro_to_jupyter.ipynb  # 课前：Jupyter Notebook 快速入门
│   └── recitation1.ipynb                 # 习题课 1：NumPy / SciPy 与线性代数
├── src/
│   ├── utils.py           # 工具函数（计时与内存分析）
│   └── time_memory.py     # 时间与内存基准测试辅助函数
├── LICENSE                # MIT 许可证
└── pyproject.toml         # 项目配置与依赖
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

## 主要依赖

| 包                            | 用途               |
| ----------------------------- | ------------------ |
| `numpy`                       | 数值计算           |
| `scipy`                       | 科学计算与线性代数 |
| `sympy`                       | 符号数学           |
| `matplotlib` / `scienceplots` | 绘图               |
| `plotly`                      | 交互式可视化       |
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
