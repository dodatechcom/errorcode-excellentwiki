---
title: "[Solution] pip Legacy Python Error -- Fix Python 2 pip Compatibility"
description: "Fix pip legacy Python error when trying to use pip features not available in Python 2. Migrate to Python 3."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means you are trying to use a pip feature that requires Python 3 but you are running Python 2.

## Common Causes

- Running pip under Python 2.7
- System default python points to Python 2
- Scripts use `#!/usr/bin/env python` which resolves to Python 2

## How to Fix

### 1. Use python3 Explicitly

```bash
python3 -m pip install <package>
```

### 2. Upgrade to Python 3

```bash
sudo apt install python3 python3-pip
```

### 3. Use python3 as Default

```bash
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
```

### 4. Check Which Python pip Uses

```bash
pip --version
# Should show python3.x in the path
```

## Examples

```bash
$ pip install requests
DEPRECATION: Python 2.7 will reach the end of its life

$ python3 -m pip install requests
Successfully installed requests-2.31.0
```
