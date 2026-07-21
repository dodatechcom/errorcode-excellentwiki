---
title: "[Solution] Neo4j Unique Constraint Violated Error"
description: "How to fix Neo4j unique constraint violation errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Duplicate property value on unique constraint
- Data migration creating duplicates

## How to Fix

Find duplicates:

```cypher
MATCH (n:User)
WITH n.email AS email, count(*) AS cnt
WHERE cnt > 1
RETURN email, cnt;
```

Use MERGE:

```cypher
MERGE (n:User {email: 'user@example.com'})
ON CREATE SET n.name = 'John';
```

## Examples

```cypher
MATCH (n:User) RETURN n.email, count(*) AS cnt ORDER BY cnt DESC LIMIT 10;
```
