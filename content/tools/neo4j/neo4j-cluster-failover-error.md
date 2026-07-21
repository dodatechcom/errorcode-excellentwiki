---
title: "[Solution] Neo4j Cluster Failover Error"
description: "How to fix Neo4j cluster failover errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Leader election timeout
- Network partition between core servers
- Too few cores for consensus

## How to Fix

```cypher
CALL dbms.cluster.overview()
```

## Examples

```bash
neo4j-adminserver status
```
