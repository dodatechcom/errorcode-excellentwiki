---
title: "[Solution] Elasticsearch Shard Failed Error"
description: "Fix Elasticsearch shard failed error. Resolve shard corruption and recovery issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Shard Failed Error

A shard fails during indexing, search, or recovery. The shard may be corrupted or experiencing I/O errors.

## Common Causes

- Disk corruption on shard data path
- I/O errors reading segments
- JVM crashes during shard operations

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
