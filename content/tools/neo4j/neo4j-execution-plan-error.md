---
title: "[Solution] Neo4j Execution Plan Error"
description: "How to fix Neo4j query execution plan errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Unoptimized execution plan
- Full graph scan instead of index lookup
- Planner choosing wrong strategy

## How to Fix

Check execution plan:

```cypher
PROFILE MATCH (n:Person {name: 'John'}) RETURN n;
```

## Examples

```cypher
PROFILE MATCH (n:Person {name: 'John'}) RETURN n;
EXPLAIN MATCH (n:Person) WHERE n.age > 25 RETURN n;
```
