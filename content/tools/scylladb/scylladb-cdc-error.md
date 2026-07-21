---
title: "[Solution] ScyllaDB CDC Log Error"
description: "How to fix ScyllaDB Change Data Capture log errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- CDC table not created with CDC enabled
- CDC log table schema mismatch
- TTL on CDC log too short
- Too much CDC data overwhelming storage

## How to Fix

Enable CDC:

```cql
CREATE TABLE my_table (id UUID PRIMARY KEY, val TEXT) WITH cdc = {'enabled': true};
```

## Examples

```cql
DESCRIBE TABLE my_table_scylla_cdc_log;
SELECT * FROM my_table_scylla_cdc_log LIMIT 10;
```
