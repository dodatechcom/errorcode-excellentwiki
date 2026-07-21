---
title: "[Solution] ClickHouse RBAC Error"
description: "How to fix ClickHouse role-based access control configuration errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Circular role dependencies
- Role granted to wrong user
- Attached policies conflicting
- Settings profile override

## How to Fix

Check roles:

```sql
SELECT * FROM system.roles;
SELECT * FROM system.role_grants;
```

## Examples

```sql
SELECT * FROM system.roles;
SELECT * FROM system.grants WHERE user_name = 'my_user';
```
