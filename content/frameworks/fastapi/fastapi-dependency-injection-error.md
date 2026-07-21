---
title: "[Solution] FastAPI Dependency Injection Error"
description: "Dependency not resolving."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Dependency not resolving.

## Common Causes

Wrong Depends usage.

## How to Fix

Use Depends correctly.

## Example

```python
from fastapi import Depends
async def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()
@app.get('/users')
async def get_users(db=Depends(get_db)): return db.query(User).all()
```
