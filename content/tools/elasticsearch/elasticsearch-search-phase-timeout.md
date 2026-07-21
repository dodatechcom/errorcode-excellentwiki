---
title: "[Solution] Elasticsearch Search Phase Execution Timeout"
description: "Fix Elasticsearch search phase execution timeout errors. Resolve slow query phases causing timeouts."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Search Phase Execution Timeout

Elasticsearch search phase execution timeout occurs when a search operation exceeds the allowed time limit during a specific phase such as fetch or query.

## Common Causes

- Complex aggregation queries scanning too many documents
- Slow disk I/O on data nodes during heavy search load
- Large result sets requiring excessive fetch operations
- Unoptimized mappings causing fielddata explosion

## Common Error Messages

- `search_phase_execution_exception`
- `query_phase_execution_exception`
- `fetch_phase_execution_exception`

## How to Fix It

### Solution 1: Increase timeout for critical queries

Set a higher timeout on the specific search request:

```bash
curl -X GET "localhost:9200/myindex/_search?timeout=60s" -H 'Content-Type: application/json' -d '{
  "query": { "match_all": {} },
  "size": 100
}'
```

### Solution 2: Use scroll or search_after for large results

Avoid deep pagination with scroll:

```bash
curl -X GET "localhost:9200/myindex/_search?scroll=2m" -H 'Content-Type: application/json' -d '{
  "size": 100,
  "query": { "match_all": {} }
}'
```

### Solution 3: Optimize field mappings

Disable fielddata on text fields and use keyword instead:

```bash
curl -X PUT "localhost:9200/myindex/_mapping" -H 'Content-Type: application/json' -d '{
  "properties": {
    "message": {
      "type": "text",
      "fielddata": false
    }
  }
}'
```

## Prevent It

- Use index aliases to target specific time ranges
- Limit aggregation bucket counts
- Profile slow queries with the `_profile` API
