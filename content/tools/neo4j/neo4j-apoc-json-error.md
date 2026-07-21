---
title: "[Solution] Neo4j APOC JSON Error"
description: "Fix Neo4j APOC JSON parsing errors when processing JSON data in Cypher"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC JSON Error

APOC JSON errors occur when APOC JSON parsing functions encounter malformed or unexpected input.

## Common Causes

- Invalid JSON syntax in input string
- JSON string containing single quotes
- Nested JSON too deep for parser
- Unicode characters not properly escaped

## Common Error Messages

```
apoc.exception.json.JsonParsingException: Cannot parse JSON string
```

## How to Fix It

### 1. Validate JSON First

```cypher
RETURN apoc.json.validate('{"name": "test"}') AS isValid;
```

### 2. Parse JSON Safely

```cypher
WITH apoc.json.slurp('{"users": [{"name": "Alice"}, {"name": "Bob"}]}') AS data
UNWIND data.users AS user
RETURN user.name;
```

### 3. Handle Malformed JSON

```cypher
WITH '{"name": "test"' AS json
RETURN apoc.json.parse(json) AS parsed
```

## Examples

```cypher
RETURN apoc.convert.toJson({name: 'Alice', age: 30}) AS jsonString;
```
