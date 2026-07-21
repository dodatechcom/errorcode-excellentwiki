---
title: "[Solution] Neo4j Constraint Not Found Error"
description: "How to fix Neo4j constraint not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Constraint name wrong
- Constraint was dropped

## How to Fix

List constraints:

```cypher
SHOW CONSTRAINTS;
```

## Examples

```cypher
SHOW CONSTRAINTS;
CREATE CONSTRAINT unique_email IF NOT EXISTS FOR (u:User) REQUIRE u.email IS UNIQUE;
```
