---
title: "[Solution] Neo4j APOC Periodic Error"
description: "Fix Neo4j APOC periodic iteration errors when batch processing large datasets"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Periodic Error

APOC periodic errors occur when the periodic iterate procedure encounters batch processing issues.

## Common Causes

- Batch size too large for available memory
- Query inside iteration causing deadlock
- Concurrent modifications during iteration
- Iterator query returning no results

## Common Error Messages

```
Neo.ClientError.Statement.ProcedureCallFailed: apoc.periodic.iterate failed
```

## How to Fix It

### 1. Reduce Batch Size

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.processed IS NULL RETURN n',
  'SET n.processed = true',
  {batchSize: 500, parallel: true}
);
```

### 2. Use Sequential Processing

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) RETURN n',
  'SET n.updatedAt = datetime()',
  {batchSize: 1000, parallel: false}
);
```

### 3. Add Error Handling

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) RETURN n',
  'SET n.status = "active"',
  {batchSize: 500, errorHandler: 'log'}
);
```

## Examples

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.email IS NULL RETURN n',
  'DETACH DELETE n',
  {batchSize: 100}
) YIELD batches, total, errorMessages;
```
