---
title: "[Solution] Elasticsearch Shard Error"
description: "Fix Elasticsearch shard errors. Learn why this happens and how to resolve it quickly."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Elasticsearch Shard Error

Elasticsearch shard errors occur when shards fail to allocate, are unassigned, or have corruption issues.

## Why This Happens

- Unassigned shards
- Shard allocation failed
- Shard corruption
- Too many shards

## Common Error Messages

- `shard_unassigned`
- `shard_allocation_failed`
- `shard_corruption`
- `shard_limit_error`

## How to Fix It

### Solution 1: Check shard status

View unassigned shards:

```bash
curl -X GET "localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason"
```

### Solution 2: Allocate shards

Manually allocate:

```bash
curl -X POST "localhost:9200/_cluster/reroute" \
  -d '{"commands":[{"allocate_replica":{"index":"myindex","shard":0,"node":"node-1"}}]}'
```

### Solution 3: Reduce shard count

Use fewer shards per index:

```yaml
settings:
  number_of_shards: 1
```


## Common Scenarios

- **Shard unassigned:** Check node capacity and disk watermarks.
- **Too many shards:** Reduce shards or add nodes.

## Prevent It

- Monitor shard allocation
- Set disk watermarks
- Plan capacity
