---
title: "[Solution] Elasticsearch Snapshot In Progress Error"
description: "Fix Elasticsearch snapshot in progress error. Resolve concurrent snapshot operation issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Snapshot In Progress Error

A snapshot operation is already in progress. Concurrent snapshot operations are not allowed.

## Common Causes

- Previous snapshot not completed
- Snapshot restore is in progress
- Delete waiting for snapshot

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_snapshot/myrepo/_status?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
