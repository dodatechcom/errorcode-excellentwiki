---
title: "[Solution] Neo4j Bolt Protocol Error — How to Fix"
description: "Fix Neo4j Bolt protocol errors including connection issues, protocol version mismatches, and Bolt SSL configuration problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Bolt Protocol Error

Bolt protocol errors in Neo4j occur when clients cannot communicate via the Bolt binary protocol. This includes connection issues, protocol version incompatibilities, and SSL/TLS configuration problems.

## Why It Happens

- The Bolt port is not enabled or configured
- The client driver uses an incompatible Bolt protocol version
- SSL/TLS certificates are missing or misconfigured
- The Bolt connector thread pool is exhausted
- The firewall blocks port 7687
- The Bolt transport encounters a network error

## Common Error Messages

```
Neo.ClientError.Security.Unauthorized: The client is unauthorized
```

```
Neo.TransientError.Network.ConnectionPoolTimeout:
Connection timeout
```

```
Neo.ClientError.Protocol.ServiceUnavailable:
The connection has been closed
```

```
javax.net.ssl.SSLHandshakeException: SSL handshake failed
```

## How to Fix It

### 1. Enable and Configure Bolt

```bash
# In neo4j.conf
server.bolt.enabled=true
server.bolt.listen_address=0.0.0.0:7687
server.bolt.thread_pool_min_size=5
server.bolt.thread_pool_max_size=40
server.bolt.thread_pool_keep_alive=60
```

### 2. Fix Bolt Protocol Version

```javascript
// In the driver, specify the correct protocol version
const driver = neo4j.driver(
  'neo4j://localhost:7687',
  neo4j.auth.basic('neo4j', 'password'),
  { disableLosslessIntegers: true }
);
```

### 3. Fix Bolt SSL Configuration

```bash
# In neo4j.conf
dbms.connector.bolt.tls_level=REQUIRED
server.bolt.ssl_policy=boltSSL
server.ssl.policy=boltSSL

# SSL certificate configuration
server.bolt.ssl_key_file=/etc/neo4j/ssl/bolt.key
server.bolt.ssl_certificate_file=/etc/neo4j/ssl/bolt.crt
```

### 4. Monitor Bolt Connections

```cypher
// Check active Bolt connections
CALL dbms.listConnections()
YIELD connectionId, userAgent, elapsedTimeMillis
RETURN connectionId, userAgent, elapsedTimeMillis
ORDER BY elapsedTimeMillis DESC;

// Check Bolt connector metrics
CALL dbms.listMetrics()
YIELD name, value
WHERE name CONTAINS 'bolt'
RETURN name, value;
```

## Common Scenarios

- **Driver cannot connect to Bolt**: Ensure port 7687 is open and Bolt is enabled.
- **SSL handshake fails**: Verify certificate files exist and are valid.
- **Connection pool exhausted**: Increase `server.bolt.thread_pool_max_size` or reduce connection duration.

## Prevent It

- Use connection pooling in the driver for high-throughput applications
- Monitor Bolt connection count and thread pool usage
- Test Bolt connectivity as part of deployment validation

## Related Pages

- [Neo4j Connection Error](/tools/neo4j/neo4j-connection-error)
- [Neo4j Auth Error](/tools/neo4j/neo4j-auth-error)
- [Neo4j SSL Error](/tools/neo4j/neo4j-ssl-error)
