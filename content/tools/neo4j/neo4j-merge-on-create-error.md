---
title: "[Solution] Neo4j MERGE ON CREATE Error"
description: "How to fix Neo4j MERGE ON CREATE clause errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ON CREATE without MERGE
- SET syntax wrong in ON CREATE

## How to Fix

```cypher
MERGE (n:Person {id: 123})
ON CREATE SET n.name = 'New Person', n.createdAt = datetime()
ON MATCH SET n.lastAccessed = datetime();
```

## Examples

```cypher
MERGE (n:Person {email: 'user@example.com'})
ON CREATE SET n.name = 'John'
ON MATCH SET n.loginCount = coalesce(n.loginCount, 0) + 1;
```
