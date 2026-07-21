---
title: "SQL VIEW Referenced Table Dropped Error"
description: "Fix SQL VIEW errors when a referenced table has been dropped or altered making the view definition invalid."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Base table was dropped but view still references it
- Column referenced by view was dropped from base table
- View uses WITH CHECK OPTION that conflicts with new data
- View definition uses deprecated syntax
- View depends on another view that was dropped (cascading)

## How to Fix

```sql
-- WRONG: Table dropped but view exists
CREATE VIEW active_users AS
SELECT * FROM users WHERE status = 'active';
-- Later: DROP TABLE users;
SELECT * FROM active_users;
-- ERROR: table 'users' does not exist

-- CORRECT: Recreate view or restore table
CREATE VIEW active_users AS
SELECT * FROM new_users WHERE status = 'active';
```

```sql
-- WRONG: Column dropped from base table
CREATE VIEW user_summary AS
SELECT id, name, email, phone FROM users;
-- Later: ALTER TABLE users DROP COLUMN phone;
SELECT * FROM user_summary;
-- ERROR: column 'phone' does not exist

-- CORRECT: Recreate view without dropped column
CREATE VIEW user_summary AS
SELECT id, name, email FROM users;
```

## Examples

```sql
-- Example 1: Check view validity (PostgreSQL)
SELECT * FROM information_schema.views
WHERE table_schema = 'public';

-- Example 2: Recreate view with OR REPLACE
CREATE OR REPLACE VIEW active_customers AS
SELECT id, name, email
FROM customers
WHERE status = 'active';

-- Example 3: Drop and recreate dependent view
DROP VIEW IF EXISTS customer_report;
CREATE VIEW customer_report AS
SELECT c.name, o.total
FROM customers c
JOIN (SELECT customer_id, SUM(amount) AS total
      FROM orders GROUP BY customer_id) o ON c.id = o.customer_id;
```

## Related Errors

- [View error](sql-view-error) -- VIEW definition issues
- [SQL view error](sql-view-error-v2) -- view-related failures
