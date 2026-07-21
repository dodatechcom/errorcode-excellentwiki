---
title: "[Solution] Neo4j OPTIONAL MATCH Error"
description: "Fix Neo4j OPTIONAL MATCH errors when optional pattern matching produces unexpected nulls"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j OPTIONAL MATCH Error

OPTIONAL MATCH errors occur when optional patterns produce unexpected null values that break downstream operations.

## Common Causes

- Using null values from OPTIONAL MATCH in arithmetic
- OPTIONAL MATCH producing multiple rows unexpectedly
- Cascading OPTIONAL MATCH creating Cartesian product
- Using result without checking for null

## Common Error Messages

```
Neo.ClientError.Statement.TypeError: Cannot perform division by zero
```

## How to Fix It

### 1. Check for Null Before Use

```cypher
MATCH (n:User)
OPTIONAL MATCH (n)-[:OWNS]->(c:Car)
WHERE c IS NOT NULL
RETURN n.name, c.model;
```

### 2. Use coalesce for Default Values

```cypher
MATCH (n:User)
OPTIONAL MATCH (n)-[:OWNS]->(c:Car)
RETURN n.name, coalesce(c.model, 'No car') AS car;
```

### 3. Limit OPTIONAL MATCH Results

```cypher
MATCH (n:User)
OPTIONAL MATCH (n)-[:KNOWS]->(m:User)
WITH n, collect(m) AS friends
WHERE size(friends) <= 10
RETURN n.name, friends;
```

## Examples

```cypher
MATCH (n:User)
OPTIONAL MATCH (n)-[:WROTE]->(p:Post)
RETURN n.name, count(p) AS postCount;
```
