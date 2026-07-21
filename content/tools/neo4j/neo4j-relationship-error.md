---
title: "[Solution] Neo4j Relationship Error"
description: "Fix Neo4j relationship errors when creating or querying relationships with invalid patterns"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Relationship Error

Relationship errors occur when a query creates or matches relationships that violate graph structure.

## Common Causes

- Creating relationship between same node without direction
- Unique constraint on relationship properties
- Relationship type contains invalid characters
- Creating duplicate relationships

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed: Multiple unique relationships
```

## How to Fix It

### 1. Check Relationship Constraints

```cypher
SHOW CONSTRAINTS WHERE type = 'UNIQUENESS';
```

### 2. Prevent Duplicate Relationships

```cypher
MATCH (a:Person {id: 1}), (b:Person {id: 2})
WHERE NOT (a)-[:KNOWS]->(b)
CREATE (a)-[:KNOWS {since: 2024}]->(b);
```

### 3. Count Relationships by Type

```cypher
CALL db.relationshipTypes() YIELD relationshipType
RETURN relationshipType;
```

## Examples

```cypher
MATCH ()-[r]->()
RETURN type(r) AS relType, count(r) AS cnt
ORDER BY cnt DESC;
```
