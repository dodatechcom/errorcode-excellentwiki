---
title: "[Solution] Elasticsearch Update By Query Error"
description: "Fix Elasticsearch update by query error. Resolve update by query failure issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Update By Query Error

The update_by_query task fails. Some documents cannot be updated due to conflicts.

## Common Causes

- Documents modified by another process
- Script fails for some documents
- Index is read-only

## How to Fix

### Solution 1

```bash
curl -X POST 'localhost:9200/myindex/_update_by_query?conflicts=proceed' -H 'Content-Type: application/json' -d '{"query":{"match_all":{}}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
