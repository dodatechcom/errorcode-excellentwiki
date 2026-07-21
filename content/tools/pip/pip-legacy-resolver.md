---
title: "[Solution] pip Legacy Resolver -- Fix Backtracking Resolver Issues"
description: "Fix pip legacy resolver errors when pip's dependency resolver gets stuck in an infinite backtracking loop. Simplify requirements."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip's new dependency resolver is backtracking endlessly trying to find compatible versions.

## Common Causes

- Circular or extremely complex dependency constraints
- Very broad version ranges in multiple packages
- A package has conflicting optional dependencies

## How to Fix

### 1. Pin Specific Versions

```bash
pip install package-a==1.0.0 package-b==2.0.0
```

### 2. Use Constraints File

```bash
echo "lib==2.0.0" > constraints.txt
pip install -c constraints.txt package-a package-b
```

### 3. Install One Package at a Time

```bash
pip install package-a
pip install package-b
```

### 4. Use Legacy Resolver (Temporary)

```bash
pip install --use-deprecated=legacy-resolver <package>
```

## Examples

```bash
$ pip install package-a package-b
ERROR: pip's dependency resolver is stuck in backtracking

$ pip install "package-a==1.0.0" "package-b==2.0.0"
```
