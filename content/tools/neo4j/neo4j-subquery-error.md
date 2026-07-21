---
title: "[Solution] Neo4j CALL Subquery Error"
description: "How to fix Neo4j CALL subquery errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Subquery syntax error
- Variable scope issue between outer and inner query
- Missing YIELD in subquery

## How to Fix

```cypher
MATCH (n:Person)
CALL {
  WITH n
  MATCH (n)-[:KNOWS]->(m)
  RETURN m.name AS friend
}
RETURN n.name, friend;
```

## Examples

```cypher
MATCH (n:Person)
CALL (n) {
  MATCH (n)-[:WORKS_AT]->(c)
  RETURN c.name AS company
}
RETURN n.name, company;
```
