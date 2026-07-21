---
title: "[Solution] Elasticsearch Completion Suggest Error"
description: "Fix Elasticsearch completion suggest error. Resolve completion suggestion issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Completion Suggest Error

The completion suggester fails. The completion field is not mapped or the query is incorrect.

## Common Causes

- Completion field is not mapped as completion type
- Suggestions are too expensive
- Fuzzy edits are too many

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{"suggest":{"name-suggest":{"prefix":"ela","completion":{"field":"suggest","size":5}}}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
