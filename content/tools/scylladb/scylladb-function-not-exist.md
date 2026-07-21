---
title: "[Solution] ScyllaDB Function Does Not Exist Error"
description: "How to fix ScyllaDB function not found errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Function name misspelled
- Argument types do not match
- Function in different keyspace

## How to Fix

List functions:

```cql
SELECT * FROM system_schema.functions WHERE keyspace_name = 'my_keyspace';
```

## Examples

```cql
SELECT function_name, argument_types FROM system_schema.functions;
```
