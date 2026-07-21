---
title: "[Solution] Neo4j APOC Function Error"
description: "Fix Neo4j APOC function errors when APOC utility functions fail during evaluation"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Function Error

APOC function errors occur when APOC user-defined functions encounter invalid input or fail.

## Common Causes

- Function called with wrong number of arguments
- Null input where non-null required
- Function not available in community edition
- Return type mismatch

## Common Error Messages

```
Neo.ClientError.Statement.ProcedureCallFailed: Failed to invoke function
```

## How to Fix It

### 1. Check Function Signature

```cypher
SHOW FUNCTIONS YIELD name, signature WHERE name STARTS WITH 'apoc.';
```

### 2. Test Function Individually

```cypher
RETURN apoc.util.sha256('test') AS hash;
```

### 3. Handle Null Input

```cypher
RETURN apoc.convert.toJson(coalesce(n.data, {})) AS json;
```

## Examples

```cypher
RETURN apoc.text.capitalize('hello world') AS capitalized;
```
