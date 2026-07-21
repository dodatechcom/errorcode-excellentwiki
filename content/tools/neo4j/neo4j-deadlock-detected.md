---
title: "[Solution] Neo4j Deadlock Detected Error"
description: "How to fix Neo4j deadlock errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Two transactions locking same resources in different order
- High write concurrency on same nodes
- Missing index causing lock escalation

## How to Fix

Ensure consistent lock order and use indexes:

```cypher
CREATE INDEX FOR (n:Person) ON (n.id);
MATCH (n:Person {id: 1}) SET n.name = 'Updated';
```

## Examples

```cypher
CALL dbms.listTransactions() YIELD transactionId, lockCount;
```
