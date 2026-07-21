---
title: "[Solution] Neo4j APOC Create Node Error"
description: "Fix Neo4j APOC node creation errors when using apoc.create procedures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Create Node Error

APOC node creation errors occur when apoc.create procedures fail to create nodes or relationships.

## Common Causes

- Unique constraint violation on created node
- Property value type does not match constraint
- Creating relationship to non-existent node
- Label name contains invalid characters

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed: Node already exists
```

## How to Fix It

### 1. Use SET for Existing Nodes

```cypher
MATCH (n:User {email: 'alice@example.com'})
SET n += $properties;
```

### 2. Create with APOC Safely

```cypher
CALL apoc.create.node(['User'], {name: 'Alice', email: 'alice@test.com'})
YIELD node RETURN node;
```

### 3. Handle Duplicate Key

```cypher
MERGE (n:User {email: 'alice@example.com'})
ON CREATE SET n.name = 'Alice'
ON MATCH SET n.updatedAt = datetime();
```

## Examples

```cypher
CALL apoc.create.relationships([{name: 'Alice'}, {name: 'Bob'}], 'KNOWS', {})
YIELD rel RETURN rel;
```
