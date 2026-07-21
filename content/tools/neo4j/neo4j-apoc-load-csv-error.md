---
title: "[Solution] Neo4j APOC Load CSV Error"
description: "How to fix Neo4j APOC CSV loading errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- File not accessible from server
- CSV format wrong
- URL not whitelisted

## How to Fix

```ini
dbms.security.procedures.unrestricted=apoc.load.*
```

## Examples

```cypher
CALL apoc.load.csv('file:///data.csv') YIELD row RETURN row
```
