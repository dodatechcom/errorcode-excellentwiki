---
title: "[Solution] Neo4j Constraint Already Exists Error"
description: "Fix Neo4j constraint already exists errors when creating duplicate constraint definitions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Constraint Already Exists Error

This error occurs when attempting to create a constraint that already exists in the database.

## Common Causes

- Application bootstrap creates constraints on every start
- Migration script runs multiple times
- Same constraint defined with different name but same properties

## Common Error Messages

```
Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists: Equivalent constraint already exists
```

## How to Fix It

### 1. List Existing Constraints

```cypher
SHOW CONSTRAINTS YIELD name, type, labelsOrTypes, properties;
```

### 2. Drop and Recreate

```cypher
DROP CONSTRAINT user_email_unique IF EXISTS;
CREATE CONSTRAINT user_email_unique IF NOT EXISTS
FOR (u:User) REQUIRE u.email IS UNIQUE;
```

### 3. Use IF NOT EXISTS

```cypher
CREATE CONSTRAINT product_sku IF NOT EXISTS
FOR (p:Product) REQUIRE p.sku IS UNIQUE;
```

## Examples

```cypher
SHOW CONSTRAINTS WHERE type = 'UNIQUE';
```
