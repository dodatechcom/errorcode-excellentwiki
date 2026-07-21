---
title: "[Solution] Neo4j Pattern Match Error"
description: "How to fix Neo4j pattern matching errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Variable length path too long
- Pattern not matching expected data
- Cartesian product from disconnected patterns

## How to Fix

```cypher
MATCH (a:Person)-[:KNOWS*1..3]->(b:Person) WHERE a.name = 'Alice' RETURN b
```

## Examples

```cypher
PROFILE MATCH (a)-[:KNOWS]->(b) RETURN count(*)
```
