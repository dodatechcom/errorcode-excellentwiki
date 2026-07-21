---
title: "[Solution] ClickHouse Named Collection Error"
description: "How to fix ClickHouse named collection configuration errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Named collection not defined
- Wrong collection name in query
- Required parameter missing from collection

## How to Fix

Create named collection:

```xml
<named_collections>
  <my_s3>
    <access_key_id>KEY</access_key_id>
    <secret_access_key>SECRET</secret_access_key>
  </my_s3>
</named_collections>
```

## Examples

```sql
SELECT * FROM system.named_collections;
```
