---
title: "[Solution] Elasticsearch Node Left Cluster Error"
description: "Fix Elasticsearch node left cluster error. Resolve node departure and recovery issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Node Left Cluster Error

A node has left the cluster, leaving shards unassigned and cluster health degraded.

## Common Causes

- Node crashed or was shut down ungracefully
- Network issue caused disconnect
- Node was removed via API

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/nodes?v'
```

### Solution 2

```bash
curl -X GET 'localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
