---
title: "[Solution] Poetry Publish TestPyPI -- Fix TestPyPI Upload Errors"
description: "Fix Poetry publish TestPyPI errors when uploading to TestPyPI fails. Configure the test repository and handle version conflicts."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry failed to upload your package to TestPyPI. This is often caused by version conflicts or authentication issues.

## Common Causes

- The package version already exists on TestPyPI
- TestPyPI token is invalid or missing
- The repository URL is incorrect
- TestPyPI is experiencing downtime

## How to Fix

### 1. Configure TestPyPI Repository

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

### 2. Set TestPyPI Token

```bash
poetry config pypi-token.testpypi pypi-AgEI...
```

### 3. Publish to TestPyPI

```bash
poetry publish --build --repository testpypi
```

### 4. Use a Different Version for Testing

```toml
[tool.poetry]
version = "1.0.0rc1"
```

## Examples

```bash
$ poetry publish --build --repository testpypi
HTTPError: 400 Bad Request: Version 1.0.0 already exists

# Increment version:
$ poetry version 1.0.1rc1
$ poetry publish --build --repository testpypi
```
