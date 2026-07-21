---
title: "[Solution] Neo4j Cypher Compilation Error"
description: "How to fix Neo4j Cypher compilation errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query too complex for planner
- Infinite pattern in query
- Missing index for query pattern

## How to Fix

Simplify query:

```cypher
EXPLAIN MATCH (a)-[:KNOWS]->(b)-[:KNOWS]->(c) RETURN a, b, c;
```

## Examples

```cypher
EXPLAIN MATCH (n:Person)-[:KNOWS*1..3]->(m:Person) RETURN n, m;
```
