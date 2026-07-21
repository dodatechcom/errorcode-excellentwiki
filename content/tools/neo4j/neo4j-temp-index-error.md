---
title: "[Solution] Neo4j Temp Index Error"
description: "How to fix Neo4j temporal index errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Temporal value format wrong
- Index not created for temporal field
- Timezone mismatch

## How to Fix

```cypher
CREATE INDEX FOR (n:Event) ON (n.timestamp)
```

## Examples

```cypher
MATCH (n:Event) WHERE n.timestamp > datetime() - duration('PT1H') RETURN n
```
