---
title: "[Solution] Elasticsearch Replica Shard Not Allocated Error"
description: "Fix Elasticsearch replica shard not allocated error. Resolve replica allocation failures."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Replica Shard Not Allocated Error

A replica shard cannot be allocated. The index works but is at risk of data loss if the primary fails.

## Common Causes

- Not enough data nodes for replicas
- Disk watermarks prevent allocation
- Allocation filtering excludes nodes

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
