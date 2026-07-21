---
title: "[Solution] Neo4j List Index Error"
description: "How to fix Neo4j list index out of bounds errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Accessing index beyond list length
- Empty list access
- Negative index

## How to Fix

```cypher
MATCH (n) WHERE size(n.tags) > 0 RETURN n.tags[0]
```

## Examples

```cypher
MATCH (n) RETURN CASE WHEN size(n.items) > 2 THEN n.items[2] ELSE null END
```
