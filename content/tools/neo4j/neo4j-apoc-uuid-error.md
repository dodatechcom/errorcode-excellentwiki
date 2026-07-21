---
title: "[Solution] Neo4j APOC UUID Error"
description: "How to fix Neo4j APOC UUID generation errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- APOC UUID procedure not found
- UUID format not as expected
- Duplicate UUIDs generated

## How to Fix

```cypher
CREATE (n:Person {uuid: apoc.create.uuid()})
```

## Examples

```cypher
RETURN apoc.create.uuid()
```
