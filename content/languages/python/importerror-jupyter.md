---
title: "[Solution] Python ImportError: No module named 'jupyter' — Fix"
description: "Fix Python ImportError: No module named 'jupyter'. Install jupyter with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 306
---

# Python ImportError: No module named 'jupyter'

The `ModuleNotFoundError: No module named 'jupyter'` error occurs when Python cannot locate the Jupyter package, which provides interactive computing notebooks and related tools.

## Common Causes

```python
# Cause 1: jupyter not installed
# Running: jupyter notebook
# ModuleNotFoundError: No module named 'jupyter'

# Cause 2: Installed for wrong Python version or virtual environment
import jupyter  # ModuleNotFoundError

# Cause 3: Only jupyter-client installed, not full jupyter
# pip install jupyter-client does not install jupyter core
```

```python
# Cause 4: Jupyter kernel cannot find Python
# KernelSpecNotFoundError or missing ipykernel

# Cause 5: conda environment not activated
# jupyter installed in conda but shell uses system Python
```

## How to Fix

### Fix 1: Install Jupyter with pip

```bash
pip install jupyter

# Lightweight install (notebook server only)
pip install jupyter notebook

# WithLab extension
pip install jupyterlab
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install jupyter
jupyter --version
```

### Fix 3: Register IPython kernel for Jupyter

```bash
pip install ipykernel
python -m ipykernel install --user --name myenv
```

## Examples

```bash
# Start Jupyter Notebook
jupyter notebook

# Start JupyterLab
jupyter lab

# List installed kernels
jupyter kernelspec list

# Install a kernel for current environment
python -m ipykernel install --user --name python3 --display-name "Python 3"
```

```python
# Using jupyter_client programmatically
from jupyter_client import KernelManager

km = KernelManager(kernel_name="python3")
km.start_kernel()
kc = km.client()
kc.start_channels()
```

## Related Errors

- {{< relref "importerror-ipython" >}} — ImportError: IPython
- {{< relref "importerror-notebook" >}} — ImportError: notebook
- {{< relref "importerror-ipykernel" >}} — ImportError: ipykernel
