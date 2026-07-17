---
title: "[Solution] SQLAlchemy OperationalError: Connection Failed Fix"
description: "Fix SQLAlchemy OperationalError connection failed. Verify connection strings, check database availability, and configure pool settings."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SQLAlchemy OperationalError: Connection Failed Fix

An `sqlalchemy.exc.OperationalError` is raised when SQLAlchemy cannot establish or maintain a connection to the database. This covers connection refused, authentication failure, and database does not exist errors.

## What This Error Means

Common messages:

- `OperationalError: (psycopg2.OperationalError) connection refused`
- `OperationalError: (psycopg2.OperationalError) FATAL: database "mydb" does not exist`
- `OperationalError: (pymysql.OperationalError) (2003, "Can't connect to MySQL server")`

SQLAlchemy's connection pool attempted to connect to the database but the underlying database driver rejected the connection or the server is unreachable.

## Common Causes

```python
from sqlalchemy import create_engine

# Cause 1: Wrong connection string
engine = create_engine("postgresql://user:pass@localhost:5432/mydb")

# Cause 2: Database server not running
engine = create_engine("postgresql://user:pass@localhost:5432/mydb")
engine.connect()  # ConnectionRefusedError

# Cause 3: Wrong credentials
engine = create_engine("postgresql://wrong_user:wrong_pass@localhost:5432/mydb")

# Cause 4: Connection pool exhausted
engine = create_engine("postgresql://...", pool_size=5, max_overflow=0)
# All connections checked out, new request waits then times out
```

## How to Fix

### Fix 1: Verify connection string

```python
from sqlalchemy import create_engine

# PostgreSQL
engine = create_engine("postgresql://user:password@localhost:5432/mydb")

# MySQL
engine = create_engine("mysql+pymysql://user:password@localhost:3306/mydb")

# SQLite
engine = create_engine("sqlite:///path/to/database.db")

# Test connection
with engine.connect() as conn:
    print("Connected successfully")
```

### Fix 2: Configure connection pool settings

```python
engine = create_engine(
    "postgresql://user:password@localhost:5432/mydb",
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
)
```

### Fix 3: Use engine.dispose() to reset connections

```python
# After long idle period
engine.dispose()

# Get fresh connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
```

### Fix 4: Handle transient connection failures with retry

```python
from sqlalchemy import create_engine, text
from tenacity import retry, stop_after_attempt, wait_exponential

engine = create_engine("postgresql://user:password@localhost:5432/mydb")

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def query_db():
    with engine.connect() as conn:
        return conn.execute(text("SELECT 1")).fetchone()
```

### Fix 5: Check database availability before connecting

```python
import socket

def is_db_reachable(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except (ConnectionRefusedError, TimeoutError):
        return False

if is_db_reachable("localhost", 5432):
    engine = create_engine("postgresql://user:password@localhost:5432/mydb")
else:
    print("Database is not reachable")
```

## Related Errors

- {{< relref "connectionrefusederror" >}} — Python connection refused error.
- {{< relref "importerror-sqlalchemy" >}} — SQLAlchemy import issue.
