---
title: "[Solution] Neo4j APOC Merge Error"
description: "Fix Neo4j APOC merge procedure errors when using apoc.merge functions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Merge Error

APOC merge errors occur when apoc.merge functions cannot match or create the expected pattern.

## Common Causes

- Multiple nodes match the merge key
- Merge key contains null values
- Relationship merge conflicts with existing
- APOC merge not imported properly

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed: Multiple nodes with same property
```

## How to Fix It

### 1. Use apoc.merge.node

```cypher
CALL apoc.merge.node(['User'], {email: 'alice@test.com'}, {name: 'Alice'})
YIELD node RETURN node;
```

### 2. Ensure Unique Key

```cypher
MERGE (n:User {email: $email})
ON CREATE SET n.name = $name, n.createdAt = datetime()
ON MATCH SET n.lastSeen = datetime();
```

### 3. Check Merge Result

```cypher
MATCH (n:User {email: 'alice@test.com'})
RETURN n IS NOT NULL AS exists;
```

## Examples

```cypher
CALL apoc.merge.relationships(
  {email: 'alice@test.com'}, 'KNOWS', {email: 'bob@test.com'}, {}
) YIELD rel RETURN rel;
```
