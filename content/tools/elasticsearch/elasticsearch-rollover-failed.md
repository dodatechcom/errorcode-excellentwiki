---
title: "[Solution] Elasticsearch Rollover Failed Error"
description: "Fix Elasticsearch rollover failed error. Resolve ILM rollover issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Rollover Failed Error

The ILM rollover action fails. The write alias is missing or the rollover conditions are not met.

## Common Causes

- Index does not have a write alias
- Rollover conditions not met
- Index is not in hot phase

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_ilm/explain?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
