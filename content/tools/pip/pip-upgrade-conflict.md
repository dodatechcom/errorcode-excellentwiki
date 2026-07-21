---
title: "[Solution] pip Upgrade Conflict -- Fix Package Upgrade Dependency Conflict"
description: "Fix pip upgrade conflict errors when upgrading a package creates dependency conflicts. Resolve version constraints carefully."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip cannot upgrade a package because the new version conflicts with other installed packages.

## Common Causes

- Another package requires a specific version of the dependency
- The new version dropped support for a feature you need
- Multiple packages have conflicting version ranges

## How to Fix

### 1. Upgrade Everything Together

```bash
pip install --upgrade <package> <dependent-packages>
```

### 2. Use pip-check to Find Conflicts

```bash
pip check
```

### 3. Force Upgrade with --no-deps

```bash
pip install --upgrade --no-deps <package>
```

### 4. Create a Fresh Virtual Environment

```bash
python -m venv .venv-new
source .venv-new/bin/activate
pip install <package>
```

## Examples

```bash
$ pip install --upgrade requests
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed.

$ pip check
requests 2.31.0 requires charset-normalizer,<4,>=2 but you have charset-normalizer 1.0.0

$ pip install --upgrade charset-normalizer requests
```
