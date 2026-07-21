---
title: "[Solution] Neo4j Foreach Error"
description: "How to fix Neo4j FOREACH clause errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- FOREACH not allowed in MATCH RETURN
- Variable scope issue
- Empty list in FOREACH

## How to Fix

```cypher
MATCH (n:Person) FOREACH (tag IN n.tags | CREATE (n)-[:HAS_TAG]->(:Tag {name: tag}))
```

## Examples

```cypher
MATCH (n:Person) WHERE n.name = 'Alice' FOREACH (i IN range(1,3) | CREATE (n)-[:REL]->(:Node {val: i}))
```
