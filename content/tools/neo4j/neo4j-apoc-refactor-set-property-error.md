---
title: "[Solution] Neo4j APOC Refactor Set Property Error"
description: "Fix Neo4j APOC refactor property errors when moving or copying node properties"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Refactor Set Property Error

APOC refactor property errors occur when moving, copying, or removing properties between nodes.

## Common Causes

- Source property does not exist
- Target property name conflicts
- Property value type mismatch
- Node not found during property operation

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Property 'oldProp' not found on node
```

## How to Fix It

### 1. Move Property Between Nodes

```cypher
MATCH (source:User {name: 'Alice'}), (target:User {name: 'Bob'})
CALL apoc.refactor.moveProperty(source, 'email', target)
YIELD node RETURN node;
```

### 2. Copy Property

```cypher
MATCH (source:User), (target:User)
WHERE source.copyField IS NOT NULL
SET target.copiedField = source.copyField;
```

### 3. Remove Property Safely

```cypher
MATCH (n:User)
WHERE n.deprecatedField IS NOT NULL
REMOVE n.deprecatedField;
```

## Examples

```cypher
MATCH (n:User)
WHERE n.oldName IS NOT NULL
SET n.name = n.oldName
REMOVE n.oldName;
```
