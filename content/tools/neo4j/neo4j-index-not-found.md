---
title: "[Solution] Neo4j Index Not Found Error"
description: "How to fix Neo4j index not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Index name wrong
- Index dropped
- Index not yet created

## How to Fix

List indexes:

```cypher
SHOW INDEXES;
```

Create index:

```cypher
CREATE INDEX FOR (n:Person) ON (n.name);
```

## Examples

```cypher
SHOW INDEXES;
CREATE INDEX IF NOT EXISTS FOR (n:Person) ON (n.name);
```
