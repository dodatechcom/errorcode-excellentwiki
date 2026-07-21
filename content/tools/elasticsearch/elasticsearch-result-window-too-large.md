---
title: "[Solution] Elasticsearch Result Window Too Large Error"
description: "Fix Elasticsearch result window too large error. Resolve deep pagination limit issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Result Window Too Large Error

The search result window exceeds the max_result_window limit. Deep pagination is blocked.

## Common Causes

- from + size exceeds max_result_window (default 10000)
- Application paginates too deeply
- No search_after or scroll used

## How to Fix

### Solution 1

```bash
curl -X PUT 'localhost:9200/myindex/_settings' -H 'Content-Type: application/json' -d '{"index.max_result_window":20000}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
