---
title: "[Solution] Neo4j APOC Refactor Error"
description: "Fix Neo4j APOC refactor errors when using graph transformation procedures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Refactor Error

APOC refactor errors occur when the graph transformation procedures encounter invalid operations.

## Common Causes

- Trying to rename label that has indexes
- Refactoring creates duplicate relationships
- Source node deleted during refactor
- Circular reference in node clone

## Common Error Messages

```
Neo.ClientError.Schema.SchemaRuleAllocationFailed: Failed to create schema rule
```

## How to Fix It

### 1. Clone Nodes Correctly

```cypher
MATCH (n:User {name: 'Alice'})
CALL apoc.refactor.cloneNodes([n], false, true)
YIELD input, output
RETURN input, output;
```

### 2. Rename Label Safely

```cypher
CALL apoc.refactor.rename.label('OldLabel', 'NewLabel', ['OldLabel']);
```

### 3. Fix Duplicate Relationships

```cypher
MATCH (a)-[r1:KNOWS]->(b)
WITH a, b, collect(r1) AS rels
WHERE size(rels) > 1
UNWIND rels[1..] AS dup
DELETE dup;
```

## Examples

```cypher
CALL apoc.refactor.to('nodeId1', 'nodeId2', 'SAME_AS', {});
```
