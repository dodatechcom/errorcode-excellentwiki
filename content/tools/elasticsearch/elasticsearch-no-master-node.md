---
title: "[Solution] Elasticsearch No Master Node Error"
description: "Fix Elasticsearch no master node error. Resolve master node election failures."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch No Master Node Error

The cluster cannot elect or maintain a master node. The cluster enters a RED state and cannot serve requests.

## Common Causes

- All master-eligible nodes are down
- Network partition prevents election
- Insufficient master-eligible nodes

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/master?v'
```

### Solution 2

```bash
curl -X GET 'localhost:9200/_cat/nodes?v&h=name,master,ip'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
