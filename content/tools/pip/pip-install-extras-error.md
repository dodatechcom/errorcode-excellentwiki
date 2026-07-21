---
title: "[Solution] pip Install Extras Error -- Fix Invalid Extras Specification"
description: "Fix pip install extras error when specifying package extras with invalid syntax. Use correct bracket notation."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means the extras syntax in the package specification is invalid. pip cannot parse the extras requirement.

## Common Causes

- Wrong bracket syntax for extras
- Space inside brackets
- Using single quotes instead of double quotes in shell
- Missing bracket characters

## How to Fix

### 1. Use Correct Syntax

```bash
pip install "package[extra1,extra2]"
```

### 2. Quote for Shell

```bash
pip install "requests[security,socks]"
```

### 3. Check Available Extras

```bash
pip index versions <package>
pip install <package>[all]
```

### 4. Use Separate Packages

```bash
pip install requests pyOpenSSL pysocks
```

## Examples

```bash
$ pip install requests[security]
ERROR: Invalid requirement: 'requests[security'

# Use quotes:
$ pip install "requests[security]"
Successfully installed pyOpenSSL-23.2.0
```
