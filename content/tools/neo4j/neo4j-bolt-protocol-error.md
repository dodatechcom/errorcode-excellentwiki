---
title: "[Solution] Neo4j Bolt Protocol Error"
description: "Fix Neo4j Bolt protocol errors when client drivers cannot communicate with the server"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Bolt Protocol Error

Bolt protocol errors occur when the client driver version is incompatible with the Neo4j server.

## Common Causes

- Driver version too old for server Bolt version
- Bolt connector disabled in server config
- SSL/TLS configuration mismatch
- Thread pool exhausted for Bolt connections

## Common Error Messages

```
Neo.ClientError.Security.Unauthorized: The client is unauthorized
```

## How to Fix It

### 1. Check Bolt Status

```bash
curl http://localhost:7474/db/manage/server/bolt
```

### 2. Enable Bolt Connector

```properties
# neo4j.conf
server.bolt.enabled=true
server.bolt.listen_address=:7687
```

### 3. Test Bolt Connectivity

```bash
cypher-shell -u neo4j -p password "RETURN 1"
```

## Examples

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
print(driver.protocol_version)
```
