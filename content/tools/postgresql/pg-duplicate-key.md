---
title: "[Solution] PostgreSQL Duplicate Key Violates Unique Constraint - Fix Insert Conflicts"
description: "Fix PostgreSQL duplicate key value violates unique constraint errors by using upsert, handling conflicts, and designing proper unique indexes"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Duplicate Key Violates Unique Constraint

This error occurs when an `INSERT` or `UPDATE` statement attempts to create a row that duplicates a value in a column (or set of columns) that has a `UNIQUE` constraint or unique index.

## What This Error Means

PostgreSQL enforces `UNIQUE` constraints and unique indexes at the row level. When you try to insert a row with a value that already exists in the constrained column(s), the operation fails:

```
ERROR: duplicate key value violates unique constraint "mytable_email_key"
DETAIL: Key (email)=(user@example.com) already exists.
```

The error message includes the constraint name and the duplicate value, which makes debugging straightforward. The constraint can be a `PRIMARY KEY`, a `UNIQUE` constraint, or a `CREATE UNIQUE INDEX` statement.

## Why It Happens

- Race conditions where two concurrent inserts try to create the same row
- Application logic does not check for existence before inserting
- Bulk import or `COPY` operation encounters duplicate data
- `INSERT ... ON CONFLICT` is not used, and duplicates are expected
- A unique index was added to a table that already contains duplicate values
- Composite unique constraints are violated by a combination of values

## How to Fix It

### 1. Use INSERT with ON CONFLICT (Upsert)

```sql
-- Insert or update if the email already exists
INSERT INTO users (email, name) VALUES ('user@example.com', 'John')
ON CONFLICT (email)
DO UPDATE SET name = EXCLUDED.name;

-- Insert or do nothing if conflict exists
INSERT INTO users (email, name) VALUES ('user@example.com', 'John')
ON CONFLICT (email)
DO NOTHING;
```

### 2. Check for Existing Rows First

```sql
-- Verify before inserting
SELECT EXISTS (SELECT 1 FROM users WHERE email = 'user@example.com');
```

### 3. Handle Concurrency with Advisory Locks

```sql
-- Prevent race conditions using an advisory lock
SELECT pg_advisory_xact_lock(hashtext('user@example.com'));
INSERT INTO users (email, name) VALUES ('user@example.com', 'John');
```

### 4. Remove Duplicates Before Adding the Constraint

```sql
-- Find duplicates
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Keep only the first occurrence
DELETE FROM users
WHERE ctid NOT IN (
    SELECT MIN(ctid)
    FROM users
    GROUP BY email
);

-- Now add the unique constraint
ALTER TABLE users ADD CONSTRAINT users_email_key UNIQUE (email);
```

### 5. Use a Temporary Table for Bulk Imports

```sql
-- Load data into a temp table, deduplicate, then insert
CREATE TEMP TABLE staging (LIKE users);

COPY staging FROM '/path/to/data.csv';

INSERT INTO users (email, name)
SELECT DISTINCT ON (email) email, name
FROM staging
ON CONFLICT (email) DO NOTHING;

DROP TABLE staging;
```

## Common Mistakes

- Catching the duplicate key error in application code and retrying without `ON CONFLICT` -- this wastes cycles under high concurrency
- Assuming `UNIQUE` constraints are database-level only -- they prevent duplicates at the index level regardless of how the insert happens
- Not considering NULL values -- multiple NULLs are allowed in a UNIQUE column in PostgreSQL
- Using `INSERT OR IGNORE` patterns from other databases instead of PostgreSQL's native `ON CONFLICT`
- Adding a unique constraint to a column that already contains duplicates without first cleaning the data

## Related Pages

- [PostgreSQL Foreign Key Violation](/tools/postgresql/pg-foreign-key-violation)
- [PostgreSQL Null Violation](/tools/postgresql/pg-null-violation)
- [PostgreSQL Serialization Failure](/tools/postgresql/pg-serialization-failure)
- [MySQL Duplicate Entry](/tools/mysql/mysql-duplicate-entry)
