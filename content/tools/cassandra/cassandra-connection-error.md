---
title: "[Solution] Cassandra Connection Error — How to Fix"
description: "Fix Cassandra connection errors by resolving seed node issues, tuning timeout settings, repairing network configuration, and restoring cluster health."
tools: ["cassandra"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra connection error occurs when a client application or node cannot establish a TCP connection to the Cassandra cluster. This prevents all read and write operations and is one of the most common operational issues in Cassandra deployments.

## Why It Happens

Connection errors in Cassandra typically stem from infrastructure misconfigurations or cluster instability. Understanding the root cause requires examining the network path, node health, and driver configuration together.

- Seed nodes are unreachable or down, preventing cluster bootstrapping
- The native transport port (default 9042) is blocked by firewalls or security groups
- The client driver is configured with incorrect contact points or datacenter names
- Cassandra nodes have exhausted file descriptors or thread pools under heavy load
- Network partitions isolate the client from all available coordinator nodes
- TLS configuration mismatches between client and server prevent handshake completion
- DNS resolution fails for seed node hostnames in containerized environments

## Common Error Messages

```text
NoHostAvailableException: All host(s) tried for query failed (tried: /10.0.1.1:9042, /10.0.1.2:9042)
```

This indicates every contact point in the driver was unreachable. The cluster may be fully down or the network is blocking all traffic.

```text
TransportException: [/10.0.1.1:9042] Cannot connect to Cassandra cluster
```

A specific node refused the connection. The node may be down, overloaded, or the port may be incorrect.

```text
OperationTimedOutException: Timed out waiting for server response
```

The TCP connection succeeded but Cassandra did not respond within the driver timeout. This often indicates a overloaded coordinator or GC pause.

```text
javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake_failure
```

The TLS handshake failed. This usually means mismatched certificates, unsupported TLS versions, or missing CA trust chain.

## How to Fix It

### 1. Verify Seed Node Reachability

```bash
# Check if seed nodes are alive
nodetool status

# Test TCP connectivity from the client
nc -zv 10.0.1.1 9042

# Check Cassandra process on the node
ps aux | grep cassandra
```

Ensure at least one seed node is running and reachable. Cassandra requires seed nodes during startup to form the cluster ring.

### 2. Configure Contact Points Correctly

```java
// Java driver 4.x
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.1", 9042))
    .addContactPoint(new InetSocketAddress("10.0.1.2", 9042))
    .withLocalDatacenter("datacenter1")
    .withAuthCredentials("cassandra", "cassandra_password")
    .build();
```

```python
# Python driver
from cassandra.cluster import Cluster

cluster = Cluster(
    contact_points=['10.0.1.1', '10.0.1.2'],
    port=9042,
    auth_provider=PlainTextAuthProvider(
        username='cassandra',
        password='cassandra_password'
    )
)
session = cluster.connect()
```

Always provide at least two contact points so the driver can recover if one node is down. Match the datacenter name to your actual topology.

### 3. Tune Timeouts and Retries

```yaml
# cassandra.yaml
native_transport_max_threads: 128
native_transport_max_frame_size_in_mb: 16
```

```java
// Driver timeout configuration
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.1", 9042))
    .withLocalDatacenter("datacenter1")
    .withConfigLoader(DriverConfigLoader.fromString(
        """" +
        "advanced.connection.pool.local.size = 5\n" +
        "advanced.reconnection-policy.class = ExponentialReconnectionPolicy\n" +
        "advanced.reconnection-policy.max-delay = 60s\n" +
        "basic.request.timeout = 10s\n" +
        """"))
    .build();
```

Increase the native transport thread pool if connections are timing out under load. Use exponential backoff reconnection to handle transient failures.

### 4. Open Firewall Ports

```bash
# Allow Cassandra native transport
sudo ufw allow from 10.0.0.0/8 to any port 9042

# Allow inter-node gossip
sudo ufw allow from 10.0.0.0/8 to any port 7000

# Allow inter-node SSL gossip
sudo ufw allow from 10.0.0.0/8 to any port 7001
```

### 5. Fix TLS Configuration

```yaml
# cassandra.yaml
client_encryption_options:
  enabled: true
  keystore: /etc/cassandra/keystore.jks
  keystore_password: changeit
  truststore: /etc/cassandra/truststore.jks
  truststore_password: changeit
  require_client_auth: false
```

```bash
# Verify certificate expiry
keytool -list -v -keystore /etc/cassandra/keystore.jks -storepass changeit | grep -A2 "Valid from"
```

## Common Scenarios

**Docker containers cannot connect to Cassandra nodes.** The default Cassandra configuration binds to localhost. Set `rpc_address: 0.0.0.0` in cassandra.yaml and ensure the container exposes port 9042 in the Docker Compose or Kubernetes pod spec.

**Kubernetes pods lose connection after node restart.** The Cassandra service or StatefulSet DNS may not have updated. Use headless services with predictable pod hostnames and ensure the seed provider configuration points to stable DNS entries rather than IP addresses.

**Connection pool exhaustion under high concurrency.** The default local pool size may be too small. Increase `advanced.connection.pool.local.size` in the driver config and monitor active connections with `nodetool tpstats`.

## Prevent It

- Always provide multiple seed nodes across different availability zones and verify they remain reachable during deployments
- Monitor node health with Prometheus and Grafana using the Cassandra exporter to detect connectivity degradation before clients fail
- Use connection pool sizing guidelines: one connection per 100-200 concurrent requests for Java driver 4.x, and test failover by randomly killing nodes in staging
