---
title: "[Solution] Neo4j Connection Refused Error"
description: "Fix Neo4j connection refused errors when clients cannot connect to Bolt or HTTP port"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Connection Refused Error

Connection refused errors occur when the client cannot establish a TCP connection to Neo4j.

## Common Causes

- Neo4j service not running
- Firewall blocking port 7687 or 7474
- Neo4j binding to localhost only
- Wrong hostname in connection string

## Common Error Messages

```
Neo4jError: Connection refused
```

## How to Fix It

### 1. Check Neo4j Status

```bash
systemctl status neo4j
```

### 2. Verify Listening Ports

```bash
ss -tlnp | grep -E '7474|7687'
```

### 3. Check Bind Address

```properties
# neo4j.conf
server.bolt.listen_address=0.0.0.0:7687
server.http.listen_address=0.0.0.0:7474
```

## Examples

```bash
nc -zv localhost 7687
```
