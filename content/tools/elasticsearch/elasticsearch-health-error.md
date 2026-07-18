---
title: "[Solution] Elasticsearch Cluster Health Error"
description: "Fix Elasticsearch cluster health errors. Learn why this happens and how to resolve it quickly."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Elasticsearch Cluster Health Error

Elasticsearch cluster health errors occur when the cluster cannot reach a healthy state.

## Why This Happens

- Red status
- Yellow status
- Master not elected
- Nodes disconnected

## Common Error Messages

- `health_red`
- `health_yellow`
- `health_no_master`
- `health_nodes_disconnected`

## How to Fix It

### Solution 1: Check health status

View cluster health:

```bash
curl -X GET "localhost:9200/_cluster/health?pretty"
```

### Solution 2: Fix red status

Check for unassigned primary shards:

```bash
curl -X GET "localhost:9200/_cat/shards?v&h=index,shard,prirep,state"
```

### Solution 3: Fix yellow status

Allocate unassigned replica shards.


## Common Scenarios

- **Cluster is red:** Check for missing primary shards.
- **Cluster is yellow:** Allocate replica shards.

## Prevent It

- Monitor cluster health
- Set up alerting
- Plan capacity
