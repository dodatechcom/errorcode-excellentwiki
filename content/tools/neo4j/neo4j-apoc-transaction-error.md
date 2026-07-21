---
title: "[Solution] Neo4j APOC Transaction Error"
description: "Fix Neo4j APOC transaction procedure errors when running queries within transactions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Transaction Error

APOC transaction errors occur when running queries within APOC transaction procedures.

## Common Causes

- Transaction timeout during long APOC operation
- Nested transaction limit exceeded
- Write operation in read-only transaction
- Transaction terminated due to memory pressure

## Common Error Messages

```
Neo.TransientError.Transaction.TransactionTimedOut: Transaction timeout
```

## How to Fix It

### 1. Increase Transaction Timeout

```cypher
CALL apoc.tx.run('MATCH (n:User) SET n.active = true', {}, 60000);
```

### 2. Use Periodic Iterate Instead

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) RETURN n',
  'SET n.active = true',
  {batchSize: 500}
);
```

### 3. Split Large Transactions

```cypher
CALL apoc.periodic.iterate(
  'MATCH (n:User) WHERE n.migrated IS NULL RETURN n',
  'SET n.migrated = true',
  {batchSize: 100, parallel: false}
);
```

## Examples

```cypher
CALL apoc.tx.run('CREATE (n:Test {id: 1})');
```
