---
title: "[Solution] Neo4j Cluster Leader Error"
description: "How to fix Neo4j cluster leader unavailability errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Leader node down
- Leader cannot commit (quorum lost)
- Network partition

## How to Fix

Check leader:

```cypher
CALL dbms.cluster.overview() YIELD role WHERE role = 'Leader';
```

## Examples

```cypher
CALL dbms.cluster.overview() YIELD id, role, leader;
```
