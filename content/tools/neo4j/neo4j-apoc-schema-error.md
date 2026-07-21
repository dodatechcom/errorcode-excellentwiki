---
title: "[Solution] Neo4j APOC Schema Procedure Error"
description: "Fix Neo4j APOC schema procedure errors when using schema inspection functions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Schema Procedure Error

APOC schema procedure errors occur when schema inspection functions fail due to missing permissions or configuration.

## Common Causes

- APOC schema procedures restricted by security policy
- Schema in transition state during index creation
- Database offline during schema inspection
- Procedure called on non-existent database

## Common Error Messages

```
Neo.ClientError.Security.Forbidden: This operation requires privileged access
```

## How to Fix It

### 1. Grant Schema Access

```cypher
GRANT EXECUTE PROCEDURE ON DBMS PROCEDURE apoc.schema.* TO reader;
```

### 2. Use Standard Schema Commands

```cypher
SHOW INDEXES YIELD name, type, state;
SHOW CONSTRAINTS YIELD name, type;
```

### 3. Wait for Index Online

```cypher
SHOW INDEXES YIELD name, state WHERE state = 'online';
```

## Examples

```cypher
CALL apoc.schema.assert({User: ['email']}, {User: [{name: 'User', type: 'UNIQUE', property: 'email'}]});
```
