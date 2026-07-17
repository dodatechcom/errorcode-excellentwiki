---
title: "ERROR: database \"X\" already exists"
description: "Attempted to create a PostgreSQL database that already exists"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when you try to create a database with a name that is already taken in the PostgreSQL cluster.

## Common Causes

- Running CREATE DATABASE twice with the same name
- Script executed multiple times without idempotency
- Typo in database name (e.g., trying to create "mydb" when "mydb" exists)
- Schema migration rerun without drop

## How to Fix

1. Use `IF NOT EXISTS` to avoid the error:

```sql
CREATE DATABASE IF NOT EXISTS mydb;
```

2. List existing databases to verify the name:

```sql
SELECT datname FROM pg_database WHERE datname = 'mydb';
```

3. Drop the existing database if needed:

```bash
dropdb mydb
```

## Examples

```sql
-- This will fail if mydb already exists
CREATE DATABASE mydb;

-- Error output:
-- ERROR: database "mydb" already exists

-- Safe approach:
CREATE DATABASE IF NOT EXISTS mydb;
```

```bash
# Check if database exists
psql -l | grep mydb

# Create only if not exists
createdb mydb || echo "Database already exists"
```

## Related Errors

- [Connection Refused](/tools/postgresql/connection-refused)
- [Table Already Exists](/tools/mysql/table-exists)
