---
title: "[Solution] Neo4j Constraint Error"
description: "Fix Neo4j constraint errors when creating constraints that conflict with existing data"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Constraint Error

Constraint errors occur when a new constraint conflicts with existing data or other constraints.

## Common Causes

- Creating unique constraint on property with duplicates
- Property existence constraint on nodes missing that property
- Multiple constraints with conflicting rules

## Common Error Messages

```
Neo.ClientError.Schema.ConstraintValidationFailed: The constraint cannot be created
```

## How to Fix It

### 1. Find Duplicate Data

```cypher
MATCH (n:User)
WITH n.email AS email, count(*) AS cnt
WHERE cnt > 1
RETURN email, cnt;
```

### 2. Clean Duplicates

```cypher
MATCH (n:User)
WITH n.email AS email, collect(n) AS nodes
WHERE size(nodes) > 1
UNWIND nodes[1..] AS dup
DETACH DELETE dup;
```

### 3. Create Constraint

```cypher
CREATE CONSTRAINT user_email_unique IF NOT EXISTS
FOR (u:User) REQUIRE u.email IS UNIQUE;
```

## Examples

```cypher
SHOW CONSTRAINTS;
```
