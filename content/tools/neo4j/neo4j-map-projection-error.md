---
title: "[Solution] Neo4j Map Projection Error"
description: "How to fix Neo4j map projection errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Missing node variable in map projection
- Wrong property selector syntax

## How to Fix

```cypher
MATCH (n:Person)
RETURN n { .name, .age, friends: [(n)-[:KNOWS]->(m) | m.name] } AS personMap;
```

## Examples

```cypher
MATCH (n:Person)
RETURN n { .*, computed: n.age * 2 } AS enriched;
```
