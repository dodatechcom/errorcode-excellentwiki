---
title: "[Solution] ScyllaDB Secondary Index Error"
description: "How to fix ScyllaDB secondary index errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Index on high cardinality column
- Index query not using index
- Index creation on large table taking too long

## How to Fix

Create index:

```cql
CREATE INDEX my_idx ON my_table (val);
```

## Examples

```cql
SELECT * FROM my_table WHERE val = 'search';
SELECT * FROM system_schema.indexes WHERE table_name = 'my_table';
```
