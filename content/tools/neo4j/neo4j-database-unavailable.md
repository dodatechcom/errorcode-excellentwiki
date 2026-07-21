---
title: "[Solution] Neo4j Database Unavailable Error"
description: "How to fix Neo4j database unavailable errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Database is offline
- Cluster leader unavailable
- Store corruption

## How to Fix

Check database status:

```cypher
SHOW DATABASES YIELD name, address, role, requestedStatus, status;
```

## Examples

```cypher
SHOW DATABASES;
```
