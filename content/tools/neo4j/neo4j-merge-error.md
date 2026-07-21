---
title: "[Solution] Neo4j MERGE Error"
description: "Fix Neo4j MERGE errors when match-or-create operations produce unexpected duplicates"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j MERGE Error

MERGE errors occur when the merge operation matches more patterns than expected or creates unintended duplicates.

## Common Causes

- MERGE matching multiple existing patterns
- Missing property in MERGE causing multiple matches
- MERGE with MATCH creating Cartesian product
- Using MERGE in FOREACH with wrong scope

## Common Error Messages

```
Neo.ClientError.Statement.ConstraintViolation: Already exists
```

## How to Fix It

### 1. Specify All Match Properties

```cypher
MERGE (n:User {email: 'alice@example.com'})
ON CREATE SET n.createdAt = datetime()
ON MATCH SET n.updatedAt = datetime();
```

### 2. Use MERGE with Relationship

```cypher
MATCH (a:User {name: 'Alice'}), (b:User {name: 'Bob'})
MERGE (a)-[:KNOWS]->(b);
```

### 3. Check Existing Before Merge

```cypher
MATCH (n:User {email: $email})
RETURN count(n) AS existing;
// Then MERGE if count is 0
```

## Examples

```cypher
MERGE (c:Country {code: 'US'})
ON CREATE SET c.name = 'United States', c.founded = 1776
ON MATCH SET c.lastAccessed = datetime();
```
