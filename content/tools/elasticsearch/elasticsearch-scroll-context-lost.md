---
title: "[Solution] Elasticsearch Scroll Context Lost Error"
description: "Fix Elasticsearch scroll context lost error. Resolve scroll context expiration issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Scroll Context Lost Error

The scroll context has expired or been cleared. Subsequent scroll requests fail.

## Common Causes

- Scroll context timed out (default 1m)
- Too many scroll contexts open
- Scroll not maintained with keep-alive

## How to Fix

### Solution 1

```bash
curl -X DELETE 'localhost:9200/_search/scroll/_all'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
