---
title: "[Solution] ClickHouse Cluster Not Found Error"
description: "How to fix ClickHouse cluster not found errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Cluster name wrong in config
- Cluster not defined in remote_servers
- Node not part of cluster

## How to Fix

Check clusters:

```sql
SELECT * FROM system.clusters;
```

## Examples

```sql
SELECT cluster, shard_num, host_name, port FROM system.clusters;
```
