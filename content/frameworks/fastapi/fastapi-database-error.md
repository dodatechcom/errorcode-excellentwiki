---
title: "[Solution] FastAPI Database Error -- How to Fix"
description: "Fix FastAPI database errors. Resolve SQLAlchemy connection failures, query errors, and database session issues."
frameworks: ["fastapi"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI database error occurs when database connections fail, queries are incorrect, or session management has issues.

## Why It Happens

Database errors happen due to connection pool exhaustion, incorrect URLs, missing tables, query syntax errors, or session lifecycle issues.

## Common Error Messages

```
sqlalchemy.exc.OperationalError: connection to server timed out
```

```
sqlalchemy.exc.ProgrammingError: relation 'users' does not exist
```

```
sqlalchemy.exc.IntegrityError: duplicate key value violates unique constraint
```

```
sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached
```

## How to Fix It

### 1. Configure Database Connection Pool

Set up proper connection pooling.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### 2. Use Database Sessions Properly

Implement dependency injection for sessions.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post('/users/')
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

### 3. Handle Database Errors Gracefully

Add error handling.

```python
from sqlalchemy.exc import IntegrityError, OperationalError

@app.post('/users/')
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail='User already exists')
    except OperationalError:
        db.rollback()
        raise HTTPException(status_code=503, detail='Database unavailable')
    db.refresh(db_user)
    return db_user
```

### 4. Use Async Database Drivers

Switch to async drivers.

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine('postgresql+asyncpg://user:pass@localhost/db')
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```

## Common Scenarios

**Scenario 1: Connection timeout under high traffic.**
Increase pool_size and use pool_pre_ping.

**Scenario 2: Table not found error.**
Run `alembic upgrade head`.

**Scenario 3: Duplicate key violation.**
Catch IntegrityError and return 409.

## Prevent It

1. **Use connection pooling.**
Configure appropriate pool size.

2. **Run migrations before deployment.**
Always run `alembic upgrade head`.

3. **Monitor database health.**
Track connections and query performance.

