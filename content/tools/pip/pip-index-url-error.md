---
title: "[Solution] pip Index URL Error -- Fix Package Index Configuration"
description: "Fix pip index URL error when the configured package index URL is invalid or unreachable. Verify and correct the index URL."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip cannot reach or parse the package index URL configured in pip.conf or via --index-url.

## Common Causes

- The index URL has a typo
- The index server is down
- The URL uses HTTP when HTTPS is required
- The index URL format is wrong (missing /simple/)

## How to Fix

### 1. Check Current Index URL

```bash
pip config get global.index-url
```

### 2. Set Correct URL

```bash
pip config set global.index-url https://pypi.org/simple/
```

### 3. Test the URL

```bash
curl -I https://pypi.org/simple/
```

### 4. Use Default PyPI

```bash
pip install <package> -i https://pypi.org/simple/
```

## Examples

```bash
$ pip install requests
ERROR: Could not find a version that satisfies the requirement requests

$ pip config get global.index-url
https://old-mirror.example.com/pypi/

$ pip config set global.index-url https://pypi.org/simple/
$ pip install requests
Successfully installed requests-2.31.0
```
