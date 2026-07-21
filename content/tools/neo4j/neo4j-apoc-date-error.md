---
title: "[Solution] Neo4j APOC Date Error"
description: "How to fix Neo4j APOC date parsing errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Date format not matching parser pattern
- Invalid date value
- Timezone not specified

## How to Fix

```cypher
RETURN apoc.date.parse('2024-01-15', 'ms', 'yyyy-MM-dd')
```

## Examples

```cypher
RETURN apoc.date.format(timestamp(), 'ms', 'yyyy-MM-dd HH:mm:ss')
```
