---
title: "[Solution] Elasticsearch Index Read Only Error"
description: "Fix Elasticsearch index read only error. Resolve index read-only mode issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Index Read Only Error

The index is in read-only mode and rejects write operations. This happens when disk watermarks are exceeded.

## Common Causes

- Disk watermark exceeded triggers read-only block
- Index was manually set to read-only
- ILM set read-only phase

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_settings?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
