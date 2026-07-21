---
title: "[Solution] Neo4j Index Already Exists Error"
description: "Fix Neo4j index already exists errors when trying to create a duplicate index definition"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Index Already Exists Error

This error occurs when you attempt to create an index that already exists in the database.

## Common Causes

- Migration script running multiple times
- Application startup creates indexes on every boot
- Duplicate index definitions for same label and property

## Common Error Messages

```
Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists: An equivalent index already exists
```

## How to Fix It

### 1. List Existing Indexes

```cypher
SHOW INDEXES;
```

### 2. Create Index Only If Not Exists

```cypher
CREATE INDEX user_email IF NOT EXISTS FOR (u:User) ON (u.email);
```

### 3. Drop and Recreate

```cypher
DROP INDEX user_email IF EXISTS;
CREATE INDEX user_email FOR (u:User) ON (u.email);
```

## Examples

```cypher
SHOW INDEXES YIELD name, type, labelsOrTypes, properties, state
RETURN name, type, labelsOrTypes, properties, state;
```
