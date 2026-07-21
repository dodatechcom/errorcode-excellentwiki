---
title: "[Solution] pip Requirements Not Editable -- Fix Editable Flag in Requirements"
description: "Fix pip requirements not editable errors when -r requirements.txt contains -e entries that fail. Handle editable installs separately."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means a `requirements.txt` file contains `-e .` or `-e git+...` entries that failed to install in editable mode.

## Common Causes

- The requirements.txt was generated with editable entries
- The project does not support editable installs
- Git dependencies with editable flag are broken

## How to Fix

### 1. Remove -e Flag from Requirements

```bash
sed -i '/^-e /d' requirements.txt
pip install -r requirements.txt
```

### 2. Install Non-Editable First

```bash
grep -v '^-e ' requirements.txt > requirements-fixed.txt
pip install -r requirements-fixed.txt
```

### 3. Install Editable Packages Separately

```bash
grep '^-e ' requirements.txt | sed 's/^-e //' | xargs -I{} pip install {}
```

### 4. Generate Requirements Without Editable

```bash
pip freeze --exclude-editable > requirements.txt
```

## Examples

```bash
$ pip install -r requirements.txt
ERROR: editable mode is not supported for this project

$ pip freeze --exclude-editable > requirements.txt
$ pip install -r requirements.txt
```
