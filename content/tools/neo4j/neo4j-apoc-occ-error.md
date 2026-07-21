---
title: "[Solution] Neo4j APOC OCC Error"
description: "Fix Neo4j APOC optimistic concurrency control errors during concurrent graph modifications"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC OCC Error

APOC OCC errors occur when optimistic concurrency control detects conflicts during graph modifications.

## Common Causes

- Two transactions modifying same node simultaneously
- Version property mismatch after concurrent update
- Retry loop not handling OCC failures
- Stale read causing write conflict

## Common Error Messages

```
Neo.ClientError.Statement.ConstraintVerificationFailed: Concurrent modification detected
```

## How to Fix It

### 1. Use Version Property

```cypher
MATCH (n:User {id: 1})
WHERE n.version = $expectedVersion
SET n.name = $newName, n.version = n.version + 1
RETURN n;
```

### 2. Implement Retry Logic

```cypher
CALL apoc.retry.withDelay(
  'MATCH (n:User {id: 1}) SET n.name = $name RETURN n',
  ['Neo.ClientError.Statement.ConstraintVerificationFailed'],
  3, 1000
);
```

### 3. Use MERGE with ON MATCH

```cypher
MERGE (n:User {id: 1})
ON CREATE SET n.name = 'Alice', n.version = 1
ON MATCH SET n.name = 'Alice', n.version = n.version + 1;
```

## Examples

```cypher
MATCH (n:User {id: 1})
SET n.version = coalesce(n.version, 0) + 1
RETURN elementId(n), n.version;
```
