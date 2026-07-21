---
title: "[Solution] Elasticsearch Cluster Health Red Error"
description: "Fix Elasticsearch cluster health red error. Resolve critical cluster health issues where primary shards are unassigned."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Cluster Health Red Error

The cluster health is RED, meaning one or more primary shards are unassigned. This indicates data loss or unavailable indices.

## Common Causes

- Primary shards cannot be assigned to any node
- A node holding primary shards has left the cluster
- Disk watermark has been exceeded

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cluster/health?pretty'
```

### Solution 2

```bash
curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
