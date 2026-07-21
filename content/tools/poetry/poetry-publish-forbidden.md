---
title: "[Solution] Poetry Publish Forbidden -- Fix Package Name Taken on PyPI"
description: "Fix Poetry publish forbidden errors when PyPI rejects your upload because the package name is already taken or you lack permissions."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means PyPI returned a 403 Forbidden when uploading your package. The name is taken or you do not have permission to publish under that name.

## Common Causes

- Another user already published a package with the same name
- You are using a PyPI token for a different account
- The package name was recently claimed by someone else
- You lack maintainer access to the existing package

## How to Fix

### 1. Choose a Different Package Name

```toml
[tool.poetry]
name = "mycompany-mypackage"
```

### 2. Claim the Name on PyPI

If the package is abandoned, file a PEP 541 request.

### 3. Verify Your Token

```bash
poetry config pypi-token.pypi
```

### 4. Test on TestPyPI First

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish --build --repository testpypi
```

## Examples

```bash
$ poetry publish --build
HTTPError: 403 Forbidden: The name 'mypackage' is already in use

# Use a qualified name:
$ sed -i 's/name = "mypackage"/name = "mycompany-mypackage"/' pyproject.toml
$ poetry publish --build
Uploading mycompany_mypackage-1.0.0-py3-none-any.whl
```
