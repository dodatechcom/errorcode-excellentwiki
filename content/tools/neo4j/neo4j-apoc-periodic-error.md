---
title: "[Solution] Neo4j APOC Periodic Error"
description: "How to fix Neo4j APOC periodic iteration errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Batch size too large
- APOC not installed
- Transaction timeout during iteration

## How to Fix

```cypher
CALL apoc.periodic.iterate('MATCH (n:Person) RETURN n', 'SET n.processed = true', {batchSize: 1000})
```

## Examples

```cypher
CALL apoc.periodic.list()
```
