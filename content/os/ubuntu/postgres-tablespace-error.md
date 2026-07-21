---
title: "PostgreSQL Tablespace Error"
description: "PostgreSQL cannot create or access tablespace"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL Tablespace Error

PostgreSQL cannot create or access tablespace

## Common Causes

- Tablespace directory does not exist
- Directory permissions not allowing PostgreSQL access
- Filesystem full on tablespace partition
- Tablespace already exists with same name

## How to Fix

1. Check tablespace: `SELECT spcname FROM pg_tablespace;`
2. Create directory: `mkdir -p /pgdata/tbs && chown postgres:postgres /pgdata/tbs`
3. Create tablespace: `CREATE TABLESPACE mytbs LOCATION '/pgdata/tbs';`
4. Check disk: `df -h /pgdata/`

## Examples

```sql
-- List tablespaces
SELECT spcname, pg_tablespace_size(spcname) AS size FROM pg_tablespace;

-- Create tablespace
CREATE TABLESPACE mytbs LOCATION '/pgdata/tbs';

-- Use tablespace
CREATE TABLE mytable (id int) TABLESPACE mytbs;
```
