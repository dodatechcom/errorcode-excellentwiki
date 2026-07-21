---
title: "[Solution] FastAPI Health Check Database Error"
description: "Fix FastAPI health check database errors when health endpoints fail to verify database connectivity."
frameworks: ["fastapi"]
error-types: ["database-error"]
severities: ["error"]
---

Health check endpoints in FastAPI fail when they cannot verify database connectivity.

## Common Causes

- Database connection pool exhausted during health check
- Health check uses synchronous database call in async endpoint
- Database is temporarily unavailable
- Health check timeout too short for database queries
- ORM session not properly closed after health check query

## How to Fix

### Implement Proper Health Check

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": str(e)}
```

### Use Separate Health Check Endpoints

```python
@app.get("/health/live")
def liveness():
    return {"status": "alive"}

@app.get("/health/ready")
def readiness(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception:
        return JSONResponse(status_code=503, content={"status": "not ready"})
```

## Examples

```python
from fastapi import FastAPI
from sqlalchemy.orm import Session

app = FastAPI()

# Bug -- synchronous DB call in async context
@app.get("/health")
async def broken_health(db: Session = Depends(get_db)):
    result = db.execute("SELECT 1")  # May block the event loop
    return {"status": "ok"}

# Fix -- use async session or run in executor
@app.get("/health")
async def working_health(db: Session = Depends(get_db)):
    result = await asyncio.to_thread(db.execute, text("SELECT 1"))
    return {"status": "ok"}
```

Use `/health/live` for liveness probes and `/health/ready` for readiness probes in Kubernetes.
