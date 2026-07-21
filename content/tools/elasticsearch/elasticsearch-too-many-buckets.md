---
title: "[Solution] Elasticsearch Too Many Buckets Error"
description: "Fix Elasticsearch too many buckets error. Resolve aggregation bucket limit issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Too Many Buckets Error

The aggregation generates more buckets than allowed. The request is rejected.

## Common Causes

- Terms agg on high-cardinality field
- Date histogram with very fine granularity
- Multiple nested aggs generate exponential buckets

## How to Fix

### Solution 1

```bash
curl -X PUT 'localhost:9200/_cluster/settings' -H 'Content-Type: application/json' -d '{"transient":{"search.max_buckets":20000}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
