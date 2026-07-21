---
title: "[Solution] Poetry Lock Hash Mismatch -- Fix Package Integrity Check"
description: "Fix Poetry lock hash mismatch errors when downloaded package hashes do not match those recorded in poetry.lock. Regenerate the lock file."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the SHA256 hash of a downloaded package does not match the hash stored in `poetry.lock`. Poetry treats this as a security concern and refuses to install.

## Common Causes

- The lock file was generated with a different version of the package
- PyPI returned a corrupted file
- A package was re-released with the same version number
- The lock file was edited manually

## How to Fix

### 1. Regenerate the Lock File

```bash
poetry lock --no-update
```

### 2. Update the Specific Package

```bash
poetry update requests
```

### 3. Clear Cache and Regenerate

```bash
poetry cache clear --all pypi
poetry lock
```

### 4. Force Install Without Hash Check

Not recommended for production, but useful for debugging:

```bash
poetry install --no-root
```

## Examples

```bash
$ poetry install
HashMismatchError: Hash mismatch for download requests-2.31.0-py3-none-any.whl

$ poetry lock --no-update
Resolving dependencies... (4.2s)

$ poetry install
Installing dependencies from lock file...
```
