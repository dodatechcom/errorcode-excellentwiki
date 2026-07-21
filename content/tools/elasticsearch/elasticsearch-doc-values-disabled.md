---
title: "[Solution] Elasticsearch Doc Values Disabled Error"
description: "Fix Elasticsearch doc values disabled error. Resolve doc_values usage issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Doc Values Disabled Error

Doc values are disabled for a field. Aggregations and sorting on this field require doc values.

## Common Causes

- Field was mapped with doc_values: false
- Text fields do not support doc values
- Field type does not support doc values

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_mapping?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
