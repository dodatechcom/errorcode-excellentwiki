---
title: "[Solution] ScyllaDB CQL Parse Error"
description: "How to fix ScyllaDB CQL query syntax errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CQL keyword used as identifier without quoting
- Missing semicolon
- Wrong data type literal
- Reserved word in column name

## How to Fix

Quote reserved words:

```cql
SELECT "user" FROM my_table;
SELECT * FROM my_table WHERE "user" = 'admin';
```

## Examples

```cql
DESCRIBE TABLE my_table;
SELECT column_name, type FROM system_schema.columns WHERE table_name = 'my_table';
```
