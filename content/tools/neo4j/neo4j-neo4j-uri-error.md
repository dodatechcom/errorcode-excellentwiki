---
title: "[Solution] Neo4j neo4j:// URI Error"
description: "How to fix Neo4j neo4j:// URI scheme errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Using bolt:// instead of neo4j:// for routed connections
- Missing database name in URI
- Driver version incompatible

## How to Fix

Use correct URI:

```
neo4j://localhost:7687/mydb
bolt://localhost:7687
```

## Examples

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))
```
