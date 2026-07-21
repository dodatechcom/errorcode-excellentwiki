---
title: "[Solution] Neo4j APOC Util Error"
description: "Fix Neo4j APOC utility function errors when using general-purpose helper functions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Util Error

APOC util errors occur when general APOC utility functions receive invalid parameters.

## Common Causes

- Function called on wrong type
- Index out of bounds for collection functions
- Null map access in utility functions
- Hash algorithm not supported

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Invalid argument
```

## How to Fix It

### 1. Check Function Signature

```cypher
SHOW FUNCTIONS YIELD name, signature WHERE name = 'apoc.util.sha256';
```

### 2. Validate Input Types

```cypher
RETURN apoc.util.validatePredicate(true, 'Validation failed') AS result;
```

### 3. Use Correct Function

```cypher
RETURN apoc.util.compress('hello world', 'UTF-8') AS compressed;
```

## Examples

```cypher
RETURN apoc.create.virtual.relationship('Alice', 'KNOWS', {}, 'Bob') AS rel;
```
