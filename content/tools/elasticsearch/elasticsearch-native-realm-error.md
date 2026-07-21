---
title: "[Solution] Elasticsearch Native Realm Error"
description: "Fix Elasticsearch native realm error. Resolve native user store issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Native Realm Error

The native realm encounters errors. Users stored in Elasticsearch are not accessible.

## Common Causes

- Native realm is not enabled
- Users index is corrupted
- Security index is not available

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_security/_authenticate'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
