---
title: "[Solution] Neo4j Load Balancing Error"
description: "How to fix Neo4j driver load balancing errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Driver not distributing queries across servers
- Least connected strategy not working
- All connections going to single server

## How to Fix

Configure load balancing:

```python
driver = GraphDatabase.driver(
    "neo4j://localhost:7687",
    auth=("neo4j", "password"),
    load_balancing_strategy="least_connected"
)
```

## Examples

```python
driver.verify_connectivity()
```
