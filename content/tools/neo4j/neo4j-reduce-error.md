---
title: "[Solution] Neo4j REDUCE Error"
description: "Fix Neo4j REDUCE function errors when aggregating list values in Cypher"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j REDUCE Error

REDUCE errors occur when the aggregation function encounters type mismatches or invalid initial values.

## Common Causes

- Initial value type does not match accumulator
- Expression returns unexpected type during iteration
- REDUCE on empty list without proper initial value
- Stack overflow from very large lists

## Common Error Messages

```
Neo.ClientError.Statement.TypeError: Type mismatch
```

## How to Fix It

### 1. Ensure Type Consistency

```cypher
REDUCE(acc = 0, x IN [1, 2, 3] | acc + x);
```

### 2. Use Proper Initial Value

```cypher
MATCH (n:User)
RETURN REDUCE(total = 0, score IN n.scores | total + score) AS totalScore;
```

### 3. Alternative with APOC

```cypher
MATCH (n:User)
RETURN apoc.coll.sum(n.scores) AS totalScore;
```

## Examples

```cypher
MATCH (p:Person)-[:KNOWS]->(friend)
RETURN p.name, REDUCE(names = '', f IN collect(friend) | names + f.name + ', ') AS friends;
```
