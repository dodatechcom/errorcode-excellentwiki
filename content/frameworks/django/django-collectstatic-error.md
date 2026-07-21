---
title: "[Solution] Django Collectstatic Error"
description: "collectstatic failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

collectstatic failing.

## Common Causes

Wrong STATIC_ROOT.

## How to Fix

Set root.

## Example

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```
