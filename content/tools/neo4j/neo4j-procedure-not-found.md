---
title: "[Solution] Neo4j Procedure Not Found Error"
description: "How to fix Neo4j procedure not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Procedure not installed (APOC etc.)
- Wrong procedure name
- Plugin JAR not loaded

## How to Fix

List procedures:

```cypher
CALL dbms.procedures() YIELD name RETURN name ORDER BY name;
```

## Examples

```cypher
CALL dbms.procedures() YIELD name WHERE name CONTAINS 'apoc' RETURN name;
```
