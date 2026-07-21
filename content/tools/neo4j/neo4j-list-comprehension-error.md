---
title: "[Solution] Neo4j List Comprehension Error"
description: "How to fix Neo4j list comprehension errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Wrong syntax for list comprehension
- Variable not in scope
- Filter expression wrong

## How to Fix

```cypher
MATCH (n:Person)
RETURN [m IN [(n)-[:KNOWS]->(friend) | friend] WHERE m.age > 25 | m.name] AS youngFriends;
```

## Examples

```cypher
MATCH (n:Person)
RETURN [x IN range(1, 10) | x * 2] AS doubled;
```
