---
title: "[Solution] Elasticsearch Terms Bucket Overflow Error"
description: "Fix Elasticsearch terms bucket overflow error. Resolve terms aggregation bucket limit."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Terms Bucket Overflow Error

The terms aggregation exceeds the bucket limit. Too many unique terms are generated.

## Common Causes

- High-cardinality field used in terms agg
- No size parameter to limit buckets
- Aggregation is not filtered enough

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{"size":0,"aggs":{"top_values":{"terms":{"field":"status.keyword","size":100}}}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
