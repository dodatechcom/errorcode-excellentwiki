---
title: "[Solution] pip Install Conflict -- Fix Dependency Version Conflict"
description: "Fix pip install conflict errors when two packages require incompatible versions of a shared dependency. Resolve the conflict chain."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip cannot install both requested packages because they depend on incompatible versions of a shared dependency.

## Common Causes

- Package A requires lib>=2.0 while package B requires lib<2.0
- Version constraints are too tight
- A newly released package tightened its requirements

## How to Fix

### 1. Use pip-check to Identify

```bash
pip check
```

### 2. Install Compatible Versions

```bash
pip install "package-a>=1.0,<2.0" "package-b>=2.0,<3.0"
```

### 3. Use Resolver Debug Output

```bash
pip install --verbose <package-a> <package-b> 2>&1 | grep -i conflict
```

### 4. Create Separate Environments

```bash
python -m venv .venv-a
source .venv-a/bin/activate
pip install package-a

python -m venv .venv-b
source .venv-b/bin/activate
pip install package-b
```

## Examples

```bash
$ pip install package-a package-b
ERROR: package-a requires lib>=2.0, but package-b requires lib<2.0

$ pip install "package-a>=1.0" "lib>=2.0,<3.0"
```
