---
title: "[Solution] Django Template Loader Error"
description: "Template not found."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Template not found.

## Common Causes

DIRS not set.

## How to Fix

Add directory.

## Example

```python
TEMPLATES = [{'DIRS': [BASE_DIR / 'templates']}]
```
