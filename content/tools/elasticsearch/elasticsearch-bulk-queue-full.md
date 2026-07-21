---
title: "[Solution] Elasticsearch Bulk Queue Full Error"
description: "Fix Elasticsearch bulk queue full error. Resolve bulk indexing queue overflow issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Bulk Queue Full Error

The bulk indexing queue is full. Indexing requests are rejected or throttled.

## Common Causes

- Indexing rate exceeds bulk thread pool capacity
- Bulk queue size is too small
- Cluster is under heavy indexing load

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/thread_pool/bulk?v&h=node_name,queue,active,completed'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
