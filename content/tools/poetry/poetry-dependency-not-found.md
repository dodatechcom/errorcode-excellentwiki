---
title: "[Solution] Poetry Dependency Not Found -- Fix Package Resolution Failure"
description: "Fix Poetry dependency not found errors when a required package cannot be found on any configured source. Verify the package name and sources."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not find a package on any configured package source. The package name may be wrong or the source is misconfigured.

## Common Causes

- Package name is misspelled
- Package was removed from PyPI
- The package is on a private source not configured
- The source index is stale

## How to Fix

### 1. Verify the Package Exists

```bash
pip index versions <package>
```

### 2. Search PyPI

```bash
poetry search <package>
```

### 3. Check Source Configuration

```bash
poetry source --list
```

### 4. Add Missing Source

```toml
[[tool.poetry.source]]
name = "private"
url = "https://pypi.internal.com/simple/"
priority = "supplemental"
```

## Examples

```bash
$ poetry add my-private-lib
PackageNotFound: No package named 'my-private-lib'

$ poetry source --list
# Check if private source is listed

[[tool.poetry.source]]
name = "internal"
url = "https://pypi.internal.com/simple/"

$ poetry add my-private-lib
Resolving dependencies...
```
