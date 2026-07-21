---
title: "[Solution] pip Install Pre-Release -- Fix Installing Pre-release Versions"
description: "Fix pip install pre-release errors when pip refuses to install pre-release versions by default. Use --pre flag to include them."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip did not find a stable release of the package and only pre-release versions are available.

## Common Causes

- The package has no stable release yet
- You specifically need a beta or RC version
- The stable release was yanked

## How to Fix

### 1. Allow Pre-releases

```bash
pip install --pre <package>
```

### 2. Specify Pre-release Version

```bash
pip install <package>==2.0.0b1
```

### 3. Use --pre with Upgrade

```bash
pip install --pre --upgrade <package>
```

### 4. Check Available Versions

```bash
pip index versions <package>
```

## Examples

```bash
$ pip install numpy==2.0.0
ERROR: No matching distribution found for numpy==2.0.0

$ pip index versions numpy
numpy (2.0.0rc1)

$ pip install --pre numpy==2.0.0rc1
Successfully installed numpy-2.0.0rc1
```
