---
title: "[Solution] Neo4j Spatial Index Error"
description: "How to fix Neo4j spatial index errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Point type not indexed
- Wrong coordinate system
- Bounding box query too large

## How to Fix

```cypher
CREATE POINT INDEX FOR (n:Location) ON (n.point)
```

## Examples

```cypher
MATCH (n:Location) WHERE point.distance(n.point, point({latitude: 51.5, longitude: -0.1})) < 1000 RETURN n
```
