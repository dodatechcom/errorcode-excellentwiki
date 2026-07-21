---
title: "[Solution] ScyllaDB Role Not Found Error"
description: "How to fix ScyllaDB role not found errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Role name wrong
- Role not created
- Role in different authentication backend

## How to Fix

List roles:

```cql
SELECT * FROM system_auth.roles;
```

Create role:

```cql
CREATE ROLE my_role WITH PASSWORD = 'secret' AND LOGIN = true;
```

## Examples

```cql
SELECT role FROM system_auth.roles;
GRANT SELECT ON my_keyspace.my_table TO my_role;
```
