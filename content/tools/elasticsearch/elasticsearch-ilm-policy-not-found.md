---
title: "[Solution] Elasticsearch ILM Policy Not Found Error"
description: "Fix Elasticsearch ILM policy not found error. Resolve index lifecycle management issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch ILM Policy Not Found Error

The ILM policy does not exist. Indices cannot follow a lifecycle without a valid policy.

## Common Causes

- ILM policy was never created
- Policy name is misspelled
- Policy was deleted

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/_ilm/policy?pretty'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
