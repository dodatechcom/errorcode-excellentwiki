---
title: "[Solution] Neo4j Read Only Database Error"
description: "How to fix Neo4j read-only database mode errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Database in read-only mode
- User lacks write permissions
- Cluster follower cannot write

## How to Fix

Check mode:

```cypher
SHOW DATABASES YIELD name, requestedStatus;
```

## Examples

```cypher
SHOW DATABASES YIELD name, requestedStatus, status;
```
