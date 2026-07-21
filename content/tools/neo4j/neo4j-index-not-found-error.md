---
title: "[Solution] Neo4j Index Not Found Error"
description: "Fix Neo4j index not found errors when DROP INDEX references non-existent index"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Index Not Found Error

Index not found errors occur when trying to drop or use an index that does not exist.

## Common Causes

- Index name typo in DROP statement
- Index was already dropped
- Using wrong database context
- Index name case mismatch

## Common Error Messages

```
Neo.ClientError.Schema.IndexNotFound: Index with name 'wrong_name' does not exist
```

## How to Fix It

### 1. List All Indexes

```cypher
SHOW INDEXES YIELD name, type;
```

### 2. Drop with IF EXISTS

```cypher
DROP INDEX my_index IF EXISTS;
```

### 3. Check Index in Specific Database

```cypher
USE analytics
SHOW INDEXES YIELD name, labelsOrTypes;
```

## Examples

```cypher
SHOW INDEXES YIELD name, state
ORDER BY name;
```
