---
title: "[Solution] ClickHouse Network Timeout Error"
description: "How to fix ClickHouse network timeout errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Network latency between client and server
- Server under heavy load
- Connection pool exhausted
- Firewall dropping idle connections

## How to Fix

Increase timeout:

```bash
clickhouse-client --connect_timeout=30 --receive_timeout=300
```

Check server load:

```sql
SELECT * FROM system.processes;
```

## Examples

```bash
clickhouse-client --connect_timeout=60 --send_timeout=60 --receive_timeout=60
```
