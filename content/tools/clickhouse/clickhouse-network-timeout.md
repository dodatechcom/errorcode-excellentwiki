---
title: "[Solution] ClickHouse Network Timeout Error"
description: "Fix ClickHouse network timeout errors when distributed queries lose connectivity"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Network Timeout Error

Network timeout errors occur when ClickHouse distributed queries timeout waiting for remote shard responses.

## Common Causes

- Remote shard unreachable
- Network latency between ClickHouse nodes
- Query timeout too short for distributed operations
- DNS resolution slow for shard hostnames

## How to Fix

Check distributed table connections:

```sql
SELECT * FROM system.clusters;
```

Increase network timeout:

```sql
SET receive_timeout = 120, send_timeout = 120;
```

Test shard connectivity:

```bash
clickhouse-client -h shard2 --query "SELECT 1"
```

## Examples

```sql
SELECT * FROM system.clusters WHERE cluster = 'my_cluster';
```
