---
title: "[Solution] Poetry PyPI Upload Failed Error — How to Fix"
description: "Fix Poetry PyPI upload failures when poetry publish fails to upload packages. Resolve authentication, build, and repository configuration errors."
tools: ["poetry"]
error-types: ["deploy-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means Poetry failed to upload your package to PyPI (or another package repository). The upload may fail due to authentication issues, build artifacts missing, package metadata errors, or repository configuration problems.

## Why It Happens

- PyPI credentials are not configured or the API token has expired
- The package was not built before publishing (`poetry build` was not run)
- The package name or version already exists on PyPI (duplicate upload)
- The package metadata (description, license, classifiers) contains invalid characters
- The repository URL is misconfigured in `pyproject.toml`
- The package exceeds PyPI's size limits
- Two-factor authentication is required but not configured

## Common Error Messages

```
HTTPError

403 Forbidden: The credentials provided are invalid.
```

```
HTTPError

400 Bad Request: The version '1.0.0' already exists for package 'my-package'.
```

```
UploadError

Failed to upload package to PyPI.
```

```
RepositoryError

Invalid repository URL: https://upload.pypi.org/legacy/
```

## How to Fix It

### 1. Configure PyPI Credentials

```bash
# Using a PyPI API token (recommended)
poetry config pypi-token.pypi pypi-AgEI...your-token...

# Using username and password (legacy)
poetry config repositories.pypi https://upload.pypi.org/legacy/
poetry config http-basic.pypi username password
```

### 2. Build Before Publishing

```bash
poetry build
poetry publish
```

Or combine both:

```bash
poetry build && poetry publish
```

### 3. Check for Existing Version

```bash
pip index versions your-package-name
```

If the version already exists, bump the version:

```bash
poetry version patch  # 1.0.0 -> 1.0.1
poetry version minor  # 1.0.0 -> 1.1.0
poetry version major  # 1.0.0 -> 2.0.0
```

Then build and publish:

```bash
poetry build && poetry publish
```

### 4. Publish to TestPyPI First

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi pypi-AgEI...your-test-token...
poetry publish --repository testpypi
```

### 5. Fix Package Metadata

```bash
poetry check
```

Ensure `pyproject.toml` has all required fields:

```toml
[tool.poetry]
name = "my-package"
version = "1.0.0"
description = "A short description"
authors = ["Your Name <you@example.com>"]
license = "MIT"
readme = "README.md"
```

### 6. Handle Two-Factor Authentication

PyPI requires 2FA for all accounts. Use an API token instead of password:

```bash
# Generate a token at https://pypi.org/manage/account/token/
poetry config pypi-token.pypi pypi-AgEI...your-token...
poetry publish
```

### 7. Publish to a Private Repository

```toml
# pyproject.toml
[[tool.poetry.source]]
name = "private-pypi"
url = "https://pypi.company.com/simple/"
priority = "supplemental"
```

```bash
poetry publish --repository private-pypi
```

## Common Scenarios

**Upload fails with 403 Forbidden.** Your API token may have expired or lacks upload permissions. Generate a new token at pypi.org.

**Version already exists on PyPI.** PyPI does not allow re-uploading the same version. Bump the version number and publish a new release.

**Build succeeds but publish fails.** Check the built artifact:

```bash
ls dist/
# Should contain: my-package-1.0.0.tar.gz and my_package-1.0.0-py3-none-any.whl
```

If the files are missing, check `pyproject.toml` for correct `name` and `version`.

## Prevent It

1. Always run `poetry check` before `poetry build` to catch metadata issues early
2. Use API tokens instead of passwords for PyPI authentication — tokens can be revoked without changing your password
3. Test uploads to TestPyPI before publishing to production PyPI to catch issues early
