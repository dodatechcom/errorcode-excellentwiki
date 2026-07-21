---
title: "[Solution] Neo4j APOC OC (OpenCypher) Error"
description: "How to fix Neo4j APOC openCypher compatibility errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- OpenCypher syntax not supported
- Procedure expects different input type
- Version mismatch between APOC and Neo4j

## How to Fix

```cypher
CALL apoc.merge.node(['Person'], {name: 'Alice'}, {created: datetime()}) YIELD node RETURN node
```

## Examples

```cypher
CALL dbms.procedures() YIELD name WHERE name STARTS WITH 'apoc.merge'
```
