---
title: "[Solution] ClickHouse Concurrent Insert Error"
description: "Fix ClickHouse concurrent insert errors when parallel INSERT operations conflict"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Concurrent Insert Error

Concurrent insert errors occur when multiple simultaneous INSERT operations create conflicts.

## Common Causes

- Too many parallel inserts creating too many parts
- Insert timeout exceeded under concurrent load
- Concurrent inserts exceeding max_concurrent_queries
- Concurrent inserts to same partition overwhelming merge

## How to Fix

Check concurrent inserts:

```sql
SELECT query, elapsed FROM system.processes WHERE query LIKE 'INSERT%';
```

Batch inserts in application:

```python
batch = []
for row in data:
    batch.append(row)
    if len(batch) >= 10000:
        client.execute("INSERT INTO my_table VALUES", batch)
        batch = []
if batch:
    client.execute("INSERT INTO my_table VALUES", batch)
```

Limit concurrent queries:

```xml
<max_concurrent_queries>100</max_concurrent_queries>
```

## Examples

```sql
SELECT count() FROM system.processes WHERE query LIKE 'INSERT%';
```
