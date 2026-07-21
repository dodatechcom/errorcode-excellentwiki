---
title: "[Solution] Neo4j Label Not Found Error"
description: "How to fix Neo4j label not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Label name misspelled
- No nodes with that label

## How to Fix

List labels:

```cypher
CALL db.labels();
```

## Examples

```cypher
CALL db.labels();
MATCH (n:Person) RETURN count(n);
```
