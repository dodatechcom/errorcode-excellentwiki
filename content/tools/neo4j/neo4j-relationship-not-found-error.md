---
title: "[Solution] Neo4j Relationship Not Found Error"
description: "Fix Neo4j relationship not found errors when DELETE or SET operations target missing relationships"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Relationship Not Found Error

Relationship not found errors occur when a query references a relationship that does not exist.

## Common Causes

- Relationship was deleted in another transaction
- Wrong relationship type in MATCH
- Relationship direction reversed
- Referencing internal relationship ID after mutation

## Common Error Messages

```
Neo.ClientError.Statement.EntityNotFound: Relationship not found
```

## How to Fix It

### 1. Check Relationship Existence

```cypher
MATCH (a:User)-[r:KNOWS]->(b:User)
WHERE a.name = 'Alice' AND b.name = 'Bob'
RETURN count(r) AS relCount;
```

### 2. Use OPTIONAL MATCH

```cypher
MATCH (a:User {name: 'Alice'})
OPTIONAL MATCH (a)-[r:KNOWS]->(b:User)
RETURN b.name AS friend;
```

### 3. Create if Not Exists

```cypher
MATCH (a:User {name: 'Alice'}), (b:User {name: 'Bob'})
MERGE (a)-[:KNOWS]->(b);
```

## Examples

```cypher
MATCH (a)-[r]->(b)
WHERE type(r) = 'KNOWS'
RETURN a.name, b.name LIMIT 10;
```
