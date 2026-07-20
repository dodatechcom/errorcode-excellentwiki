---
title: "[Solution] Python ImportError: No module named 'notebook' — Fix"
description: "Fix Python ImportError: No module named 'notebook'. Install notebook with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 307
---

# Python ImportError: No module named 'notebook'

The `ModuleNotFoundError: No module named 'notebook'` error occurs when Python cannot locate the notebook package, which provides the Jupyter Notebook server and web application.

## Common Causes

```python
# Cause 1: notebook not installed
# Running: jupyter notebook
# ModuleNotFoundError: No module named 'notebook'

# Cause 2: Installed for wrong Python version or virtual environment
import notebook  # ModuleNotFoundError

# Cause 3: Upgraded from notebook v6 to v7 and extensions broken
# nbclassic requires separate installation
```

```python
# Cause 4: notebook server cannot find its own modules
# pip install jupyter does not always install notebook

# Cause 5: JupyterLab requires notebook as dependency
# from notebook.auth import passwd — ModuleNotFoundError in v7+
```

## How to Fix

### Fix 1: Install notebook with pip

```bash
pip install notebook

# For legacy notebook v6 compatibility
pip install "notebook<7"

# Verify installation
jupyter notebook --version
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install notebook
python -c "import notebook; print(notebook.__version__)"
```

### Fix 3: Install JupyterLab instead (recommended)

```bash
pip install jupyterlab
jupyter lab
```

## Examples

```bash
# Start notebook server
jupyter notebook

# Start with specific port
jupyter notebook --port=8889

# Generate config file
jupyter notebook --generate-config

# Run headless (no browser)
jupyter notebook --no-browser --ip=0.0.0.0
```

```python
# Using notebook API programmatically
from notebook.notebookapp import NotebookApp

# Check if server is running
app = NotebookApp.instance()
print(app.port)
```

## Related Errors

- {{< relref "importerror-jupyter" >}} — ImportError: jupyter
- {{< relref "importerror-ipython" >}} — ImportError: IPython
- {{< relref "importerror-ipykernel" >}} — ImportError: ipykernel
