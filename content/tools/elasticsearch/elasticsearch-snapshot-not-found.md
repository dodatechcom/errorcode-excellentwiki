---
title: "[Solution] Elasticsearch Snapshot Not Found Error"
description: "Fix Elasticsearch snapshot not found error. Resolve snapshot reference issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Snapshot Not Found Error

The requested snapshot does not exist. The snapshot may have been deleted or the name is wrong.

## Common Causes

- Snapshot was deleted by retention policy
- Snapshot name is misspelled
- Repository does not contain snapshot

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_snapshot/myrepo/_all?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
