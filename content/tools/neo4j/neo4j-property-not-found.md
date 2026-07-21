---
title: "[Solution] Neo4j Property Not Found Error"
description: "How to fix Neo4j property not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Property name misspelled
- Property does not exist on node/relationship

## How to Fix

Check properties:

```cypher
MATCH (n:Person) RETURN properties(n) LIMIT 1;
```

## Examples

```cypher
MATCH (n:Person) RETURN n LIMIT 1;
```
