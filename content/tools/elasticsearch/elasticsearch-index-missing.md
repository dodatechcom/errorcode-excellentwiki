---
title: "[Solution] Elasticsearch Index Missing Error"
description: "Fix Elasticsearch index missing error. Resolve missing or deleted index issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Index Missing Error

The requested index does not exist. It may have been deleted or the name is misspelled.

## Common Causes

- Index was deleted by retention policy or ILM
- Index name is misspelled
- Index was never created

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/indices?v&s=index:asc'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
