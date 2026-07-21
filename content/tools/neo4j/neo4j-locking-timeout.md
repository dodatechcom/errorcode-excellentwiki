---
title: "[Solution] Neo4j Locking Timeout Error"
description: "How to fix Neo4j lock acquisition timeout errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Lock held too long by another transaction
- Deadlock causing automatic rollback
- Large write transaction blocking reads

## How to Fix

Set lock timeout:

```cypher
CALL { SET n.name = 'x' } IN TRANSACTIONS TIMEOUT 5000;
```

## Examples

```cypher
CALL dbms.listTransactions() YIELD transactionId, lockCount WHERE lockCount > 0;
```
