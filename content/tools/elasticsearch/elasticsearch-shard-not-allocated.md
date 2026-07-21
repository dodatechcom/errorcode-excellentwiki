---
title: "[Solution] Elasticsearch Shard Not Allocated Error"
description: "Fix Elasticsearch shard not allocated error. Resolve shard allocation failures."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Shard Not Allocated Error

A shard cannot be allocated to any node in the cluster. The shard remains in unassigned state.

## Common Causes

- All nodes exceed disk watermark
- Shard allocation is disabled
- No node satisfies allocation filters

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cluster/allocation/explain?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
