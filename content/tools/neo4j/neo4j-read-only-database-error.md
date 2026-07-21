---
title: "[Solution] Neo4j Read-Only Database Error"
description: "Fix Neo4j read-only database errors when write operations are attempted on follower servers"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Read-Only Database Error

Read-only database errors occur when write operations are attempted on a database or server that is in read-only mode.

## Common Causes

- Application connected to follower server in cluster
- Database mode set to read-only for maintenance
- Causal cluster routing directing writes to follower
- Transaction started on read-only connection

## Common Error Messages

```
Neo.ClientError.Statement.AccessModeViolation: Write operations are not allowed on this server
```

## How to Fix It

### 1. Check Server Role

```cypher
CALL dbms.cluster.overview() YIELD addresses, role
RETURN addresses, role;
```

### 2. Route Writes to Leader

```python
# Use routing table for write operations
with driver.session(default_access_mode="WRITE") as session:
    session.run("CREATE (n:User {name: $name})", name="Alice")
```

### 3. Set Database to Read/Write

```cypher
ALTER DATABASE neo4j SET ACCESS READ WRITE;
```

## Examples

```cypher
CALL dbms.cluster.overview() YIELD id, addresses, role;
```
