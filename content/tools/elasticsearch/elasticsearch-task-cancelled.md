---
title: "[Solution] Elasticsearch Task Cancelled Error"
description: "Fix Elasticsearch task cancelled error. Resolve task cancellation and timeout issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Task Cancelled Error

A background task was cancelled. This may be due to timeout, manual cancellation, or resource constraints.

## Common Causes

- Task exceeded its timeout
- Task was manually cancelled
- Cluster is under resource pressure

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_tasks?detailed=true'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
