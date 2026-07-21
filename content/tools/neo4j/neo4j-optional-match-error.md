---
title: "[Solution] Neo4j OPTIONAL MATCH Error"
description: "How to fix Neo4j OPTIONAL MATCH errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- OPTIONAL MATCH returning null when expected data
- Coalesce not used for null values

## How to Fix

Handle nulls:

```cypher
MATCH (n:Person)
OPTIONAL MATCH (n)-[:KNOWS]->(m)
RETURN n.name, coalesce(m.name, 'No friend');
```

## Examples

```cypher
MATCH (n:Person) OPTIONAL MATCH (n)-[:WORKS_AT]->(c) RETURN n.name, c.name;
```
