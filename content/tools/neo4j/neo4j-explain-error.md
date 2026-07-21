---
title: "[Solution] Neo4j Query Plan Error"
description: "How to fix Neo4j query execution plan errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Wrong index chosen by planner
- Full scan instead of index scan
- Missing statistics

## How to Fix

```cypher
EXPLAIN MATCH (n:Person {name: 'Alice'}) RETURN n
```

## Examples

```cypher
CALL dbms.queryJProfiler()
```
