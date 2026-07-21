---
title: "[Solution] pip Requirements Not Found -- Fix Missing Requirements File"
description: "Fix pip requirements not found errors when the specified requirements file does not exist. Verify the file path and name."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `pip install -r <file>` was run but the specified requirements file does not exist.

## Common Causes

- The file path is wrong
- The file was deleted
- You are in the wrong directory
- The filename is misspelled

## How to Fix

### 1. Check File Exists

```bash
ls -la requirements.txt
```

### 2. Use Absolute Path

```bash
pip install -r /path/to/requirements.txt
```

### 3. Create a Basic Requirements File

```bash
pip freeze > requirements.txt
```

### 4. Check for Alternatives

```bash
ls *.txt *.pip requirements* -la
```

## Examples

```bash
$ pip install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory

$ ls *.txt
dev-requirements.txt

$ pip install -r dev-requirements.txt
```
