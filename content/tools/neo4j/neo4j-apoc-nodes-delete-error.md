---
title: "[Solution] Neo4j APOC Delete Node Error"
description: "Fix Neo4j APOC node deletion errors when removing nodes with APOC procedures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Delete Node Error

APOC node deletion errors occur when deleting nodes using APOC procedures fails.

## Common Causes

- Node has relationships without DETACH
- Deleting node referenced by index
- Node ID changed during transaction
- Batch delete exceeding transaction timeout

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed: Cannot delete node with relationships
```

## How to Fix It

### 1. Detach Before Delete

```cypher
MATCH (n:User {status: 'deleted'})
CALL apoc.nodes.delete(n, true)
YIELD nodeCount RETURN nodeCount;
```

### 2. Delete in Batches

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:TempData) RETURN n',
  'DETACH DELETE n',
  {batchSize: 500}
);
```

### 3. Delete with APOC

```cypher
MATCH (n:OldRecord)
CALL apoc.nodes.delete(n, true)
YIELD nodeCount
RETURN count(*) AS deletedCount;
```

## Examples

```cypher
MATCH (n:User)
WHERE n.createdAt < date('2020-01-01')
DETACH DELETE n;
```
