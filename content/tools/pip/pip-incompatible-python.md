---
title: "[Solution] pip Incompatible Python Version — Fix Module Requires Python >= 3.x"
description: "Fix pip incompatible Python version errors when a package requires a newer Python. Upgrade Python, use versioned installs, or find compatible alternatives."
tools: ["pip"]
error-types: ["python-error"]
severities: ["warning"]
weight: 5
---

This error means a package explicitly declares a minimum Python version requirement that your current Python does not meet. pip refuses to install an incompatible version.

## What This Error Means

Modern packages specify `python_requires` in their metadata. When your Python version is below the minimum:

```
ERROR: Package 'example' requires a different Python: 3.9.2 not in '>=3.10'
```

Or with pip's resolver:

```
ERROR: pip's dependency resolver found that Python version >3.10 is required
```

## Why It Happens

- Your system Python is too old for the latest version of a package
- The virtual environment was created with an older Python than what the package needs
- A dependency transitively requires a newer Python than your environment provides
- The package dropped support for your Python version in a recent release
- You are running an end-of-life Python version (2.7, 3.5, 3.6, 3.7)

## How to Fix It

### Check Your Python Version

```bash
python --version
python3 --version
```

### Install an Older Compatible Package Version

```bash
pip install "<package><3.0"  # compatible with your Python
```

### Upgrade Python on Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev
python3.11 -m venv venv
source venv/bin/activate
```

### Upgrade Python on macOS

```bash
brew install python@3.11
/opt/homebrew/bin/python3.11 -m venv venv
source venv/bin/activate
```

### Install the Package with --python-version Flag

When downloading from a platform with multiple Python variants:

```bash
pip install --python-version 3.9 <package>
```

### Pin to an Older Compatible Release

```bash
pip install "<package><2.0"
```

Or specify the exact version that supports your Python:

```bash
pip install <package>==1.2.3
```

## Common Mistakes

- Not checking the package's PyPI page for supported Python versions
- Assuming the latest version always supports your Python
- Using system Python instead of a version-managed environment (pyenv)
- Not pinning package versions in requirements.txt for legacy Python deployments

## Related Pages

- [pip Virtualenv Error]({{< relref "/tools/pip/pip-virtualenv-error" >}}) -- virtualenv issues
- [pip Dependency Conflict]({{< relref "/tools/pip/pip-dependency-conflict" >}}) -- dependency conflicts
- [pip Version Error]({{< relref "/tools/pip/pip-version-error" >}}) -- pip version issues
