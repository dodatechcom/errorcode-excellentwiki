---
title: "[Solution] Poetry Requirements Invalid -- Fix requirements.txt Format"
description: "Fix Poetry requirements invalid errors when importing or using an invalid requirements.txt file. Correct the file format and syntax."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry found syntax errors or invalid entries when reading a `requirements.txt` file for import or comparison.

## Common Causes

- requirements.txt contains comments in wrong format
- Version specifiers use invalid syntax
- Empty lines with whitespace characters
- Line continuation characters are malformed

## How to Fix

### 1. Check the Requirements File

```bash
cat -A requirements.txt | head -20
```

### 2. Fix Common Syntax Issues

```bash
# Remove BOM and trailing whitespace
sed -i 's///g; s/[[:space:]]*$//' requirements.txt
```

### 3. Validate with pip

```bash
pip install --dry-run -r requirements.txt
```

### 4. Regenerate from Poetry

```bash
poetry export -f requirements.txt -o requirements.txt
```

## Examples

```bash
$ poetry install -r requirements.txt
InvalidRequirement: Invalid URL reference: requests>=2.28#egg=requests

# Fix: remove the #egg fragment
$ sed -i 's/#egg=.*//g' requirements.txt
```
