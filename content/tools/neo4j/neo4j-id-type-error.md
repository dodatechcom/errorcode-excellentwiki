---
title: "[Solution] Neo4j ID Type Error"
description: "How to fix Neo4j ID type errors in queries"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Using internal ID after store switch
- ID type mismatch in parameters
- Deprecated ID() function usage

## How to Fix

```cypher
MATCH (n) WHERE n.myId = $id RETURN n
```

## Examples

```cypher
CREATE CONSTRAINT FOR (n:Person) REQUIRE n.myId IS UNIQUE
```
