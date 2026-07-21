---
title: "[Solution] Neo4j APOC Convert Error"
description: "How to fix Neo4j APOC type conversion errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Value cannot be converted to target type
- Null value in conversion
- Format string mismatch

## How to Fix

```cypher
RETURN apoc.convert.toJson({name: 'Alice', age: 30})
```

## Examples

```cypher
RETURN apoc.convert.toSet([1, 2, 2, 3])
```
