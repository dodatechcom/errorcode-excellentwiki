---
title: "[Solution] Cassandra Connection Error - Fix Driver Connectivity"
description: "Fix Cassandra driver connection errors by verifying the host address and port, configuring SSL and TLS settings, and ensuring driver-to-server version compatibi"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra connection error occurs when the client driver cannot establish a TCP connection to a Cassandra node. This is distinct from `NoHostAvailableException` because it typically involves a specific connection failure rather than all hosts being unreachable.

## What This Error Means

Connection errors surface when the driver attempts to open a socket to a Cassandra node and the OS or network rejects the connection. Common error messages include `Connection refused`, `Connection timed out`, or `Unable to connect`. The driver may also fail during the CQL protocol handshake after the TCP connection is established.

## Why It Happens

- Cassandra is not listening on the configured port (default 9042)
- Wrong IP address or hostname in the connection string
- Cassandra is bound to `127.0.0.1` and the driver connects from a remote host
- SSL/TLS handshake failure when encryption is required
- Driver version is incompatible with the Cassandra server version
- Too many concurrent connections exhausting server resources
- DNS resolution failure for the configured hostname

## How to Fix It

### 1. Verify Cassandra is Listening

```bash
ss -tlnp | grep 9042
# Expected: LISTEN 0 128 0.0.0.0:9042
```

### 2. Check Cassandra Listen Address

```yaml
# cassandra.yaml
listen_address: 0.0.0.0
rpc_address: 0.0.0.0
native_transport_port: 9042
```

### 3. Test the Connection Manually

```bash
cqlsh 10.0.1.5 9042
# Or with SSL
cqlsh --ssl 10.0.1.5 9042
```

### 4. Configure the Driver Correctly

```java
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.5", 9042))
    .withLocalDatacenter("datacenter1")
    .withKeyspace("my_keyspace")
    .withConnectionPoolOptions(
        ConnectionPoolOptions.builder()
            .setMaxQueueSize(1024)
            .build()
    )
    .build();
```

### 5. Check SSL Configuration

```java
SSLContext sslContext = SSLContext.getInstance("TLS");
// Load truststore and keystore
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.5", 9042))
    .withSslContext(sslContext)
    .withLocalDatacenter("datacenter1")
    .build();
```

### 6. Increase Driver Timeouts

```java
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.5", 9042))
    .withConfigLoader(DriverConfigLoader.fromString(
        "advanced.connection.connect-timeout = 10s"
    ))
    .build();
```

## Common Mistakes

- Using the broadcast address instead of the listen address in the driver config
- Not specifying `withLocalDatacenter()` which causes connection routing issues
- Forgetting to open port 9042 in the cloud security group or firewall
- Running an older driver (e.g., 3.x) against Cassandra 4.x without upgrading

## Related Pages

- [Cassandra NoHostAvailableException](/tools/cassandra/cassandra-unavailable)
- [Cassandra Authentication Error](/tools/cassandra/cassandra-authentication-error)
- [Cassandra Schema Error](/tools/cassandra/cassandra-schema-error)
