---
title: "[Solution] Neo4j Graph Projection Error"
description: "How to fix Neo4j GDS graph projection errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Projection node/relationship types wrong
- Memory limit exceeded during projection
- Source data does not match projection schema

## How to Fix

Create projection:

```cypher
CALL gds.graph.project('myGraph', 'Person', 'KNOWS');
```

## Examples

```cypher
CALL gds.graph.project('myGraph', 'Person', 'KNOWS') YIELD graphName, nodeCount, relationshipCount;
```
