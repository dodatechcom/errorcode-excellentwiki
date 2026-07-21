---
title: "[Solution] Neo4j Password Change Required Error"
description: "How to fix Neo4j forced password change errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- First login with default password
- Password policy enforcement

## How to Fix

Change password:

```cypher
ALTER USER neo4j SET PASSWORD 'newpassword';
```

## Examples

```cypher
:password
ALTER USER neo4j SET PASSWORD 'strongpassword';
```
