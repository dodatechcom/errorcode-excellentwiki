---
title: "[Solution] Elasticsearch Remote Cluster Not Connected Error"
description: "Fix Elasticsearch remote cluster not connected error. Resolve remote cluster connectivity issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Remote Cluster Not Connected Error

The remote cluster connection is not established. Nodes cannot communicate across clusters.

## Common Causes

- Remote seed nodes are unreachable
- Firewall blocks connection
- Cluster credentials are invalid

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_remote/info?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
