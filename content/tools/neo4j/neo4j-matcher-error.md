---
title: "[Solution] Neo4j Matcher Error"
description: "Fix Neo4j pattern matcher errors when graph pattern matching produces incorrect results"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Matcher Error

Matcher errors occur when the pattern matching engine encounters ambiguous or invalid patterns.

## Common Causes

- Same variable used for node and relationship
- Multiple MATCH clauses creating unintended Cartesian product
- Pattern matching on non-indexed properties causing timeout
- Variable-length pattern without upper bound

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Variable already declared
```

## How to Fix It

### 1. Use Distinct Variable Names

```cypher
// BAD: 'r' used twice
MATCH (a)-[r]->(b)-[r]->(c)
// GOOD: unique names
MATCH (a)-[r1]->(b)-[r2]->(c)
```

### 2. Add Index for Matched Properties

```cypher
CREATE INDEX user_email IF NOT EXISTS FOR (u:User) ON (u.email);
```

### 3. Use WHERE Clause

```cypher
MATCH (n:User)-[r:KNOWS]->(m:User)
WHERE n.name = 'Alice'
RETURN m.name;
```

## Examples

```cypher
MATCH (a)-[r1:KNOWS]->(b)-[r2:KNOWS]->(c)
WHERE a <> c
RETURN a.name, b.name, c.name;
```
