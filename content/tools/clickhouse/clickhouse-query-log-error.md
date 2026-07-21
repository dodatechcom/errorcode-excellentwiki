---
title: "[Solution] ClickHouse Query Log Error"
description: "Fix ClickHouse query log errors when system.query_log has missing or incomplete entries"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Query Log Error

Query log errors occur when ClickHouse query logging fails or produces incomplete records.

## Common Causes

- Query log table not created
- Query log retention too short
- Logging disabled in server config
- Query log disk full

## How to Fix

Check query log:

```sql
SELECT count(), min(event_time), max(event_time) FROM system.query_log;
```

Check logging config:

```xml
<query_log>
    <database>system</database>
    <table>query_log</table>
    <flush_interval_milliseconds>7500</flush_interval_milliseconds>
</query_log>
```

Query recent errors:

```sql
SELECT query, exception, event_time FROM system.query_log
WHERE type = 'ExceptionWhileProcessing' ORDER BY event_time DESC LIMIT 10;
```

## Examples

```sql
SELECT query, type, event_time FROM system.query_log
WHERE query LIKE '%INSERT%' ORDER BY event_time DESC LIMIT 5;
```
