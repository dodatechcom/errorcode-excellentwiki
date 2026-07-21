---
title: "[Solution] Neo4j Vector Index Error"
description: "How to fix Neo4j vector index errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Vector dimension mismatch
- Index not built for vector field
- Similarity metric wrong

## How to Fix

```cypher
CREATE VECTOR INDEX myvec FOR (n:Item) ON (n.embedding) OPTIONS {indexConfig: {`vector.dimensions`: 1536, `vector.similarity_function`: 'cosine'}}
```

## Examples

```cypher
CALL db.index.vector.queryNodes('myvec', 10, $queryVector) YIELD node, score
```
