---
title: "[Solution] Elasticsearch Master Not Elected Error"
description: "Fix Elasticsearch master not elected error. Resolve master election timeout issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Master Not Elected Error

The master election process times out or fails. Nodes cannot agree on a master within the election timeout.

## Common Causes

- Election timeout is too low
- Nodes cannot communicate on transport port
- Cluster bootstrapping is incomplete

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_cat/nodes?v&h=name,master,ip'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
