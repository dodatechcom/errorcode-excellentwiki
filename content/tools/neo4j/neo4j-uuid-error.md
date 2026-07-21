---
title: "[Solution] Neo4j UUID Error"
description: "How to fix Neo4j UUID generation and constraint errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- UUID not generated on create
- UUID constraint not unique
- UUID format invalid

## How to Fix

```cypher
CREATE CONSTRAINT FOR (n:Person) REQUIRE n.uuid IS UNIQUE
```

## Examples

```cypher
CREATE (n:Person {uuid: randomUUID(), name: 'Alice'})
```
