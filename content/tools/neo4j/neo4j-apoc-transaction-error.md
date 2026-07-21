---
title: "[Solution] Neo4j APOC Transaction Error"
description: "How to fix Neo4j APOC transaction function errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Transaction function not registered
- Timeout during transaction function
- Rollback in transaction function

## How to Fix

```cypher
CALL apoc.tx.run('MATCH (n:Person) RETURN count(n)', {}) YIELD result
```

## Examples

```cypher
CALL dbms.procedures() YIELD name WHERE name = 'apoc.tx.run'
```
