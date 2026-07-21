---
title: "[Solution] Elasticsearch Cross Cluster Search Error"
description: "Fix Elasticsearch cross-cluster search error. Resolve CCS configuration issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Cross Cluster Search Error

Cross-cluster search fails. The remote cluster is not connected or the index name is wrong.

## Common Causes

- Remote cluster is not configured
- Remote connection timed out
- Index pattern does not match

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_remote/info?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
