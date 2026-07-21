---
title: "[Solution] Neo4j APOC UUID Error"
description: "Fix Neo4j APOC UUID generation errors when creating unique identifiers"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC UUID Error

APOC UUID errors occur when the UUID generation procedure encounters issues with configuration or format.

## Common Causes

- UUID format mismatch with property constraint
- APOC UUID handler not registered
- UUID property type is not string
- Multiple UUID assignments on same node

## Common Error Messages

```
apoc.uuid.exclude: UUID already assigned to node
```

## How to Fix It

### 1. Register UUID Handler

```cypher
CALL apoc.uuid.install('User') YIELD uuid RETURN uuid;
```

### 2. Check UUID Format

```cypher
RETURN apoc.create.uuid() AS uuid;
```

### 3. Remove Duplicate UUID Config

```cypher
CALL apoc.uuid.remove('User');
CALL apoc.uuid.install('User') YIELD uuid RETURN uuid;
```

## Examples

```cypher
CREATE (n:User {name: 'Alice'});
// UUID will be auto-assigned by APOC handler
MATCH (n:User {name: 'Alice'}) RETURN n.uuid;
```
