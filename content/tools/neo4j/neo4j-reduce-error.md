---
title: "[Solution] Neo4j REDUCE Error"
description: "How to fix Neo4j REDUCE function errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Wrong accumulator initial value
- Lambda function syntax error

## How to Fix

```cypher
MATCH (n:Person)
RETURN n.name, REDUCE(s = 0, r IN [(n)-[:KNOWS]->(m) | m.age] | s + r) AS totalAge;
```

## Examples

```cypher
MATCH path = (n:Person)-[:KNOWS*1..3]->(m)
RETURN n.name, REDUCE(s = '', x IN nodes(path) | s + x.name + ' ') AS path_names;
```
