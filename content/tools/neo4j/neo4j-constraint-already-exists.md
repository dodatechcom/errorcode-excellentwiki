---
title: "[Solution] Neo4j Constraint Already Exists Error"
description: "How to fix Neo4j constraint already exists errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Constraint creation called twice

## How to Fix

Use IF NOT EXISTS:

```cypher
CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.email IS UNIQUE;
```

## Examples

```cypher
SHOW CONSTRAINTS;
```
