---
title: "[Solution] SQL Syntax Error Near INSERT"
description: "Fix 'SQL syntax error near INSERT' when an INSERT statement is malformed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "syntax"]
severity: "error"
---

# SQL Syntax Error Near INSERT

## Error Message

```
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'INSERT ...'
```

## Common Causes

- Column count does not match the number of values provided
- Incorrect VALUES syntax such as missing parentheses or commas
- Using reserved keywords as column names without proper quoting
- Inserting into a VIEW that is not updatable

## Solutions

### Solution 1: Match column count with value count

Ensure the number of columns specified matches the number of values in the VALUES clause.

```sql
-- Wrong: 3 columns but only 2 values
INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com');

-- Correct: provide all values
INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 30);

-- Correct: specify only the columns you are inserting
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
```

### Solution 2: Use proper multi-row INSERT syntax

When inserting multiple rows, separate each row with a comma and enclose each row in parentheses.

```sql
-- Wrong: missing commas between rows
INSERT INTO users (name, email) VALUES ('Alice', 'a@ex.com') ('Bob', 'b@ex.com');

-- Correct
INSERT INTO users (name, email) VALUES
  ('Alice', 'alice@example.com'),
  ('Bob', 'bob@example.com'),
  ('Charlie', 'charlie@example.com');

-- Correct: use INSERT ... SELECT for bulk inserts
INSERT INTO users_backup (name, email)
SELECT name, email FROM users WHERE active = 1;
```

### Solution 3: Quote reserved words used as identifiers

If your table or column name is a SQL reserved word, wrap it in backticks, double quotes, or brackets.

```sql
-- Wrong: "order" is a reserved word
INSERT INTO orders (order, amount) VALUES (1, 100);

-- Correct (MySQL)
INSERT INTO `orders` (`order`, amount) VALUES (1, 100);

-- Correct (PostgreSQL)
INSERT INTO "orders" ("order", amount) VALUES (1, 100);

-- Correct (SQL Server)
INSERT INTO [orders] ([order], amount) VALUES (1, 100);
```

## Prevention Tips

- Always list columns explicitly in INSERT statements instead of relying on column order
- Use prepared statements in application code to avoid string concatenation errors in INSERT values
- Test INSERT statements with a SELECT to verify they reference valid data before executing

## Related Errors

- [Syntax Error Select]({{< relref "/languages/sql/syntax-error-select.md" >}})
- [Not Null Constraint]({{< relref "/languages/sql/not-null-constraint.md" >}})
- [Primary Key Violation]({{< relref "/languages/sql/primary-key-violation.md" >}})
