---
title: "[Solution] Neo4j Index Error"
description: "Fix Neo4j index errors when index creation or usage fails during query execution"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Index Error

Index errors occur when index creation fails or an existing index cannot be used by the query planner.

## Common Causes

- Index name already in use
- Creating index on property with mixed types
- Index corrupted after disk failure
- Using wrong index hint

## Common Error Messages

```
Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists
```

## How to Fix It

### 1. Drop Corrupted Index

```cypher
DROP INDEX corrupted_index IF EXISTS;
```

### 2. Recreate Index

```cypher
CREATE INDEX user_name FOR (u:User) ON (u.name);
```

### 3. Check Index Status

```cypher
SHOW INDEXES YIELD name, state WHERE state <> 'online';
```

## Examples

```cypher
CALL db.index.fulltext.queryNodes('myIndex', 'search term') YIELD node, score
RETURN node, score;
```
