---
title: "[Solution] Elasticsearch Frozen Data Node Error"
description: "Fix Elasticsearch frozen data node error. Resolve frozen tier node issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Frozen Data Node Error

Data cannot be moved to the frozen tier. The frozen tier nodes are unavailable or misconfigured.

## Common Causes

- Frozen tier nodes are not available
- ILM frozen phase not configured
- Searchable snapshots not configured

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/nodes?v&h=name,node.role'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
