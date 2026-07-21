---
title: "[Solution] Neo4j APOC Nodes Get Error"
description: "Fix Neo4j APOC get node errors when retrieving nodes by ID with APOC"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Nodes Get Error

APOC get node errors occur when apoc.node.get or similar functions fail to retrieve a node.

## Common Causes

- Node was deleted between query and retrieval
- Using internal ID instead of elementId
- Node belongs to different database
- Transaction isolation issue

## Common Error Messages

```
Neo.ClientError.Statement.EntityNotFound: Node not found
```

## How to Fix It

### 1. Use elementId Instead of ID

```cypher
MATCH (n:User {email: 'alice@test.com'})
RETURN elementId(n) AS uid, n.name;
```

### 2. Check Node Exists First

```cypher
OPTIONAL MATCH (n:User {email: 'alice@test.com'})
RETURN CASE WHEN n IS NOT NULL THEN n.name ELSE 'Not found' END;
```

### 3. Get Node with Relationships

```cypher
MATCH (n:User {name: 'Alice'})
OPTIONAL MATCH (n)-[r]->(m)
RETURN n, collect({rel: type(r), target: m.name}) AS connections;
```

## Examples

```cypher
MATCH (n:User)
WHERE elementId(n) = $elementId
RETURN n;
```
