---
title: "[Solution] Elasticsearch Cluster Health Yellow Error"
description: "Fix Elasticsearch cluster health yellow error. Resolve replica shard allocation issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Cluster Health Yellow Error

The cluster health is YELLOW, meaning all primary shards are allocated but some replica shards are not.

## Common Causes

- Not enough nodes for replicas
- Replica shards are unassigned due to disk watermarks
- A node recently left the cluster

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state&s=state:desc'
```

### Solution 2

```bash
curl -X POST 'localhost:9200/_cluster/reroute' -H 'Content-Type: application/json' -d '{"commands":[{"allocate_replica":{"index":"myindex","shard":0,"node":"node-1"}}]}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
