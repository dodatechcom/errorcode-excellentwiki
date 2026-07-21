---
title: "[Solution] Elasticsearch Fielddata Disabled Error"
description: "Fix Elasticsearch fielddata disabled error. Resolve fielddata usage on text fields."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Fielddata Disabled Error

Fielddata is disabled for text fields. Aggregations and sorting on text fields require fielddata to be enabled.

## Common Causes

- Attempting to aggregate on a text field
- Attempting to sort on a text field
- Fielddata is disabled by default on text

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_mapping?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
