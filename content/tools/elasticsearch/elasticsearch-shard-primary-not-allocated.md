---
title: "[Solution] Elasticsearch Primary Shard Not Allocated Error"
description: "Fix Elasticsearch primary shard not allocated error. Resolve primary shard allocation issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Primary Shard Not Allocated Error

A primary shard cannot be allocated. The index is unavailable for indexing until the primary is restored.

## Common Causes

- All nodes with shard data are down
- Disk watermarks prevent allocation
- Shard allocation is disabled

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cluster/allocation/explain?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
