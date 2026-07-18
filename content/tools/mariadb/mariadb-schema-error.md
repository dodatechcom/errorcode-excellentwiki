---
title: "[Solution] MariaDB Schema Error — How to Fix"
description: "Fix MariaDB schema errors including missing database, charset mismatches, column type conflicts, and failed DDL operations with clear steps"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Schema Error

Schema errors occur when DDL operations fail due to invalid definitions, missing databases, charset mismatches, conflicting column types, or storage engine issues.

## Why It Happens

- The target database does not exist when creating or altering a table
- Column type in ALTER TABLE is incompatible with existing data
- Character set or collation mismatch between tables
- Reserved words are used as column names without backticks
- The table already exists when CREATE TABLE is used without IF NOT EXISTS
- A column exceeds the maximum row size for the chosen engine

## Common Error Messages

```
ERROR 1049 (42000): Unknown database 'mydb'
```

```
ERROR 1113 (HY000): A table must have at least 1 column
```

```
ERROR 1071 (42000): Specified key was too long; max key length is 3072 bytes
```

```
ERROR 1005 (HY000): Can't create table 'mydb.mytable' (errno: 150)
```

## How to Fix It

### 1. Create the Database If Missing

```sql
CREATE DATABASE IF NOT EXISTS mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

### 2. Fix Column Type Conflicts

```sql
-- Check max length before shrinking
SELECT MAX(LENGTH(name)) FROM mytable;

-- Safe approach: create new, migrate, drop old
ALTER TABLE mytable ADD COLUMN name_new VARCHAR(100);
UPDATE mytable SET name_new = LEFT(name, 100);
ALTER TABLE mytable DROP COLUMN name;
ALTER TABLE mytable CHANGE COLUMN name_new name VARCHAR(100);
```

### 3. Fix Key Length Errors

```sql
-- Use prefix index for TEXT columns
CREATE INDEX idx_body ON articles(body(255));

-- Or full-text index
CREATE FULLTEXT INDEX idx_body ON articles(body);
```

### 4. Fix Foreign Key errno: 150

```sql
DESCRIBE parent;
DESCRIBE child;

ALTER TABLE child DROP FOREIGN KEY fk_parent;
ALTER TABLE child ADD CONSTRAINT fk_parent
  FOREIGN KEY (parent_id) REFERENCES parent(id)
  ON DELETE CASCADE ON UPDATE CASCADE;
```

## Common Scenarios

- **Migration script fails**: Add `CREATE DATABASE IF NOT EXISTS` at top.
- **ALTER TABLE fails with row size error**: Switch to DYNAMIC row format or use TEXT for large columns.
- **Foreign key fails after rename**: Drop FK, rename column, recreate FK.

## Prevent It

- Always use `IF NOT EXISTS` in DDL scripts for idempotency
- Test schema changes on a copy of production data
- Use a migration tool (Flyway, Liquibase) for schema management

## Related Pages

- [MariaDB Table Corruption](/tools/mariadb/mariadb-table-corruption)
- [MariaDB Partition Error](/tools/mariadb/mariadb-partition-error)
- [MySQL Schema Error](/tools/mysql/mysql-schema-error)
