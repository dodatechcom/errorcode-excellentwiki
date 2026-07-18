---
title: "[Solution] Elasticsearch Cluster Error"
description: "Fix Elasticsearch cluster errors. Learn why this happens and how to resolve it quickly."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Elasticsearch Cluster Error

Elasticsearch cluster errors occur when nodes cannot form a cluster or the cluster health is degraded.

## Why This Happens

- Red cluster health
- Yellow cluster health
- Master node down
- Split brain

## Common Error Messages

- `cluster_red`
- `cluster_yellow`
- `master_not_discovered`
- `split_brain`

## How to Fix It

### Solution 1: Check cluster health

Use the Cluster API:

```bash
curl -X GET "localhost:9200/_cluster/health?pretty"
```

### Solution 2: Fix yellow health

Allocate unassigned shards:

```bash
curl -X POST "localhost:9200/_cluster/reroute" \
  -H 'Content-Type: application/json' \
  -d '{"commands":[{"allocate_stale_primary":{"index":"myindex","shard":0,"node":"node-1","accept_data_loss":true}}]}'
```

### Solution 3: Resolve master issues

Check master-eligible nodes:

```bash
curl -X GET "localhost:9200/_cat/master?v"
```


## Common Scenarios

- **Cluster is red:** Check for unassigned primary shards.
- **Cluster is yellow:** Allocate unassigned replica shards.

## Prevent It

- Monitor cluster health
- Set up alerting
- Plan node capacity
