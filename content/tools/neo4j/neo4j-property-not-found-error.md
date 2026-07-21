---
title: "[Solution] Neo4j Property Not Found Error"
description: "Fix Neo4j property not found errors when accessing undefined node or relationship properties"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Property Not Found Error

Property not found errors occur when a query references a property that does not exist on a node or relationship.

## Common Causes

- Property was removed in schema migration
- Typo in property name
- Property exists on different label
- Property was never set during data creation

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Property 'nonexistent' not found
```

## How to Fix It

### 1. Check Existing Properties

```cypher
MATCH (n:User) RETURN keys(n) AS properties LIMIT 5;
```

### 2. Use Property Existence Check

```cypher
MATCH (n:User)
WHERE n.email IS NOT NULL
RETURN n.name, n.email;
```

### 3. Add Property with Default

```cypher
MATCH (n:User)
WHERE n.email IS NULL
SET n.email = 'unknown@example.com';
```

## Examples

```cypher
MATCH (n:User)
RETURN n.name, coalesce(n.nickname, n.name) AS displayName;
```
