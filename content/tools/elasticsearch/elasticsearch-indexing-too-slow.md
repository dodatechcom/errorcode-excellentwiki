---
title: "[Solution] Elasticsearch Indexing Too Slow Error"
description: "Fix Elasticsearch indexing too slow error. Resolve slow indexing performance issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Indexing Too Slow Error

Indexing performance is degraded. Documents take too long to be indexed.

## Common Causes

- Too many segments need merging
- Refresh interval is too frequent
- Disk I/O is slow

## How to Fix

### Solution 1

```bash
curl -X PUT 'localhost:9200/myindex/_settings' -H 'Content-Type: application/json' -d '{"index.refresh_interval":"30s"}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
