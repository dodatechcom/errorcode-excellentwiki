---
title: "[Solution] ScyllaDB User Defined Function Error"
description: "How to fix ScyllaDB UDF errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- UDF language not enabled
- Invalid function body
- Return type mismatch
- UDF crashes during execution

## How to Fix

Enable UDF:

```yaml
enable_user_defined_functions: true
```

Create UDF:

```cql
CREATE FUNCTION my_add(a INT, b INT) RETURNS NULL ON NULL INPUT RETURNS INT LANGUAGE lua AS 'return a + b;';
```

## Examples

```cql
SELECT * FROM system_schema.functions;
DROP FUNCTION IF EXISTS my_add(INT, INT);
```
