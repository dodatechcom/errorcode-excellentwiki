---
title: "[Solution] SQLite ON CONFLICT clause error"
description: "An ON CONFLICT clause is used incorrectly or conflicts with a constraint definition."
tools: ["sqlite"]
error-types: ["constraint-error"]
severities: ["error"]
---


# [Solution] SQLite ON CONFLICT clause error

SQLite raises a **ON CONFLICT clause error** error when an on conflict clause is used incorrectly or conflicts with a constraint definition. This is one of the most common classes of errors encountered in SQLite databases.

## Common Causes

- ON CONFLICT references a constraint that does not exist.
- Multiple ON CONFLICT clauses on the same constraint.
- ON CONFLICT used in a context where it is not supported.

## How to Fix

### Verify the constraint name exists

```sql
SELECT name FROM sqlite_master WHERE type='constraint';
```

### Use a valid conflict target

```sql
INSERT INTO users (id, email) VALUES (1, 'a@b.com')
ON CONFLICT(email) DO UPDATE SET email = excluded.email;
```

### Check that the column has a UNIQUE or PRIMARY KEY constraint

```sql
CREATE UNIQUE INDEX idx_email ON users(email);
```

## Examples

```sql
INSERT INTO users (id, email) VALUES (1, 'a@b.com')
ON CONFLICT(nonexistent) DO UPDATE SET email = excluded.email;
-- Error: no such constraint: nonexistent
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
