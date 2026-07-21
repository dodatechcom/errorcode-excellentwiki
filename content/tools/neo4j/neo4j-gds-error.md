---
title: "[Solution] Neo4j GDS Error"
description: "Fix Neo4j Graph Data Science library errors when running algorithm procedures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j GDS Error

GDS errors occur when Graph Data Science library algorithms encounter configuration or resource issues.

## Common Causes

- GDS plugin not installed or wrong version
- Graph projection too large for available memory
- Algorithm parameter out of valid range
- Running algorithm on empty graph projection

## Common Error Messages

```
There is no procedure with the name 'gds.pageRank' registered
```

## How to Fix It

### 1. Check GDS Installation

```cypher
RETURN gds.version();
```

### 2. Create Graph Projection

```cypher
CALL gds.graph.project(
  'myGraph',
  'Person',
  'KNOWS'
);
```

### 3. Run Algorithm with Config

```cypher
CALL gds.pageRank.stream('myGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC LIMIT 10;
```

## Examples

```cypher
CALL gds.graph.list() YIELD graphName, nodeCount, relationshipCount;
```
