---
title: "[Solution] Neo4j Cypher Syntax Error"
description: "Fix Neo4j Cypher syntax errors caused by invalid query structure or reserved keyword usage"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Cypher Syntax Error

Cypher syntax errors occur when the query parser cannot interpret the query due to structural issues.

## Common Causes

- Missing parentheses around node patterns
- Using reserved keywords as property names without backticks
- Unmatched brackets in list comprehensions
- Incorrect USE clause in multi-database setup

## Common Error Messages

```
Neo.ClientError.Statement.SyntaxError: Invalid input
```

## How to Fix It

### 1. Validate Query Structure

```cypher
// BAD: missing arrow direction
MATCH (a)-[r]-(b) RETURN a;
// GOOD: explicit direction
MATCH (a)-[r]->(b) RETURN a;
```

### 2. Escape Reserved Keywords

```cypher
// GOOD: use backticks
MATCH (n) SET n.`name` = 'test';
```

### 3. Check Parentheses Balance

```cypher
// BAD: unmatched parenthesis
WITH [x IN range(1,10] AS nums
// GOOD
WITH [x IN range(1,10)] AS nums
```

## Examples

```cypher
EXPLAIN MATCH (n:User {email: 'test@example.com'}) RETURN n;
```
