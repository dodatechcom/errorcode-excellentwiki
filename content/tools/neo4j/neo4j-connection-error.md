---
title: "[Solution] Neo4j Connection Error"
description: "Fix Neo4j connection errors when driver cannot establish or maintain database connections"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Connection Error

Connection errors occur when the driver cannot establish or maintain a connection to the Neo4j server.

## Common Causes

- Network timeout between client and server
- Server overloaded with too many connections
- Connection pool exhausted
- DNS resolution failure for server hostname

## Common Error Messages

```
Neo4jError: Connection read timed out
```

## How to Fix It

### 1. Configure Connection Pool

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password"),
    max_connection_pool_size=100,
    connection_timeout=30
)
```

### 2. Enable Connection Retries

```python
driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password"),
    retry_initial_backoff=1,
    retry_max_backoff=30
)
```

### 3. Check Server Status

```bash
systemctl status neo4j
curl http://localhost:7474/db/manage/server/causalclustering/status
```

## Examples

```bash
neo4j status
```
