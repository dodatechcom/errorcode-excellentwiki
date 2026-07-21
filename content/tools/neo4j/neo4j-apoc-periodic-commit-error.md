---
title: "[Solution] Neo4j APOC Periodic Commit Error"
description: "Fix Neo4j APOC periodic commit errors when using PERIODIC COMMIT with APOC"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Periodic Commit Error

APOC periodic commit errors occur when periodic commit operations fail due to configuration issues.

## Common Causes

- Commit batch size too large
- Transaction log filling up during commit
- Write contention during parallel commits
- Missing index causing slow commit

## Common Error Messages

```
Neo.TransientError.Transaction.TransactionTimedOut: Transaction terminated
```

## How to Fix It

### 1. Reduce Commit Size

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.batch IS NULL RETURN n',
  'SET n.batch = 1',
  {batchSize: 200, iterateList: true}
);
```

### 2. Use Commit After Each Batch

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User {processed: false}) RETURN n LIMIT 100',
  'SET n.processed = true',
  {batchSize: 100, parallel: false}
);
```

### 3. Monitor Transaction Log

```bash
ls -lh /var/lib/neo4j/data/transactions/
```

## Examples

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.indexed IS NULL RETURN n',
  'CREATE INDEX user_email IF NOT EXISTS FOR (u:User) ON (u.email)',
  {batchSize: 1, parallel: false}
);
```
