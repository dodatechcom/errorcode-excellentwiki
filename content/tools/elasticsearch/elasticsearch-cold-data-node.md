---
title: "[Solution] Elasticsearch Cold Data Node Error"
description: "Fix Elasticsearch cold data node error. Resolve cold tier node issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Cold Data Node Error

Data cannot be moved to the cold tier. The cold tier nodes are unavailable or misconfigured.

## Common Causes

- Cold tier nodes are not available
- ILM cold phase not configured
- Node roles do not include data_cold

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/nodes?v&h=name,node.role,attr'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
