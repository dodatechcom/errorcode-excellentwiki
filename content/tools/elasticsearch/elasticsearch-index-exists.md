---
title: "[Solution] Elasticsearch Index Already Exists Error"
description: "Fix Elasticsearch index already exists error. Resolve index creation conflicts."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Index Already Exists Error

The index already exists when trying to create it with create index API.

## Common Causes

- Index was already created
- Auto-creation created it first
- Name conflict with data stream

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/indices?v&s=index:asc'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
