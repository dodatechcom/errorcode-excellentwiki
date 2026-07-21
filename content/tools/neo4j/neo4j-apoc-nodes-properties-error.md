---
title: "[Solution] Neo4j APOC Nodes Properties Error"
description: "Fix Neo4j APOC property extraction errors when getting all properties from nodes"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Nodes Properties Error

APOC nodes properties errors occur when extracting properties from nodes for dynamic queries.

## Common Causes

- Node has null property values
- Property keys contain special characters
- Large number of properties causing memory issues
- Property name not matching expected format

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Property key is null
```

## How to Fix It

### 1. Get Non-Null Properties

```cypher
MATCH (n:User)
WITH n, [k IN keys(n) WHERE n[k] IS NOT NULL] AS validKeys
RETURN n.name, validKeys;
```

### 2. Extract Properties as Map

```cypher
MATCH (n:User {name: 'Alice'})
RETURN properties(n) AS props;
```

### 3. Use APOC for Dynamic Properties

```cypher
MATCH (n:User)
RETURN apoc.node.properties(n, ',') AS propertiesString;
```

## Examples

```cypher
MATCH (n:User)
UNWIND keys(n) AS key
RETURN key, n[key] AS value
ORDER BY key;
```
