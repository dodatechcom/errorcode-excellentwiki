---
title: "[Solution] Neo4j APOC Subgraph Error"
description: "Fix Neo4j APOC subgraph extraction errors when isolating graph subsets"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Subgraph Error

APOC subgraph errors occur when extracting subgraphs for analysis or export.

## Common Causes

- Subgraph too large for memory
- Missing relationship types in filter
- Circular references in subgraph extraction
- Target database not available for copy

## Common Error Messages

```
Neo.ClientError.General.OutOfMemoryError: Subgraph too large
```

## How to Fix It

### 1. Limit Subgraph Size

```cypher
MATCH (n:User {name: 'Alice'})
CALL apoc.path.subgraphAll(n, {maxLevel: 2})
YIELD nodes, relationships
RETURN nodes, relationships LIMIT 100;
```

### 2. Filter by Relationship Type

```cypher
MATCH (n:User)
CALL apoc.path.subgraphAll(n, {relationshipFilter: 'KNOWS|FOLLOWS'})
YIELD nodes, relationships
RETURN count(nodes) AS nodeCount;
```

### 3. Export Subgraph to File

```cypher
MATCH (n:User {name: 'Alice'})
CALL apoc.path.subgraphAll(n, {maxLevel: 3})
YIELD nodes, relationships
CALL apoc.export.json.data(nodes, relationships, '/tmp/subgraph.json')
YIELD nodesExported, relationshipsExported
RETURN nodesExported, relationshipsExported;
```

## Examples

```cypher
MATCH (n:User)
CALL apoc.path.spanningTree(n, {}, {}) YIELD path
RETURN count(path) AS treeCount;
```
