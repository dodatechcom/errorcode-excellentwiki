---
title: "[Solution] SQLite FOREIGN KEY constraint failed"
description: "An INSERT or UPDATE violated a FOREIGN KEY constraint by referencing a non-existent parent row."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite FOREIGN KEY constraint failed

SQLite raises a **FOREIGN KEY constraint failed** error when an insert or update violated a foreign key constraint by referencing a non-existent parent row. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Inserting a child row whose FK value has no matching parent row.
- Deleting a parent row that still has child rows (without CASCADE).
- Foreign key references a table that does not exist.

## How to Fix

### Ensure the referenced parent row exists

```sql
INSERT INTO departments (id, name) VALUES (1, 'Engineering');
INSERT INTO employees (id, name, dept_id) VALUES (1, 'Alice', 1);
```

### Use ON DELETE CASCADE for automatic child cleanup

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(id) ON DELETE CASCADE
);
```

### Enable foreign key checking explicitly

```sql
PRAGMA foreign_keys = ON;
```

## Examples

```sql
PRAGMA foreign_keys = ON;
INSERT INTO employees (id, dept_id) VALUES (1, 999);
-- Error: FOREIGN KEY constraint failed
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
