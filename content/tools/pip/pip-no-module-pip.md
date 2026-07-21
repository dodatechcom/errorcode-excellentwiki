---
title: "[Solution] pip No Module pip -- Fix pip Not Found as Module"
description: "Fix pip no module pip errors when python -m pip fails because pip is not installed. Bootstrap pip installation."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `python -m pip` fails because pip is not installed in the current Python environment.

## Common Causes

- Python was installed without pip
- pip was removed from the environment
- Using a minimal Docker image without pip
- Virtual environment was created without pip

## How to Fix

### 1. Bootstrap pip with ensurepip

```bash
python -m ensurepip --upgrade
```

### 2. Download get-pip.py

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### 3. Install pip via Package Manager

```bash
sudo apt install python3-pip
```

### 4. Recreate Virtual Environment with pip

```bash
python -m venv --clear .venv
source .venv/bin/activate
```

## Examples

```bash
$ python -m pip install requests
python: No module named pip

$ python -m ensurepip --upgrade
$ python -m pip install requests
Successfully installed requests-2.31.0
```
