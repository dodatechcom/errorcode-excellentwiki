---
title: "[Solution] pip Install Missing Source -- Fix No Source Distribution Available"
description: "Fix pip install missing source errors when neither source distribution nor wheel is available for a package. Find alternative installation sources."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip could not find either a source distribution or a wheel for the requested package on any configured index.

## Common Causes

- The package was removed from PyPI
- The index URL is wrong
- The package name is misspelled
- The package is on a private index not configured

## How to Fix

### 1. Check Package Name

```bash
pip index versions <package>
```

### 2. Verify Index URL

```bash
pip config get global.index-url
```

### 3. Add Extra Index

```bash
pip install <package> --extra-index-url https://pypi.org/simple/
```

### 4. Install from Git

```bash
pip install git+https://github.com/user/repo.git
```

## Examples

```bash
$ pip install my-internal-lib
ERROR: No matching distribution found for my-internal-lib

$ pip install my-internal-lib --extra-index-url https://pypi.internal.com/simple/
```
