---
title: "[Solution] Elasticsearch Query Timeout Error"
description: "Fix Elasticsearch query timeout error. Resolve search timeout issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Query Timeout Error

The search query times out before completing. The query is too complex or the cluster is overloaded.

## Common Causes

- Query is too complex
- Cluster is under heavy load
- Timeout is set too low

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_search?timeout=30s' -H 'Content-Type: application/json' -d '{"query":{"match_all":{}}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
