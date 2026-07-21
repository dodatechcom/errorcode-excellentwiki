---
title: "[Solution] Neo4j APOC Convert Error"
description: "Fix Neo4j APOC type conversion errors when transforming data between Cypher types"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Convert Error

APOC convert errors occur when APOC conversion functions receive incompatible input.

## Common Causes

- Converting non-numeric string to integer
- Null value passed to conversion function
- Boolean string not matching expected format

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Cannot convert value
```

## How to Fix It

### 1. Validate Before Converting

```cypher
WITH '123abc' AS val
RETURN CASE WHEN val =~ '^[0-9]+$' THEN toInteger(val) ELSE null END AS result;
```

### 2. Use Safe Conversion

```cypher
RETURN apoc.convert.toInteger('42') AS num;
```

### 3. Handle Null Values

```cypher
RETURN apoc.convert.toJson(coalesce(n.data, {})) AS json;
```

## Examples

```cypher
RETURN apoc.convert.fromJsonList('[1,2,3]') AS list;
```
