---
title: "[Solution] pip Wheel Filename Error -- Fix Invalid Wheel Filename"
description: "Fix pip wheel filename error when a downloaded wheel file has an invalid name format. Re-download or manually rename the file."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip encountered a wheel file with a filename that does not conform to the wheel naming convention.

## Common Causes

- The wheel was renamed manually
- Downloaded file is corrupted
- The filename contains invalid characters
- The wheel format version is unsupported

## How to Fix

### 1. Re-download the Wheel

```bash
pip cache purge
pip install <package>
```

### 2. Check Wheel Format

```bash
pip download <package> -d ./downloads
ls ./downloads/*.whl
```

### 3. Verify the File is a Valid Zip

```bash
file downloads/*.whl
# Should show "Zip archive data"
```

### 4. Use pip to Build the Wheel

```bash
pip wheel <package> -w ./wheels
```

## Examples

```bash
$ pip install ./downloads/package.whl
InvalidWheelFilename: Invalid wheel filename: 'package-1.0.0.zip'

$ file downloads/package.whl
downloads/package.whl: Zip archive data

$ mv downloads/package.zip downloads/package-1.0.0-py3-none-any.whl
$ pip install ./downloads/package-1.0.0-py3-none-any.whl
```
