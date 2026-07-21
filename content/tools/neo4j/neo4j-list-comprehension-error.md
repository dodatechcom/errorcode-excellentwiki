---
title: "[Solution] Neo4j List Comprehension Error"
description: "Fix Neo4j list comprehension errors when Cypher list operations fail"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j List Comprehension Error

List comprehension errors occur when Cypher cannot evaluate the expression inside a list comprehension.

## Common Causes

- Variable scope issue inside comprehension
- Calling function that returns different types
- Infinite recursion in nested comprehension
- Memory exhaustion from large list generation

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid input 'IN'
```

## How to Fix It

### 1. Check Variable Scope

```cypher
MATCH (n:User) RETURN [x IN range(1, n.count) | x * 2] AS doubled;
```

### 2. Use Filter Where Needed

```cypher
MATCH (n:User)
RETURN [x IN n.friends WHERE x.age > 25 | x.name] AS olderFriends;
```

### 3. Avoid Large List Comprehensions

```cypher
// GOOD: use UNWIND with LIMIT
UNWIND range(0, 1000000) AS x
WITH x LIMIT 1000
RETURN x;
```

## Examples

```cypher
MATCH (n:Person)
RETURN [child IN n.children WHERE child.age < 18 | child.name] AS minorChildren;
```
