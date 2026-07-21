---
title: "[Solution] Neo4j Deadlock Detected Error"
description: "Fix Neo4j deadlock detected errors when concurrent transactions compete for the same resources"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Deadlock Detected Error

Deadlock errors occur when two or more transactions hold locks that the other needs.

## Common Causes

- Concurrent transactions locking nodes in different orders
- Long-running transactions holding exclusive locks
- Heavy write load on same graph region
- Missing indexes causing full scans with locks

## Common Error Messages

```
Neo.TransientError.Transaction.DeadlockDetected: The transaction has been terminated.
```

## How to Fix It

### 1. Reduce Lock Scope

```cypher
// GOOD: lock and update individually
MATCH (a:Account {id: 1}) SET a.balance = a.balance - 100;
MATCH (b:Account {id: 2}) SET b.balance = b.balance + 100;
```

### 2. Set Transaction Timeout

```cypher
CALL dbms.transaction.timeout.set(30000);
```

### 3. Check for Long Transactions

```cypher
CALL dbms.listTransactions() YIELD transactionId, runningTime
WHERE runningTime > 10000
RETURN transactionId, runningTime;
```

## Examples

```cypher
CALL dbms.killTransaction('transaction-id');
```
