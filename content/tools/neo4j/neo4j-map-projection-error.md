---
title: "[Solution] Neo4j Map Projection Error"
description: "Fix Neo4j map projection errors when constructing maps from node properties"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Map Projection Error

Map projection errors occur when the syntax references properties that do not exist or uses invalid syntax.

## Common Causes

- Referencing property not on the node
- Using variable-length keys in projection
- Mixing map projection with literal maps incorrectly
- Nested map projection causing parse error

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid input ':'
```

## How to Fix It

### 1. Use Default Values

```cypher
MATCH (n:User)
RETURN n {
  name: n.name,
  age: coalesce(n.age, 0),
  email: n.email
};
```

### 2. Filter Null Properties

```cypher
MATCH (n:User)
WHERE n.email IS NOT NULL
RETURN n {name: n.name, email: n.email};
```

## Examples

```cypher
MATCH (n:User)-[:WROTE]->(p:Post)
RETURN n {
  name: n.name,
  posts: collect(p {title: p.title, date: p.createdAt})
};
```
