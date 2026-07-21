---
title: "[Solution] Neo4j Shortest Path Error"
description: "How to fix Neo4j shortest path algorithm errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- No path exists between nodes
- Path length exceeding limits

## How to Fix

```cypher
MATCH path = shortestPath((a:Person {name:'John'})-[*]-(b:Person {name:'Jane'}))
RETURN path;
```

## Examples

```cypher
MATCH path = shortestPath((a)-[*..10]-(b))
WHERE elementId(a) = 'start' AND elementId(b) = 'end'
RETURN path;
```
