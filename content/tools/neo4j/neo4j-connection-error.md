---
title: "[Solution] Neo4j Connection Error — How to Fix"
description: "Fix Neo4j connection errors including Bolt and HTTP interface issues, authentication failures, and pool exhaustion in Neo4j databases"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Connection Error

Neo4j connection errors occur when clients cannot establish connections via Bolt or HTTP protocols. This includes refused connections, authentication failures, pool exhaustion, and TLS handshake issues.

## Why It Happens

- Neo4j is bound to localhost and the client connects remotely
- The Bolt port (7687) or HTTP port (7474) is not open
- The connection pool is exhausted by long-running transactions
- Authentication credentials are incorrect
- The client and server Bolt protocol versions are incompatible
- TLS/SSL certificates are missing or expired

## Common Error Messages

```
Neo.ClientError.Security.Unauthorized: The client is unauthorized due to authentication failure
```

```
Neo.ClientError.Security.Unauthorized: Invalid username or password
```

```
Neo.TransientError.Network.ConnectionPoolTimeout:
Connection timeout. Ensure the database is up and accessible
```

```
Neo.ClientError.Protocol.ServiceUnavailable:
The connection has been closed by the server
```

## How to Fix It

### 1. Check Neo4j Service Status

```bash
sudo systemctl status neo4j
neo4j status
```

### 2. Fix Bolt Connectivity

```bash
# Check if Bolt is listening
ss -tlnp | grep 7687

# In /etc/neo4j/neo4j.conf
server.bolt.listen_address=0.0.0.0:7687
server.http.listen_address=0.0.0.0:7474
```

```bash
sudo systemctl restart neo4j
```

### 3. Fix Authentication

```bash
# Reset password (stop Neo4j first)
sudo systemctl stop neo4j
neo4j-admin dbms set-initial-password mypassword
sudo systemctl start neo4j
```

### 4. Increase Connection Pool

```javascript
// In application driver config
const driver = neo4j.driver(
  'bolt://localhost:7687',
  neo4j.auth.basic('neo4j', 'password'),
  { maxConnectionPoolSize: 200, connectionAcquisitionTimeout: 60000 }
);
```

### 5. Fix Firewall

```bash
sudo ufw allow 7687/tcp
sudo ufw allow 7474/tcp
```

## Common Scenarios

- **New deployment with remote access**: Set `server.bolt.listen_address` to `0.0.0.0`.
- **Connection pool exhaustion**: Increase pool size and reduce transaction duration.
- **TLS handshake failure**: Ensure certificates are valid and properly configured.

## Prevent It

- Use connection pooling in the application driver
- Monitor connection count with `CALL dbms.listConnections()`
- Set up health checks on both Bolt and HTTP ports

## Related Pages

- [Neo4j Auth Error](/tools/neo4j/neo4j-auth-error)
- [Neo4j Bolt Error](/tools/neo4j/neo4j-bolt-error)
- [Neo4j Memory Error](/tools/neo4j/neo4j-memory-error)
