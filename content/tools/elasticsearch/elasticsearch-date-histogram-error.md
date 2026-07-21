---
title: "[Solution] Elasticsearch Date Histogram Error"
description: "Fix Elasticsearch date histogram error. Resolve date histogram aggregation issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Date Histogram Error

The date histogram aggregation fails. The field is not a date type, or the interval is invalid.

## Common Causes

- Field is not mapped as date type
- Interval is missing
- Timezone setting is invalid

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{"size":0,"aggs":{"over_time":{"date_histogram":{"field":"@timestamp","calendar_interval":"day"}}}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
