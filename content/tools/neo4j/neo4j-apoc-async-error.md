---
title: "[Solution] Neo4j APOC Async Error"
description: "How to fix Neo4j APOC async procedure errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Async task queue full
- Task timed out
- Callback function error

## How to Fix

```cypher
CALL apoc.periodic.iterate('MATCH (n:Person) RETURN n', 'DETACH DELETE n', {async: true})
```

## Examples

```cypher
CALL apoc.periodic.list()
```
