---
title: "[Solution] Neo4j Constraint Not Found Error"
description: "Fix Neo4j constraint not found errors when referencing non-existent constraints"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Constraint Not Found Error

Constraint not found errors occur when trying to drop or modify a constraint that does not exist.

## Common Causes

- Constraint name typo
- Constraint already dropped
- Wrong database context
- Constraint created with different name

## Common Error Messages

```
Neo.ClientError.Schema.IndexNotFound: Constraint 'wrong_name' not found
```

## How to Fix It

### 1. List All Constraints

```cypher
SHOW CONSTRAINTS YIELD name, type;
```

### 2. Drop with IF EXISTS

```cypher
DROP CONSTRAINT my_constraint IF EXISTS;
```

### 3. Verify Constraint Exists Before Drop

```cypher
CALL {
  SHOW CONSTRAINTS YIELD name WHERE name = 'target_constraint'
  RETURN count(name) AS cnt
}
RETURN CASE WHEN cnt > 0 THEN 'DROP CONSTRAINT target_constraint' ELSE 'SKIP' END;
```

## Examples

```cypher
SHOW CONSTRAINTS YIELD name ORDER BY name;
```
