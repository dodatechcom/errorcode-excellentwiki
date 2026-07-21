---
title: "[Solution] pip Download Only Binary -- Fix No Binary Available"
description: "Fix pip download --only-binary errors when no pre-built wheel exists for your platform. Build from source or find alternatives."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip could not find a pre-built binary wheel for your platform and Python version.

## Common Causes

- The package only ships source distributions
- Your Python version is too new or too old
- Your platform (e.g., ARM) is not supported with wheels
- The package maintainer did not upload wheels

## How to Fix

### 1. Allow Source Builds

```bash
pip install <package>  # without --only-binary flag
```

### 2. Install Build Tools

```bash
sudo apt install build-essential python3-dev
```

### 3. Use a Different Python Version

```bash
pyenv install 3.11.7
pyenv shell 3.11.7
pip install <package>
```

### 4. Check Available Wheels

```bash
pip index versions <package>
```

## Examples

```bash
$ pip install --only-binary=:all: lxml
ERROR: No matching distribution found for lxml

$ pip install lxml
Building wheel for lxml (setup.py) ... done
```
