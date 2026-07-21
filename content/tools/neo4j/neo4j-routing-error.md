---
title: "[Solution] Neo4j Routing Error"
description: "How to fix Neo4j routing table errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Routing table stale
- Driver not refreshing routing info
- Cluster topology changed

## How to Fix

Use neo4j:// scheme for routing:

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "pw"))
```

## Examples

```python
driver.verify_connectivity()
```
