---
title: "[Solution] Neo4j Type Error"
description: "Fix Neo4j type errors when Cypher operations receive unexpected data types"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Type Error

Type errors occur when Cypher operations receive values of an unexpected data type.

## Common Causes

- Comparing string to integer
- Mathematical operation on boolean value
- Using list function on non-list property
- Concatenating incompatible types

## Common Error Messages

```
Neo.ClientError.Statement.TypeError: Type mismatch: expected Float but was Integer
```

## How to Fix It

### 1. Explicit Type Conversion

```cypher
MATCH (n) WHERE n.age > 25
RETURN n.name, toString(n.age) AS ageStr;
```

### 2. Use CASE for Type Safety

```cypher
MATCH (n:User)
RETURN n.name,
  CASE WHEN n.age IS NOT NULL THEN n.age ELSE 0 END AS age;
```

## Examples

```cypher
MATCH (n:User)
WHERE n.age IS NOT NULL AND toString(n.age) =~ '^[0-9]+$'
RETURN toInteger(n.age) AS age;
```
