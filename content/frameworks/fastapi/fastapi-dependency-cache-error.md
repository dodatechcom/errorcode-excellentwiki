---
title: "[Solution] FastAPI Dependency Cache Error"
description: "Dependency cached incorrectly."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Dependency cached incorrectly.

## Common Causes

Using class dependency.

## How to Fix

Use function dependency.

## Example

```python
# Function dependencies are cached per request
def dep(): return compute_expensive()
```
