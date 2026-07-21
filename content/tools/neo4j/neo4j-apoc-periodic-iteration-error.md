---
title: "[Solution] Neo4j APOC Periodic Iteration Error"
description: "Fix Neo4j APOC periodic iteration errors when batch processing queries"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Periodic Iteration Error

APOC periodic iteration errors occur when the periodic iterate function encounters execution issues.

## Common Causes

- Parallel execution causing deadlocks
- Error handler not properly configured
- Iterator query returning zero results
- Batch operation on already-processed data

## Common Error Messages

```
Neo.ClientError.Statement.ProcedureCallFailed: apoc.periodic.iterate failed
```

## How to Fix It

### 1. Use Sequential Processing

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.status = "pending" RETURN n',
  'SET n.status = "processed"',
  {batchSize: 500, parallel: false}
);
```

### 2. Add Error Handler

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) RETURN n',
  'SET n.updatedAt = datetime()',
  {batchSize: 1000, errorHandler: 'log', params: {}}
);
```

### 3. Check Result Statistics

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.migrated IS NULL RETURN n',
  'SET n.migrated = true',
  {batchSize: 500}
) YIELD batches, total, errorMessages
RETURN batches, total, errorMessages;
```

## Examples

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) RETURN n',
  'DETACH DELETE n',
  {batchSize: 100}
) YIELD batches, total RETURN batches, total;
```
