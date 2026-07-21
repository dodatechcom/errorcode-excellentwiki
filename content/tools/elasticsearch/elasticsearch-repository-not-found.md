---
title: "[Solution] Elasticsearch Repository Not Found Error"
description: "Fix Elasticsearch repository not found error. Resolve snapshot repository reference issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Repository Not Found Error

The snapshot repository does not exist. The repository was never created or was deleted.

## Common Causes

- Repository was never created
- Repository name is misspelled
- Repository was deleted

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_snapshot/_all'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
