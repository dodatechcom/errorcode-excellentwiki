---
title: "[Solution] Neo4j APOC Path Error"
description: "How to fix Neo4j APOC path finding errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Path finder takes too long
- No path found
- Wrong relationship filter

## How to Fix

```cypher
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CALL apoc.path.findShortestPaths(a, b, 'KNOWS') YIELD path RETURN path
```

## Examples

```cypher
CALL apoc.path.expandConfig('startNode', {relationshipFilter: 'KNOWS', limit: 10})
```
