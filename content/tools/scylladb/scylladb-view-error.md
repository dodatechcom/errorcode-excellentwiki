---
title: "[Solution] ScyllaDB Materialized View Error"
description: "How to fix ScyllaDB materialized view errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- View creation fails with timeout
- View data not consistent with base table
- View causes write amplification

## How to Fix

```cql
CREATE MATERIALIZED VIEW myview AS SELECT * FROM mytable WHERE id IS NOT NULL PRIMARY KEY (id);
```

## Examples

```cql
SELECT * FROM system_schema.materialized_views WHERE keyspace_name = 'myks';
```
