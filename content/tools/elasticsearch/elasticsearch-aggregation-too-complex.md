---
title: "[Solution] Elasticsearch Aggregation Too Complex Error"
description: "Fix Elasticsearch aggregation too complex error. Resolve aggregation performance and resource issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Aggregation Too Complex Error

The aggregation is too complex or uses too many resources. It may time out or cause memory pressure.

## Common Causes

- Aggregation has too many nested levels
- Terms agg has too many buckets
- Aggregation uses high-cardinality fields

## How to Fix

### Solution 1

```bash
curl -X PUT 'localhost:9200/_cluster/settings' -H 'Content-Type: application/json' -d '{"transient":{"search.max_buckets":10000}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
