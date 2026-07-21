---
title: "[Solution] Neo4j Cypher Type Mismatch Error"
description: "Fix Neo4j Cypher type mismatch errors when operations receive incompatible data types"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Cypher Type Mismatch Error

Cypher type mismatch errors occur when expressions expect one type but receive another.

## Common Causes

- Passing integer where string expected
- Using list where single value expected
- Boolean comparison with non-boolean value
- Date/time function receiving wrong format

## Common Error Messages

```
Neo.ClientError.Statement.TypeError: Type mismatch: expected String but was Integer
```

## How to Fix It

### 1. Cast Types Explicitly

```cypher
MATCH (n:User)
RETURN n.name + ' - ' + toString(n.age) AS info;
```

### 2. Use CASE for Conditional Types

```cypher
MATCH (n:User)
RETURN CASE
  WHEN n.age > 18 THEN 'Adult'
  ELSE 'Minor'
END AS status;
```

### 3. Parse Dates Correctly

```cypher
MATCH (n:User)
WHERE n.birthday IS NOT NULL
RETURN date(n.birthday) AS birthDate;
```

## Examples

```cypher
MATCH (n:User)
RETURN toInteger(n.salary) AS salary, toString(n.id) AS idStr;
```
