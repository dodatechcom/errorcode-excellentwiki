---
title: "[Solution] Elasticsearch Role Not Found Error"
description: "Fix Elasticsearch role not found error. Resolve role configuration issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Role Not Found Error

The specified role does not exist. The role was never created or was deleted.

## Common Causes

- Role was never created
- Role was deleted
- Role name is misspelled

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_security/role/myrole'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
