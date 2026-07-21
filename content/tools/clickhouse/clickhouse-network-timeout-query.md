---
title: "[Solution] ClickHouse Network Timeout During Query"
description: "How to fix ClickHouse query network timeout errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Query remote table takes too long
- Distributed query across slow network
- Connection pool timeout

## How to Fix

Increase timeouts:

```sql
SET max_execution_time = 600;
SET receive_timeout = 600;
```

## Examples

```bash
clickhouse-client --receive_timeout=600 --send_timeout=600
```
