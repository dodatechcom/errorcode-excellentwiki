---
title: "[Solution] Neo4j APOC Function Error"
description: "How to fix Neo4j APOC function errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- APOC function not available
- Wrong function parameters
- APOC security config blocking function

## How to Fix

List APOC functions:

```cypher
CALL apoc.help('apoc.convert') YIELD name, signature RETURN name LIMIT 10;
```

## Examples

```cypher
RETURN apoc.convert.toJson({key: 'value'});
```
