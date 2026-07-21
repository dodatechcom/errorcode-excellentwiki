---
title: "[Solution] Flask Flask Before First Request Error"
description: "before_first_request deprecated."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

before_first_request deprecated.

## Common Causes

Old pattern.

## How to Fix

Use app startup.

## Example

```python
@app.before_request
def before(): pass
```
