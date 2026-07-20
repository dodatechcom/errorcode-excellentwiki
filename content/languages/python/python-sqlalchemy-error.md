---
title: "[Solution] Python SQLAlchemy Error — Database ORM Issues"
description: "Fix SQLAlchemy errors by doing X, Y, Z. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 604
---

# Python SQLAlchemy Error — Database ORM Issues

SQLAlchemy errors include connection pool exhaustion, session management pitfalls, and database-level operational errors. These often manifest as connection leaks or stale state in long-running applications.

## Common Causes

```python
# Cause 1: Session not closed after use — connection leak
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://user:pass@localhost/db")
Session = sessionmaker(bind=engine)

def get_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    # Forgot session.close() — connection never returned to pool
    return user
```

```python
# Cause 2: Pool exhaustion from too many open connections
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=5,
    max_overflow=10
)

# Each call opens a new connection without closing the old one
for i in range(100):
    conn = engine.connect()
    result = conn.execute("SELECT 1")
    # Never called conn.close()
```

```python
# Cause 3: Using a session after rollback or close
from sqlalchemy.orm import Session

session = Session(engine)
session.add(User(name="alice"))
session.rollback()

# Stale session — operating on a rolled-back session raises InvalidRequestError
session.add(User(name="bob"))  # InvalidRequestError
```

```python
# Cause 4: Concurrent access to the same session from multiple threads
import threading

session = Session(engine)

def worker():
    user = session.query(User).get(1)
    user.name = "modified"

threads = [threading.Thread(target=worker) for _ in range(10)]
for t in threads:
    t.start()  # Concurrent session access raises greenlet/async errors
```

```python
# Cause 5: OperationalError when database server is unreachable
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

engine = create_engine("postgresql://user:pass@wrong-host/db")
try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
except OperationalError as e:
    print(f"Connection failed: {e}")
```

## How to Fix

### Fix 1: Use Context Managers for Sessions

```python
from sqlalchemy.orm import Session
from contextlib import contextmanager

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# Usage — session is always cleaned up
with get_session() as session:
    user = session.query(User).get(1)
    user.name = "updated"
```

### Fix 2: Configure Pool Settings for Production

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,  # Recycle connections after 30 minutes
    pool_pre_ping=True  # Verify connections before use
)
```

### Fix 3: Use Scoped Sessions for Thread Safety

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://user:pass@localhost/db")
SessionFactory = sessionmaker(bind=engine)

# Scoped session — one session per thread, automatically managed
session = scoped_session(SessionFactory)

# Each thread gets its own session
def worker():
    user = session.query(User).get(1)
    session.remove()  # Clean up thread-local session
```

### Fix 4: Handle OperationalError with Retry Logic

```python
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import time

def execute_with_retry(engine, query, max_retries=3):
    for attempt in range(max_retries):
        try:
            with engine.connect() as conn:
                result = conn.execute(text(query))
                return result.fetchall()
        except OperationalError as e:
            if attempt == max_retries - 1:
                raise
            print(f"Retry {attempt + 1}/{max_retries}: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
```

### Fix 5: Monitor and Dispose Leaked Connections

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)

# Check pool status
pool = engine.pool
print(f"Pool size: {pool.size()}")
print(f"Checked in: {pool.checkedin()}")
print(f"Checked out: {pool.checkedout()}")
print(f"Overflow: {pool.overflow()}")

# Force-dispose all connections in the pool
engine.dispose()
```

## Examples

```python
# Production-ready session management with scoped sessions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase
from contextlib import contextmanager

class Base(DeclarativeBase):
    pass

engine = create_engine(
    "postgresql://user:pass@localhost/myapp",
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)

@contextmanager
def db_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        Session.remove()

# Usage in application code
def create_user(name, email):
    with db_session() as session:
        user = User(name=name, email=email)
        session.add(user)
        return user.id
```

## Related Errors

- [Python Django ORM Error](/languages/python/python-django-orm-error/) — Django ORM query issues
- [Python ConnectionError](/languages/python/connectionerror/) — Network connection errors
- [Python SQLAlchemy Connection Error](/languages/python/sqlalchemy-connection-error/) — Direct SQLAlchemy connection issues
- [Python PicklingError](/languages/python/pickling-error/) — Serialization errors in multiprocessing
