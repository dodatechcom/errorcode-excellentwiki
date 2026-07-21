---
title: "[Solution] Elasticsearch Shrink Index Error"
description: "Fix Elasticsearch shrink index error. Resolve index shrink operation issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Shrink Index Error

The shrink index operation fails. The source index is not read-only or has non-relocatable shards.

## Common Causes

- Source index is not read-only
- Source index has replicas
- Not enough disk space on target

## How to Fix

### Solution 1

```bash
curl -X POST 'localhost:9200/myindex/_shrink/myindex-shrunk' -H 'Content-Type: application/json' -d '{"settings":{"index.number_of_replicas":0,"index.number_of_shards":1,"index.blocks.write":true}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
