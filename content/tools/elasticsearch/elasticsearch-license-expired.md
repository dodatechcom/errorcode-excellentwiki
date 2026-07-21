---
title: "[Solution] Elasticsearch License Expired Error"
description: "Fix Elasticsearch license expired error. Resolve license expiration issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch License Expired Error

The Elasticsearch license has expired. Some features are no longer available.

## Common Causes

- License has expired
- License was not renewed
- Trial license expired

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_license'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
