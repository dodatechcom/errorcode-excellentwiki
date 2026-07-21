---
title: "[Solution] FastAPI UploadFile Seek Error"
description: "UploadFile seek not working."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

UploadFile seek not working.

## Common Causes

Not resetting.

## How to Fix

Seek to 0.

## Example

```python
await file.seek(0)
contents = await file.read()
```
