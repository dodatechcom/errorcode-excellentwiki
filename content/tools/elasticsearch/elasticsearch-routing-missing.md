---
title: "[Solution] Elasticsearch Routing Missing Error"
description: "Fix Elasticsearch routing missing error. Resolve routing parameter issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Routing Missing Error

The routing parameter is required but not provided. The document cannot be correctly routed to a shard.

## Common Causes

- Index requires routing but not provided
- Routing needed for parent/child
- _routing is mandatory in mapping

## How to Fix

### Solution 1

```bash
curl -X PUT 'localhost:9200/myindex/_doc/1?routing=user123' -H 'Content-Type: application/json' -d '{"field":"value"}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
