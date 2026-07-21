---
title: "[Solution] Neo4j APOC Refactor Clone Error"
description: "Fix Neo4j APOC clone node errors when duplicating graph structures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Refactor Clone Error

APOC clone errors occur when cloneNodes or cloneSubgraph procedures fail during graph duplication.

## Common Causes

- Cloning creates circular reference
- Target database has different labels
- Property names conflict with existing
- Clone operation exceeds memory limit

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Cannot clone node
```

## How to Fix It

### 1. Clone with Relationship Handling

```cypher
MATCH (n:User {name: 'Alice'})
CALL apoc.refactor.cloneNodes([n], true, true)
YIELD input, output
RETURN input.name AS original, output.name AS cloned;
```

### 2. Clone Subgraph

```cypher
MATCH (n:User {name: 'Alice'})
CALL apoc.refactor.cloneSubgraph([n], {relationshipTypes: ['KNOWS']})
YIELD input, output, relationship
RETURN input, output, relationship;
```

### 3. Clone with New Properties

```cypher
MATCH (n:User)
CALL apoc.refactor.cloneNodes([n], false, false)
YIELD input, output
SET output.isClone = true, output.clonedAt = datetime()
RETURN output;
```

## Examples

```cypher
MATCH (n:User)-[r:KNOWS]->(m:User)
CALL apoc.refactor.cloneNodes([n, m], true, true)
YIELD input, output
RETURN input, output;
```
