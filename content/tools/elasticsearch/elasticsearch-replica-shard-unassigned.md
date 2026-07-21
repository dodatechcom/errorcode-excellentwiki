---
title: "[Solution] Elasticsearch Replica Shard Unassigned Error"
description: "Fix Elasticsearch replica shard unassigned errors. Resolve cluster health yellow status from unassigned replicas."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Replica Shard Unassigned Error

Elasticsearch replica shard unassigned errors occur when replica shards cannot be allocated to any data node, causing the cluster health to remain yellow.

## Common Causes

- Insufficient data nodes to host replica shards
- Disk watermarks exceeded on all eligible nodes
- Shard allocation filtering rules blocking allocation
- Index marked as read-only

## Common Error Messages

- `shard_unassigned`
- `replica_not_allocated`
- `cluster_health_yellow`

## How to Fix It

### Solution 1: Check unassigned shards

Find which shards are unassigned and why:

```bash
curl -X GET "localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason" | grep UNASSIGNED
```

### Solution 2: Explain allocation decisions

Get detailed allocation explanation:

```bash
curl -X GET "localhost:9200/_cluster/allocation/explain?pretty"
```

### Solution 3: Reroute unassigned shards

Force Elasticsearch to re-evaluate allocation:

```bash
curl -X POST "localhost:9200/_cluster/reroute?retry_failed=true"
```

## Prevent It

- Maintain at least 3 data nodes for replication
- Monitor disk usage and watermark thresholds
- Review allocation filtering before applying
