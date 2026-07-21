---
title: "[Solution] ScyllaDB Permission Denied Error"
description: "How to fix ScyllaDB permission denied errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Role lacks required permission
- Grant not applied
- Superuser required for operation

## How to Fix

Grant permissions:

```cql
GRANT ALL ON KEYSPACE my_keyspace TO my_role;
GRANT SELECT, INSERT ON my_keyspace.my_table TO my_role;
```

## Examples

```cql
LIST ALL PERMISSIONS OF my_role;
SHOW GRANTS FOR my_role;
```
