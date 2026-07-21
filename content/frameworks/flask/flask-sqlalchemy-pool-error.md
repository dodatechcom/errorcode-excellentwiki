---
title: "[Solution] Flask SQLAlchemy Connection Pool Error"
description: "Fix Flask SQLAlchemy connection pool errors when database connections are exhausted or timing out."
frameworks: ["flask"]
error-types: ["database-error"]
severities: ["error"]
---

Connection pool errors occur when all database connections are in use and new requests cannot acquire a connection.

## Common Causes

- Pool size too small for traffic
- Connections not returned to pool after use
- Long-running queries holding connections
- Connection timeout too short
- Pool not configured for production load

## How to Fix

### Configure Connection Pool

```python
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 10
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800
app.config["SQLALCHEMY_POOL_PRE_PING"] = True
```

### Handle Pool Exhaustion

```python
from flask import Flask
from sqlalchemy.pool import QueuePool

app = Flask(__name__)
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "poolclass": QueuePool,
    "pool_size": 20,
    "max_overflow": 10,
    "pool_timeout": 30,
    "pool_recycle": 1800,
}
```

### Monitor Pool Usage

```python
@app.route("/pool-status")
def pool_status():
    engine = db.engine
    pool = engine.pool
    return {
        "size": pool.size(),
        "checked_in": pool.checkedin(),
        "checked_out": pool.checkedout(),
        "overflow": pool.overflow(),
    }
```

## Examples

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Bug -- default pool size too small
# app.config["SQLALCHEMY_POOL_SIZE"] = 5

# Fix -- configure for production
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 10
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

db = SQLAlchemy(app)
```
