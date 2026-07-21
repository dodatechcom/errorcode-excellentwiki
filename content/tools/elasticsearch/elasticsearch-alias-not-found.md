---
title: "[Solution] Elasticsearch Alias Not Found Error"
description: "Fix Elasticsearch alias not found error. Resolve index alias reference issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Alias Not Found Error

The requested alias does not exist. The alias may have been removed or never created.

## Common Causes

- Alias was removed
- Alias name is misspelled
- Alias was never created

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/aliases?v'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
