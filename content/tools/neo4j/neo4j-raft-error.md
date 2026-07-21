---
title: "[Solution] Neo4j Raft Consensus Error"
description: "How to fix Neo4j Raft protocol errors in clusters"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Leader unreachable
- Network partition between core servers
- Raft log too large

## How to Fix

Check Raft status:

```cypher
CALL dbms.cluster.overview();
```

## Examples

```cypher
CALL dbms.cluster.overview() YIELD id, role, leader;
```
