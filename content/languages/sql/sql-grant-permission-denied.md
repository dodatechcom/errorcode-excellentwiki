---
title: "SQL GRANT Permission Denied Error"
description: "Fix SQL GRANT and permission denied errors when user lacks privileges for database operations."
languages: ["sql"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- User does not have SELECT privilege on the target table
- GRANT issued by user without GRANT OPTION
- Role-based permissions not assigned to the user
- Schema-level permissions missing for object creation
- Table-level permissions do not cascade to columns

## How to Fix

```sql
-- WRONG: Running query without permission
SELECT * FROM restricted_table;
-- ERROR: permission denied for table restricted_table

-- CORRECT: Request GRANT from table owner
GRANT SELECT ON restricted_table TO app_user;
```

```sql
-- WRONG: GRANT without admin privileges
GRANT SELECT ON hr.salary_table TO analyst_user;
-- ERROR: must be owner or superuser

-- CORRECT: Ask DBA to grant permissions
-- Or use role-based access
GRANT analyst_role TO analyst_user;
```

## Examples

```sql
-- Example 1: Grant SELECT to a user
GRANT SELECT ON customers TO report_user;

-- Example 2: Grant to role
CREATE ROLE read_only;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_only;
GRANT read_only TO analyst1, analyst2;

-- Example 3: Revoke permissions
REVOKE INSERT, UPDATE, DELETE ON audit_log FROM app_user;
-- app_user can now only SELECT from audit_log
```

## Related Errors

- [Access denied error](sql-access-denied) -- permission failures
- [SQL access denied](sql-access-denied-v2) -- access control issues
