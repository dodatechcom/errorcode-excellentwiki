---
title: "[Solution] Python ImportError: No module named 'IPython' — Fix"
description: "Fix Python ImportError: No module named 'IPython'. Install ipython with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 305
---

# Python ImportError: No module named 'IPython'

The `ModuleNotFoundError: No module named 'IPython'` error occurs when Python cannot locate the IPython package, which provides an enhanced interactive Python shell with features like tab completion and syntax highlighting.

## Common Causes

```python
# Cause 1: IPython not installed
# Running: ipython
# ModuleNotFoundError: No module named 'IPython'

# Cause 2: Installed for wrong Python version or virtual environment
import IPython  # ModuleNotFoundError

# Cause 3: Jupyter depends on IPython but it is missing
# from IPython.display import display — ModuleNotFoundError
```

```python
# Cause 4: IPython kernel not installed for Jupyter
# jupyter kernelspec list shows no Python kernel

# Cause 5: Broken IPython installation
# partial upgrade left IPython in inconsistent state
```

## How to Fix

### Fix 1: Install IPython with pip

```bash
pip install ipython

# With all optional features
pip install ipython[all]

# Verify installation
ipython --version
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install ipython
python -c "import IPython; print(IPython.__version__)"
```

### Fix 3: Reinstall to fix broken installation

```bash
pip install --force-reinstall ipython
```

## Examples

```bash
# Launch enhanced Python shell
ipython

# Run with profile
ipython --profile=myprofile

# Launch with autoimport
ipython --AutoFormatter.maximum_line_length=120
```

```python
# Using IPython display in scripts
from IPython.display import display, HTML

display(HTML("<h1>Hello World</h1>"))

# Embed IPython in a script
from IPython.terminal.interactiveshell import TerminalInteractiveShell
shell = TerminalInteractiveShell.instance()
shell.mainloop()
```

## Related Errors

- {{< relref "importerror-jupyter" >}} — ImportError: jupyter
- {{< relref "importerror-notebook" >}} — ImportError: notebook
- {{< relref "importerror-prompt-toolkit" >}} — ImportError: prompt_toolkit
