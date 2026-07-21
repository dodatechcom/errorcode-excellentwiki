---
title: "[Solution] Poetry Publish Unauthorized -- Fix PyPI Authentication Failure"
description: "Fix Poetry publish unauthorized errors when Poetry cannot authenticate with PyPI to upload your package. Configure credentials and tokens correctly."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry received a 401 Unauthorized response when trying to publish your package to PyPI. The upload is rejected due to invalid credentials.

## Common Causes

- The PyPI token is expired or invalid
- You are publishing to a private registry without credentials
- The `poetry.toml` has stale auth configuration
- You are using the wrong token (test vs production)

## How to Fix

### 1. Generate a New PyPI Token

Visit https://pypi.org/manage/account/token/ and create a new token.

### 2. Configure Poetry with the Token

```bash
poetry config pypi-token.pypi pypi-AgEI...
```

### 3. Use the Publish Command with Token

```bash
poetry publish --build --username __token__ --password pypi-AgEI...
```

### 4. Set Up Keyring

```bash
poetry config keyring-backend python.keyring.backends.fail.Keyring
```

## Examples

```bash
$ poetry publish --build
HTTPError: 403 Forbidden from https://upload.pypi.org/legacy/
The credentials you provided are not valid.

$ poetry config pypi-token.pypi pypi-AgEI...newtoken...
$ poetry publish --build
Uploading myproject-1.0.0-py3-none-any.whl (12.3 kB)
```
