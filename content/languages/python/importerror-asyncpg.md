---
title: "[Solution] Python ImportError: No module named 'asyncpg' — Fix"
description: "Fix Python ImportError: No module named 'asyncpg'. Install asyncpg with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 313
---

# Python ImportError: No module named 'asyncpg'

The `ModuleNotFoundError: No module named 'asyncpg'` error occurs when Python cannot locate the asyncpg package, which provides a fast PostgreSQL database client library for asyncio.

## Common Causes

```python
# Cause 1: asyncpg not installed
import asyncpg  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version or virtual environment
from asyncpg import create_pool  # ModuleNotFoundError

# Cause 3: Missing PostgreSQL development headers
# asyncpg requires libpq-dev on Linux
```

```python
# Cause 4: Compiled extension build failure
# asyncpg requires a C compiler during installation

# Cause 5: Python version incompatibility
# asyncpg requires Python 3.8+
```

## How to Fix

### Fix 1: Install asyncpg with pip

```bash
pip install asyncpg

# Verify installation
python -c "import asyncpg; print(asyncpg.__version__)"
```

### Fix 2: Install system dependencies first

```bash
# Ubuntu/Debian
sudo apt-get install libpq-dev python3-dev gcc

# macOS
xcode-select --install

# Then install asyncpg
pip install asyncpg
```

### Fix 3: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install asyncpg
python -c "import asyncpg; print('OK')"
```

## Examples

```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        user="postgres",
        password="password",
        database="mydb",
        host="localhost"
    )

    # Execute query
    row = await conn.fetchrow(
        "SELECT * FROM users WHERE id = $1", 1
    )
    print(row)

    await conn.close()

asyncio.run(main())
```

```python
# Connection pool
import asyncpg
import asyncio

async def pooled():
    pool = await asyncpg.create_pool(
        "postgresql://user:pass@localhost/mydb",
        min_size=5,
        max_size=20
    )
    async with pool.acquire() as conn:
        result = await conn.fetch("SELECT * FROM users")
    await pool.close()
```

## Related Errors

- {{< relref "importerror-psycopg2" >}} — ImportError: psycopg2
- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-aioredis" >}} — ImportError: aioredis
