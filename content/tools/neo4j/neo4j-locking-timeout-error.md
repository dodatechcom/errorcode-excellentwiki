---
title: "[Solution] Neo4j Locking Timeout Error"
description: "Fix Neo4j locking timeout errors when transactions wait too long for resource locks"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Locking Timeout Error

Locking timeout errors occur when a transaction cannot acquire a lock within the configured timeout.

## Common Causes

- Long-running transaction holding exclusive locks
- High contention on hot nodes
- Lock timeout too short for workload
- Index update causing write lock escalation

## Common Error Messages

```
Neo.TransientError.Transaction.LockClientTimeout: The client has timed out
```

## How to Fix It

### 1. Increase Lock Timeout

```cypher
CALL dbms.config.update('dbms.lock.acquisition.timeout', '30s');
```

### 2. Reduce Contention

```cypher
// Process in smaller batches
MATCH (n:User {processed: false})
WITH n LIMIT 100
SET n.processed = true;
```

### 3. Check Lock Information

```cypher
CALL dbms.listTransactions() YIELD transactionId, locks
WHERE locks > 0
RETURN transactionId, locks;
```

## Examples

```cypher
CALL dbms.listLocks() YIELD resourceId, type, startDateTime;
```
