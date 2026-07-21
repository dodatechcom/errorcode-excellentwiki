---
title: "[Solution] Elasticsearch Request Cache Disabled Error"
description: "Fix Elasticsearch request cache disabled error. Resolve search caching issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Request Cache Disabled Error

The request cache is disabled and searches are not cached. This impacts performance for repeated queries.

## Common Causes

- Cache is disabled at index or node level
- Query uses cache-busting features
- Cache was invalidated by writes

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_nodes/stats/indices.request_cache?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
