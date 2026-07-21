---
title: "[Solution] Poetry Package Name Invalid -- Fix Illegal Package Name"
description: "Fix Poetry package name invalid errors when the package name in pyproject.toml contains illegal characters. Use valid PEP 508 names."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the package name in `pyproject.toml` does not conform to PEP 508 naming rules. The name contains invalid characters.

## Common Causes

- Package name contains uppercase letters
- Package name has spaces or special characters
- Package name starts with a hyphen or number
- Package name uses underscores (discouraged)

## How to Fix

### 1. Use a Valid Package Name

```toml
[tool.poetry]
name = "my-package"  # lowercase, hyphens only
```

### 2. Validate the Name

```bash
python -c "import re; assert re.match(r'^[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?$', 'my-package')"
```

### 3. Fix in pyproject.toml

```toml
[tool.poetry]
name = "my-package"  # Not "My_Package" or "my package"
```

### 4. Check PyPI Naming Rules

PyPI normalizes names but Poetry validates format strictly.

## Examples

```bash
$ poetry build
InvalidProjectName: "My Cool Package" is not a valid project name

# Fix:
[tool.poetry]
name = "my-cool-package"

$ poetry build
Building my-cool-package (1.0.0)
```
