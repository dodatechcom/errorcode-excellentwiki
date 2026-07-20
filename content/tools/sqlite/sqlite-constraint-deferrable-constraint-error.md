---
title: "[Solution] SQLite Deferrable constraint error"
description: "A DEFERRABLE constraint was defined but used in a context that does not support deferred checking."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite Deferrable constraint error

SQLite raises a **Deferrable constraint error** error when a deferrable constraint was defined but used in a context that does not support deferred checking. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- Using DEFERRABLE INITIALLY DEFERRED with an incompatible PRAGMA.
- Deferrable constraint referenced outside a transaction.
- Constraint definition syntax error in DEFERRABLE clause.

## How to Fix

### Wrap the operation in a transaction for deferred constraints

```sql
BEGIN DEFERRED;
INSERT INTO child VALUES (1, 10);
-- FK checked at COMMIT
COMMIT;
```

### Use IMMEDIATE for constraints that must be checked right away

```sql
CREATE TABLE child (
    id INTEGER,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES parent(id) DEFERRABLE INITIALLY IMMEDIATE
);
```

### Verify PRAGMA foreign_keys is enabled

```sql
PRAGMA foreign_keys = ON;
```

## Examples

```sql
CREATE TABLE child (
    id INTEGER,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES parent(id) DEFERRABLE INITIALLY DEFERRED
);
-- Outside a transaction, deferred constraints act like immediate
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
