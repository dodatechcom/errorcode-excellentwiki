---
title: "[Solution] Python SQLAlchemy Connection Error — How to Fix"
description: "Fix Python SQLAlchemy connection and query errors. Resolve connection pool, ORM mapping, and migration issues with SQLAlchemy."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python SQLAlchemy Connection Error

A SQLAlchemy error occurs when the ORM or Core engine fails to connect to the database, execute queries, or map Python objects to database tables.

## Why It Happens

SQLAlchemy manages a connection pool and maps Python class attributes to database columns. Errors occur when connections are exhausted, when mapped attributes don't match the schema, or when transactions deadlock.

## Common Error Messages

- `OperationalError: (sqlalchemy.exc.OperationalError) could not connect`
- `InvalidRequestError: Session's transaction has been rolled back`
- `ArgumentError: SQL expression expected`
- `ProgrammingError: relation 'table_name' does not exist`

## How to Fix It

### Fix 1: Configure connection pooling

```python
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://user:pass@localhost/db',
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)
```

### Fix 2: Handle session lifecycle properly

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    try:
        user = User(name='Alice')
        session.add(user)
        session.commit()
    except Exception:
        session.rollback()
        raise
```

### Fix 3: Fix attribute mapping

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
```

### Fix 4: Use connection timeout

```python
engine = create_engine(
    'postgresql://user:pass@localhost/db',
    connect_args={'connect_timeout': 10}
)
```

## Common Scenarios

- **Connection pool exhaustion** — Too many concurrent connections exceed pool_size + max_overflow.
- **Detached instances** — Accessing relationships after session is closed raises DetachedInstanceError.
- **N+1 query problem** — Accessing lazy-loaded relationships in loops causes excessive queries.

## Prevent It

- Always use session.close() or context managers for sessions
- Set pool_pre_ping=True to detect stale connections
- Use joinedload() or selectinload() to avoid N+1 queries

## Related Errors

- - [psycopg2.OperationalError](/languages/python/psycopg2-operationalerror/) — PostgreSQL connection error
- - [sqlite3.DatabaseError](/languages/python/sqlite3-databaseerror/) — SQLite error
