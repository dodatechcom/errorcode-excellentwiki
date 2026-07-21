---
title: "PostgreSQL Superuser Required Error"
description: "Operation requires superuser privileges that current role does not have"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL Superuser Required Error

Operation requires superuser privileges that current role does not have

## Common Causes

- Attempting administrative operation without superuser
- Role created without SUPERUSER attribute
- Extension installation requires superuser
- pg_hba.conf not allowing superuser connection method

## How to Fix

1. Connect as postgres superuser: `psql -U postgres`
2. Grant superuser: `ALTER USER myuser WITH SUPERUSER;`
3. Use pg_hba.conf to allow trust/local for postgres user
4. Consider using pg_monitor role for read-only monitoring

## Examples

```sql
-- Grant superuser to a role
ALTER USER myadmin WITH SUPERUSER;

-- Check role attributes
SELECT rolname, rolsuper, rolcreaterole FROM pg_roles;
```
