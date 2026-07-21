---
title: "[Solution] Neo4j Cypher Type Error"
description: "How to fix Neo4j Cypher type mismatch errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Comparing incompatible types
- Wrong function return type

## How to Fix

Use type conversion:

```cypher
RETURN toInteger('42'), toString(42), toFloat(42);
```

## Examples

```cypher
RETURN toInteger('123'), toString(123), toFloat('3.14');
```
