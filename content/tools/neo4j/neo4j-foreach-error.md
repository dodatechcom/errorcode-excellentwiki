---
title: "[Solution] Neo4j FOREACH Error"
description: "Fix Neo4j FOREACH errors when iterating over collections within Cypher queries"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j FOREACH Error

FOREACH errors occur when the loop variable or collection is invalid or inner operations fail.

## Common Causes

- FOREACH variable shadows outer variable
- Collection is null instead of list
- Inner CREATE referencing wrong variable
- FOREACH used where UNWIND would be better

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Variable 'x' not defined
```

## How to Fix It

### 1. Use Unique Variable Names

```cypher
MATCH (n:User) FOREACH (tag IN n.tags | CREATE (:Tag {name: tag}));
```

### 2. Ensure Collection is Not Null

```cypher
MATCH (n:User)
WHERE n.tags IS NOT NULL
FOREACH (tag IN n.tags | CREATE (:Tag {name: tag}));
```

### 3. Use UNWIND for Read Operations

```cypher
MATCH (n:User)
UNWIND n.tags AS tag
CREATE (:Tag {name: tag});
```

## Examples

```cypher
MATCH (u:User)
FOREACH (friendName IN u.friendNames |
  MERGE (f:User {name: friendName})
  MERGE (u)-[:KNOWS]->(f)
);
```
