---
title: "[Solution] Neo4j Temp Index Error"
description: "Fix Neo4j temporary index errors when inline indexes fail during data import"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Temp Index Error

Temp index errors occur when temporary inline indexes used during bulk import operations fail.

## Common Causes

- Temp index not created before import
- Temp index dropped while import in progress
- Concurrent access to temp index
- Index cache size too small for import

## Common Error Messages

```
Neo.ClientError.Schema.IndexNotFound: No such index
```

## How to Fix It

### 1. Create Temp Index Before Import

```cypher
CREATE TEMPORARY INDEX temp_id IF NOT EXISTS
FOR (n:ImportNode) ON (n.externalId);
```

### 2. Check Temp Index Status

```cypher
SHOW INDEXES YIELD name, type WHERE type = 'TEMPORARY';
```

### 3. Recreate After Failure

```cypher
DROP INDEX temp_id IF EXISTS;
CREATE TEMPORARY INDEX temp_id FOR (n:ImportNode) ON (n.externalId);
```

## Examples

```cypher
CALL db.indexes() YIELD name, type RETURN name, type;
```
