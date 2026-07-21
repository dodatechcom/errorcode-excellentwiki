---
title: "[Solution] Neo4j Index Already Exists Error"
description: "How to fix Neo4j index already exists errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Index creation called twice

## How to Fix

Use IF NOT EXISTS:

```cypher
CREATE INDEX IF NOT EXISTS FOR (n:Person) ON (n.name);
```

## Examples

```cypher
SHOW INDEXES;
CREATE INDEX IF NOT EXISTS FOR (n:Person) ON (n.name);
```
