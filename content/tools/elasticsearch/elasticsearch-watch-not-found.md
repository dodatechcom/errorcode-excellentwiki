---
title: "[Solution] Elasticsearch Watch Not Found Error"
description: "Fix Elasticsearch watch not found error. Resolve watch reference issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Watch Not Found Error

The requested watch does not exist. The watch was deleted or the ID is wrong.

## Common Causes

- Watch was deleted
- Watch ID is misspelled
- Watch was never created

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_watcher/watch/my_watch?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
