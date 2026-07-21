---
title: "[Solution] Neo4j Shortest Path Error"
description: "Fix Neo4j shortestPath errors when pathfinding algorithms fail to find results"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Shortest Path Error

Shortest path errors occur when pathfinding functions cannot find a path or encounter invalid parameters.

## Common Causes

- No path exists between source and target
- Source and target are the same node
- Using shortestPath with negative weights
- Unbounded traversal causing memory issues

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: shortestPath requires exactly one bound relationship
```

## How to Fix It

### 1. Use OPTIONAL MATCH

```cypher
MATCH (a:User {name: 'Alice'}), (b:User {name: 'Bob'})
OPTIONAL MATCH path = shortestPath((a)-[:KNOWS*]-(b))
RETURN path;
```

### 2. Set Maximum Depth

```cypher
MATCH path = shortestPath((a)-[:KNOWS*1..10]->(b))
RETURN path;
```

### 3. Use All Shortest Paths

```cypher
MATCH path = allShortestPaths((a)-[:KNOWS*]-(b))
RETURN path;
```

## Examples

```cypher
MATCH path = shortestPath((a:City)-[:FLIES*1..5]->(b:City))
RETURN path, reduce(dist = 0, r IN relationships(path) | dist + r.distance) AS totalDist;
```
