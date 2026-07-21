---
title: "[Solution] Neo4j APOC Error"
description: "Fix Neo4j APOC procedure errors when extended library functions fail"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Error

APOC errors occur when the APOC library procedures encounter invalid input or configuration.

## Common Causes

- APOC version incompatible with Neo4j version
- Missing APOC configuration in neo4j.conf
- Invalid JSON or XML in APOC parsing functions
- Network access blocked for APOC HTTP functions

## Common Error Messages

```
Neo.ClientError.Procedure.ProcedureCallFailed: Failed to invoke procedure 'apoc.load.json'
```

## How to Fix It

### 1. Verify APOC Version

```cypher
RETURN apoc.version();
```

### 2. Allow External Access

```properties
# neo4j.conf
dbms.security.procedures.unrestricted=apoc.*
apoc.import.file.enabled=true
```

### 3. Test APOC Function

```cypher
RETURN apoc.util.sha256('test') AS hash;
```

## Examples

```cypher
CALL apoc.load.json('https://api.example.com/data.json')
YIELD value
RETURN value LIMIT 5;
```
