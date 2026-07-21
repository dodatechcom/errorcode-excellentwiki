---
title: "[Solution] Neo4j Procedure Execution Error"
description: "Fix Neo4j procedure execution errors when stored procedures fail during runtime"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Procedure Execution Error

Procedure execution errors occur when a registered stored procedure encounters a runtime failure.

## Common Causes

- Procedure accessing unavailable external resource
- Null pointer exception in custom procedure code
- Procedure exceeding time limit
- Security restriction blocking procedure access

## Common Error Messages

```
Neo.ClientError.Statement.ProcedureCallFailed: Failed to invoke procedure
```

## How to Fix It

### 1. Check Procedure Permissions

```cypher
SHOW PROCEDURES YIELD name, description
WHERE name CONTAINS 'custom';
```

### 2. Grant Procedure Access

```cypher
GRANT EXECUTE PROCEDURE ON DBMS PROCEDURE custom.* TO analyst;
```

### 3. Debug with Logging

```properties
# neo4j.conf
dbms.logs.debug.level=DEBUG
```

## Examples

```cypher
CALL custom.myProcedure($input)
YIELD result
RETURN result;
```
