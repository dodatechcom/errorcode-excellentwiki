---
title: "[Solution] ClickHouse RBAC Error"
description: "Fix ClickHouse role-based access control errors when permission grants fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse RBAC Error

RBAC errors occur when role-based access control operations encounter permission issues.

## Common Causes

- User does not have required role
- Role grant chain too deep
- Revoked role still cached in session
- Table-level grant conflicts with database-level

## How to Fix

Check user roles:

```sql
SHOW GRANTS FOR myuser;
```

Grant role:

```sql
GRANT my_role TO myuser;
```

Check effective grants:

```sql
SELECT * FROM system.grants WHERE user = 'myuser';
```

## Examples

```sql
CREATE ROLE analyst;
GRANT SELECT ON mydb.* TO analyst;
GRANT analyst TO myuser;
```
