---
title: "[Solution] Neo4j COLLECT Error"
description: "How to fix Neo4j COLLECT aggregation errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- COLLECT returning null values
- Memory limit with large collections
- DISTINCT not used when needed

## How to Fix

```cypher
MATCH (n:Person)-[:KNOWS]->(m)
RETURN n.name, COLLECT(DISTINCT m.name) AS friends;
```

## Examples

```cypher
MATCH (n:Person)
RETURN n.name, COLLECT(m.name) AS friends LIMIT 10;
```
