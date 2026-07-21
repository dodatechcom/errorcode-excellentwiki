---
title: "[Solution] ClickHouse Too Many Connections Error"
description: "Fix ClickHouse too many connections errors when server connection limit is reached"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Too Many Connections Error

Too many connections errors occur when ClickHouse rejects new connections due to max_concurrent_queries limit.

## Common Causes

- Application not closing connections properly
- Connection pool size too large
- Too many distributed queries running
- Long-running queries holding connections

## How to Fix

Check current connections:

```sql
SELECT count() FROM system.processes;
```

Check connection limit:

```sql
SELECT value FROM system.settings WHERE name = 'max_concurrent_queries';
```

Increase limit:

```xml
<max_concurrent_queries>200</max_concurrent_queries>
```

Monitor connection usage:

```sql
SELECT user, count() FROM system.processes GROUP BY user ORDER BY count() DESC;
```

## Examples

```sql
SELECT query, elapsed, user FROM system.processes WHERE elapsed > 30;
```
