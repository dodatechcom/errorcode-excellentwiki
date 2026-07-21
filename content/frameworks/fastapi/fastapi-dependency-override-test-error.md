---
title: "[Solution] FastAPI Dependency Override Test Error"
description: "Override not working in tests."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Override not working in tests.

## Common Causes

Wrong override.

## How to Fix

Use dependency_overrides.

## Example

```python
app.dependency_overrides[get_db] = override_db
```
