---
title: "[Solution] PostgreSQL Tablespace Error"
description: "Fix PostgreSQL tablespace errors. Resolve issues creating or using database tablespaces."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Tablespace Error

ERROR: could not create tablespace directory

This error occurs when PostgreSQL cannot create or access a tablespace directory due to permission or disk issues.

## Common Causes

- Insufficient filesystem permissions on the tablespace directory
- The tablespace directory does not exist on the target node
- Insufficient disk space on the tablespace volume

## How to Fix

1. Create the tablespace directory with correct ownership:

```bash
sudo mkdir -p /data/pg_tablespace
sudo chown postgres:postgres /data/pg_tablespace
sudo chmod 700 /data/pg_tablespace
```

2. Create the tablespace in PostgreSQL:

```sql
CREATE TABLESPACE fastspace LOCATION '/data/pg_tablespace';
```

3. Check disk space on the tablespace volume:

```bash
df -h /data/pg_tablespace
```

## Examples

```sql
-- Assign a table to a specific tablespace
ALTER TABLE large_events SET TABLESPACE fastspace;

-- Create a new table in a specific tablespace
CREATE TABLE logs (
  id SERIAL PRIMARY KEY,
  message TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
) TABLESPACE fastspace;
```
