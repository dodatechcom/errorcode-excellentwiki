---
title: "[Solution] Neo4j Parameter Syntax Error"
description: "How to fix Neo4j parameter syntax errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wrong parameter format
- Parameter not passed in query

## How to Fix

Use correct parameter syntax:

```cypher
MATCH (n:Person {name: $name}) RETURN n;
```

## Examples

```cypher
:param name => 'John'
MATCH (n:Person {name: $name}) RETURN n;
```
