---
title: "[Solution] Elasticsearch Document Too Large Error"
description: "Fix Elasticsearch document too large error. Resolve document size limit issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Document Too Large Error

The document exceeds the maximum allowed size. The indexing request is rejected.

## Common Causes

- Document size exceeds http.max_content_length
- Document contains very large fields
- Bulk payload is too large

## How to Fix

### Solution 1

```bash
grep http.max_content_length /etc/elasticsearch/elasticsearch.yml
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
