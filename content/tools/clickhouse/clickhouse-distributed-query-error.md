---
title: "[Solution] ClickHouse Distributed Query Error"
description: "Fix ClickHouse distributed query errors when cross-shard queries fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Distributed Query Error

Distributed query errors occur when ClickHouse cannot execute queries across multiple shards.

## Common Causes

- Shard node unreachable
- Timeout on cross-shard data transfer
- Memory limit exceeded during merge of partial results
- Incompatible data types across shards

## How to Fix

Check cluster status:

```sql
SELECT * FROM system.clusters WHERE cluster = 'my_cluster';
```

Test shard connectivity:

```bash
clickhouse-client -h shard2 --query "SELECT 1"
```

Increase distributed query timeout:

```sql
SET receive_timeout = 120;
SELECT * FROM distributed_table;
```

## Examples

```sql
SELECT shardNum(), hostName(), count() FROM distributed_table GROUP BY shardNum(), hostName();
```
