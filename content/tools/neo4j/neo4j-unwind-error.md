---
title: "[Solution] Neo4j UNWIND Error"
description: "Fix Neo4j UNWIND errors when expanding lists in Cypher queries produces unexpected results"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j UNWIND Error

UNWIND errors occur when the UNWIND clause receives an unexpected data type or null value.

## Common Causes

- UNWIND applied to null value instead of list
- Property returning single value instead of list
- UNWIND on empty list producing no rows
- Nested UNWIND causing performance issues

## Common Error Messages

```
Neo.ClientError.Statement.TypeError: Expected a list at x but got String
```

## How to Fix It

### 1. Ensure Value is a List

```cypher
// BAD: property is single value
UNWIND n.tags AS tag RETURN tag;
// GOOD: wrap in list
UNWIND coalesce(n.tags, []) AS tag RETURN tag;
```

### 2. Handle Null Values

```cypher
MATCH (n:User)
UNWIND coalesce(n.emails, []) AS email
RETURN n.name, email;
```

### 3. Use APOC for Complex Unwind

```cypher
UNWIND apoc.coll.flatten([n.friends, n.colleagues]) AS person
RETURN person;
```

## Examples

```cypher
UNWIND [1, 2, 3] AS x
RETURN x * 2 AS doubled;
```
