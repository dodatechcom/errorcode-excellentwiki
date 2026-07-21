---
title: "[Solution] Neo4j APOC Refactor Error"
description: "How to fix Neo4j APOC node/relationship refactor errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Node has relationships that prevent deletion
- Refactor creates duplicate nodes
- Label or property name collision

## How to Fix

```cypher
CALL apoc.refactor.rename.type('OLD_REL', 'NEW_REL')
```

## Examples

```cypher
CALL apoc.refactor.cloneNodes([nodeId1, nodeId2])
```
