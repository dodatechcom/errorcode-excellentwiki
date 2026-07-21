---
title: "[Solution] Neo4j Node Not Found Error"
description: "How to fix Neo4j node not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Node was deleted
- Wrong ID used in MATCH

## How to Fix

Search by property:

```cypher
MATCH (n) WHERE n.id = 123 RETURN n;
```

## Examples

```cypher
MATCH (n:Person {name: 'John'}) RETURN n;
```
