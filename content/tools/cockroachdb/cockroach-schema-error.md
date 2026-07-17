---
title: "[Solution] CockroachDB Schema Error - Fix Relation Does Not Exist"
description: "Fix CockroachDB relation does not exist errors by creating the missing table, verifying the correct database name in the connection, and fixing case sensitivity"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB schema error occurs when a query references a table, view, or index that does not exist in the current database. The error message is `relation "table_name" does not exist` or `relation does not exist`.

## What This Error Means

CockroachDB follows PostgreSQL wire protocol, so it returns the standard PostgreSQL error code `42P01` (undefined_table) when a query references a non-existent relation. The error occurs during query planning when the catalog lookup fails.

This is distinct from a permissions error (where the relation exists but the user lacks access) and a syntax error (where the relation name is malformed).

## Why It Happens

- Table was not created in the current database
- Query references a table in a different schema without qualification
- Case sensitivity issue: unquoted identifiers are lowercased in CockroachDB
- Table was dropped but the application still references it
- Wrong database in the connection string
- Missing migration step in a deployment pipeline
- Table name includes special characters or reserved words

## How to Fix It

### 1. List Tables in the Current Database

```sql
SHOW TABLES;
SHOW TABLES FROM my_database;
SHOW TABLES FROM my_schema;
```

### 2. Create the Table

```sql
CREATE TABLE IF NOT EXISTS my_table (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name STRING NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
```

### 3. Check the Search Path

```sql
SHOW search_path;
SET search_path = my_schema, public;
```

### 4. Use Double Quotes for Case-Sensitive Names

```sql
-- If table was created with "MyTable" (capital M)
SELECT * FROM "MyTable";

-- Unquoted, CockroachDB looks for "mytable" (lowercase)
```

### 5. Verify the Database Connection

```sql
SHOW DATABASE;
-- If wrong, reconnect to the correct database
```

### 6. Run Pending Migrations

```bash
# Check if migrations are pending
cockroach sql --host=localhost:26257 --database=mydb < migrations/001_create_tables.sql
```

### 7. Qualify Table Names with Schema

```sql
-- Instead of:
SELECT * FROM users;

-- Use fully qualified name:
SELECT * FROM my_schema.users;
```

## Common Mistakes

- Forgetting that CockroachDB lowercases unquoted identifiers
- Running DDL against one database but the application connects to another
- Not running database migrations before deploying application code
- Using reserved words as table names without quoting

## Related Pages

- [CockroachDB Schema Change](/tools/cockroachdb/cockroach-schema-change)
- [CockroachDB Connection Refused](/tools/cockroachdb/cockroach-connection-refused)
- [CockroachDB Serializable Error](/tools/cockroachdb/cockroach-serializable-error)
