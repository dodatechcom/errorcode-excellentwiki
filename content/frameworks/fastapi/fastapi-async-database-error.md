---
title: "[Solution] FastAPI Async Database Error"
description: "Async DB blocking."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Async DB blocking.

## Common Causes

Using sync driver.

## How to Fix

Use async drivers.

## Example

```python
from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine('postgresql+asyncpg://...')
```
