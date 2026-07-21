---
title: "[Solution] Neo4j UNWIND Error"
description: "How to fix Neo4j UNWIND errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Empty list passed to UNWIND
- UNWIND on non-list value
- Variable not in scope

## How to Fix

```cypher
UNWIND [1, 2, 3] AS x RETURN x;
```

## Examples

```cypher
UNWIND $names AS name CREATE (n:Person {name: name});
```
