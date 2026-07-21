---
title: "[Solution] Neo4j Full-Text Index Error"
description: "How to fix Neo4j full-text index errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Full-text index not created
- Analyzer mismatch
- Query syntax wrong for full-text search

## How to Fix

```cypher
CREATE FULLTEXT INDEX mytextindex FOR (n:Person) ON EACH [n.name, n.bio]
```

## Examples

```cypher
CALL db.index.fulltext.queryNodes('mytextindex', 'search term') YIELD node, score
```
