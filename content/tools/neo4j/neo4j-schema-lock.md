---
title: "[Solution] Neo4j Schema Lock Error"
description: "How to fix Neo4j schema lock timeout errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Schema operation in progress
- Index creation holding schema lock
- Long-running schema migration

## How to Fix

Wait and retry:

```cypher
SHOW INDEXES;
```

## Examples

```cypher
CREATE INDEX IF NOT EXISTS FOR (n:Person) ON (n.name);
SHOW INDEXES;
```
