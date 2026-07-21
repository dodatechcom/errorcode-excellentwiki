---
title: "[Solution] Neo4j Path Error"
description: "Fix Neo4j path errors when MATCH patterns produce invalid or unexpected paths"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Path Error

Path errors occur when path patterns in MATCH or CREATE produce invalid graph structures.

## Common Causes

- Variable-length path exceeding maximum depth
- Path pattern creating cycles unexpectedly
- Shortest path with no existing path
- Named path variable used outside MATCH scope

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Variable length path cannot be used
```

## How to Fix It

### 1. Set Path Length Limits

```cypher
MATCH path = (a)-[:KNOWS*1..5]->(b)
```

### 2. Use OPTIONAL MATCH

```cypher
MATCH (a:User {name: 'Alice'})
OPTIONAL MATCH path = shortestPath((a)-[:KNOWS*]-(b:User {name: 'Bob'}))
RETURN path;
```

### 3. Avoid Unbounded Traversals

```cypher
MATCH (n:User)
WHERE ALL(r IN relationships(n) WHERE type(r) = 'KNOWS')
RETURN n LIMIT 100;
```

## Examples

```cypher
MATCH path = (start)-[:CONNECTED*1..3]->(end)
WHERE start <> end
RETURN length(path) AS hops, nodes(path) AS nodes;
```
