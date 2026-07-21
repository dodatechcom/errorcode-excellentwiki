---
title: "[Solution] Neo4j Schema Lock Error"
description: "Fix Neo4j schema lock errors when DDL operations cannot proceed due to active transactions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Schema Lock Error

Schema lock errors occur when schema operations cannot proceed because active transactions hold locks.

## Common Causes

- Long-running read transaction blocking schema changes
- Bulk data import holding transaction open
- Application not closing transaction properly

## Common Error Messages

```
Neo.TransientError.Transaction.TransactionTimedOut: The transaction has been terminated
```

## How to Fix It

### 1. Find Long Transactions

```cypher
CALL dbms.listTransactions() YIELD transactionId, runningTime, query
WHERE runningTime > 1000
RETURN transactionId, runningTime, query;
```

### 2. Terminate Blocking Transaction

```cypher
CALL dbms.killTransaction('transaction-id');
```

### 3. Create Schema with IF NOT EXISTS

```cypher
CREATE INDEX product_sku IF NOT EXISTS FOR (p:Product) ON (p.sku);
```

## Examples

```cypher
CALL dbms.listQueries() YIELD queryId, query, elapsedTimeMillis
WHERE query CONTAINS 'CREATE'
RETURN queryId, query, elapsedTimeMillis;
```
