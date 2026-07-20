---
title: "[Solution] Default Constraint Error"
description: "Fix 'Default constraint error' when a DEFAULT value cannot be applied to a column."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "constraint, default"]
severity: "error"
---

# Default Constraint Error

## Error Message

```
ERROR 1364: Field 'X' doesn't have a default value — No DEFAULT is defined for a NOT NULL column that is omitted from the INSERT.
```

## Common Causes

- INSERT statement omits a NOT NULL column and no DEFAULT is defined
- DEFAULT value expression references a column or function that does not exist
- Data type of the DEFAULT value does not match the column's data type
- Strict SQL mode (STRICT_TRANS_TABLES) rejects missing values that would normally be auto-filled

## Solutions

### Solution 1: Add a DEFAULT constraint to the column

Define a default value so the database can fill it in automatically when the column is omitted.

```sql
-- Add a DEFAULT value
ALTER TABLE users
ALTER COLUMN status SET DEFAULT 'active';

-- MySQL: set default
ALTER TABLE users
ALTER COLUMN status SET DEFAULT 'active';

-- SQL Server: add named default
ALTER TABLE users
ADD CONSTRAINT DF_users_status DEFAULT 'active' FOR status;

-- PostgreSQL: add default with expression
ALTER TABLE users
ALTER COLUMN created_at SET DEFAULT CURRENT_TIMESTAMP;
```

### Solution 2: Provide the value explicitly in the INSERT

Include all NOT NULL columns without defaults in your INSERT statement.

```sql
-- Wrong: omitting a NOT NULL column with no default
INSERT INTO users (name) VALUES ('Alice');
-- ERROR 1364: Field 'email' doesn't have a default value

-- Correct: provide all required values
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Correct: use INSERT with column list
INSERT INTO users (name, email, status)
VALUES ('Alice', 'alice@example.com', 'active');
```

### Solution 3: Use dynamic defaults with expressions

Default values can use functions like CURRENT_TIMESTAMP or generate UUIDs.

```sql
-- MySQL: default with expression
ALTER TABLE users
ALTER COLUMN uuid SET DEFAULT (UUID());

ALTER TABLE audit_logs
ALTER COLUMN created_at SET DEFAULT CURRENT_TIMESTAMP;

-- PostgreSQL: default with expression
ALTER TABLE users
ALTER COLUMN uuid SET DEFAULT gen_random_uuid();

ALTER TABLE users
ALTER COLUMN search_name SET DEFAULT LOWER(name);

-- SQL Server: default with expression
ALTER TABLE users
ADD CONSTRAINT DF_users_uuid DEFAULT NEWID() FOR uuid;
```

## Prevention Tips

- Define DEFAULT values for all NOT NULL columns that may be omitted during INSERT operations
- Use DEFAULT expressions for columns like timestamps and UUIDs to reduce application logic
- Check your database's SQL mode — strict modes require all NOT NULL columns to have values or defaults

## Related Errors

- [Not Null Constraint]({{< relref "/languages/sql/not-null-constraint.md" >}})
- [Check Constraint Violation]({{< relref "/languages/sql/check-constraint-violation.md" >}})
- [Auto Increment Error]({{< relref "/languages/sql/auto-increment-error.md" >}})
