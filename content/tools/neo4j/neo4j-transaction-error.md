---
title: "[Solution] Neo4j Transaction Error — How to Fix"
description: "Fix Neo4j transaction errors including timeout, conflict, deadlock, and serialization failures in graph database transactions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Transaction Error

Transaction errors in Neo4j occur when transactions fail due to timeouts, conflicts, deadlocks, or resource exhaustion. Neo4j uses multi-version concurrency control for transaction isolation.

## Why It Happens

- A transaction runs longer than `dbms.transaction.timeout`
- Two transactions modify the same nodes or relationships
- A deadlock occurs between competing transactions
- The transaction tries to modify data that was changed by another committed transaction
- The transaction log is full
- The query inside the transaction exceeds memory limits

## Common Error Messages

```
Neo.TransientError.Transaction.TransactionTimedOut:
The transaction has been terminated
```

```
Neo.ClientError.Transaction.TransactionConflict:
Transaction could not be committed due to conflict with another transaction
```

```
Neo.TransientError.Transaction.DeadlockDetected:
Detected deadlock
```

```
Neo.TransientError.Transaction.OutlierTransaction:
Too many concurrent transactions
```

## How to Fix It

### 1. Fix Transaction Timeout

```bash
# Check current timeout
grep transaction.timeout /etc/neo4j/neo4j.conf

# Increase timeout (in seconds)
dbms.transaction.timeout=600
```

### 2. Fix Transaction Conflicts

```javascript
// Use optimistic locking with retries
async function updateWithRetry(session, nodeId, props, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const result = await session.run(
        'MATCH (n) WHERE id(n) = $id SET n += $props RETURN n',
        { id: nodeId, props }
      );
      return result.records[0];
    } catch (error) {
      if (error.code === 'Neo.ClientError.Transaction.TransactionConflict' && i < maxRetries - 1) {
        await new Promise(r => setTimeout(r, 100 * (i + 1)));
      } else {
        throw error;
      }
    }
  }
}
```

### 3. Fix Deadlock Issues

```bash
# Enable deadlock logging
dbms.logs.debug.level=DEBUG

# In the query, lock nodes in a consistent order
// Always lock nodes by ID ascending
MATCH (a:Person), (b:Person) WHERE id(a) < id(b) AND a.name = 'A' AND b.name = 'B'
CREATE (a)-[:KNOWS]->(b);
```

### 4. Limit Concurrent Transactions

```bash
# In neo4j.conf
dbms.max_concurrent_transactions=500
dbms.connector.bolt.thread_pool_size=200
```

## Common Scenarios

- **Long-running analytics transaction times out**: Increase `transaction.timeout` or break into smaller transactions.
- **Concurrent writes cause conflicts**: Use optimistic locking with retry logic.
- **Deadlock between two transactions**: Lock nodes in a consistent order (e.g., by ID ascending).

## Prevent It

- Keep transactions as short as possible
- Use retry logic for transaction conflicts
- Monitor `CALL dbms.listTransactions()` for long-running transactions

## Related Pages

- [Neo4j Lock Error](/tools/neo4j/neo4j-lock-error)
- [Neo4j Memory Error](/tools/neo4j/neo4j-memory-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
