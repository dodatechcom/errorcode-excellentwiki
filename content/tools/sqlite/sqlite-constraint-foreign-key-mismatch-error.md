---
title: "[Solution] SQLite Foreign key mismatch error"
description: "SQLite detected that a table's foreign key definition does not match the referenced table's structure."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite Foreign key mismatch error

SQLite raises a **Foreign key mismatch error** error when sqlite detected that a table's foreign key definition does not match the referenced table's structure. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- The parent table lacks a matching index on the referenced column.
- Column data types or collations do not match between tables.
- The referenced table does not exist.

## How to Fix

### Add an index on the parent table's referenced column

```sql
CREATE INDEX idx_dept_id ON departments(id);
```

### Verify column types match exactly

```sql
PRAGMA table_info(departments);
PRAGMA table_info(employees);
```

### Ensure the parent table exists before defining the foreign key

```sql
CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT);
```

## Examples

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    dept_id TEXT,
    FOREIGN KEY (dept_id) REFERENCES departments(id)
);
-- Error: foreign key mismatch - 'departments' and 'employees' columns differ
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
