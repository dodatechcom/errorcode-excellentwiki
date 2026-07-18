---
title: "[Solution] YugabyteDB YSQL Error — How to Fix"
description: "Fix YugabyteDB YSQL errors by resolving PostgreSQL compatibility issues, fixing YSQL-specific features, and handling SQL syntax problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB YSQL Error

YugabyteDB YSQL errors occur when using the PostgreSQL-compatible YSQL interface. While YSQL supports most PostgreSQL features, some extensions and functions have limitations.

## Why It Happens

- SQL syntax is not supported in YSQL
- PostgreSQL extension is not available in YugabyteDB
- YSQL-specific features are used incorrectly
- Distributed execution fails for certain queries
- Sequence or auto-increment configuration is wrong
- Stored procedure uses unsupported PL/pgSQL features

## Common Error Messages

```
ERROR: unsupported SQL statement in distributed mode
```

```
ERROR: extension not supported
```

```
ERROR: function does not exist
```

```
ERROR: YSQL operation not allowed
```

## How to Fix It

### 1. Use Supported YSQL Features

```sql
-- YSQL supports most PostgreSQL syntax
-- CREATE TABLE, INSERT, UPDATE, DELETE
-- JOINs, subqueries, CTEs
-- Window functions
-- Stored procedures (PL/pgSQL)

-- Use serial/uuid for auto-generation
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 2. Handle Unsupported Extensions

```sql
-- Check available extensions
SELECT * FROM pg_available_extensions;

-- Some extensions available:
-- pgcrypto, fuzzystrmatch, uuid-ossp, intarray
-- pg_stat_statements

-- NOT available: postgis, timescaledb, pgvector
```

### 3. Use Sequences Correctly

```sql
-- Create sequence
CREATE SEQUENCE order_seq START 1;

-- Use in table
CREATE TABLE orders (
  id INTEGER DEFAULT nextval('order_seq') PRIMARY KEY,
  amount DECIMAL
);

-- Or use SERIAL (auto-creates sequence)
CREATE TABLE orders2 (
  id SERIAL PRIMARY KEY,
  amount DECIMAL
);
```

### 4. Fix Stored Procedures

```sql
-- YSQL supports PL/pgSQL
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger
CREATE TRIGGER set_timestamp
  BEFORE UPDATE ON users
  FOR EACH ROW
  EXECUTE FUNCTION update_timestamp();
```

## Common Scenarios

- **Extension not found**: Check if extension is supported in YugabyteDB.
- **Auto-increment not working**: Use SERIAL or UUID instead of custom sequences.
- **Stored procedure fails**: Check PL/pgSQL feature compatibility.

## Prevent It

- Check YugabyteDB documentation for supported PostgreSQL features
- Test SQL on YugabyteDB before using in production
- Use YSQL-compatible alternatives for unsupported features

## Related Pages

- [YugabyteDB Query Error](/tools/yugabyte/yugabyte-query-error)
- [YugabyteDB DDL Error](/tools/yugabyte/yugabyte-ddl-error)
- [YugabyteDB YCQL Error](/tools/yugabyte/yugabyte-ycql-error)
