---
title: "[Solution] FastAPI UploadFile Read Error"
description: "UploadFile not reading."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

UploadFile not reading.

## Common Causes

Not awaiting.

## How to Fix

Use async methods.

## Example

```python
content = await file.read()
```
