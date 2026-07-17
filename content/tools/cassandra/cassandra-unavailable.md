---
title: "[Solution] Cassandra NoHostAvailableException - Fix Cluster Connectivity"
description: "Fix Cassandra NoHostAvailableException by verifying all nodes are running and healthy, checking driver contact points, opening firewall ports, and testing conne"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra `NoHostAvailableException` means the client driver cannot contact any replica node that owns the requested token range. Every contacted host either refused the connection or failed to respond.

## What This Error Means

When the driver attempts to execute a query, it determines which nodes own the relevant token ranges using the cluster metadata. If every candidate host is unreachable, the driver throws `NoHostAvailableException`. This is a connectivity-level failure, not a query-level failure like `ReadTimeoutException`.

The exception message lists the attempted hosts and the individual connection errors (e.g., connection refused, unreachable host).

## Why It Happens

- All Cassandra nodes in the contact points list are down
- Firewall rules blocking the driver-to-node communication (default port 9042)
- Driver contact points are misconfigured or use wrong IPs
- Gossip protocol has not settled after a node restart
- SSL/TLS configuration mismatch between driver and nodes
- Kubernetes or cloud network policies blocking inter-pod communication
- All nodes in the datacenter are in a down state

## How to Fix It

### 1. Verify Node Status

```bash
nodetool status
# Look for UN (Up Normal) for all expected nodes
```

### 2. Check if Cassandra is Listening

```bash
ss -tlnp | grep 9042
# Should show LISTENING on port 9042
```

### 3. Verify Driver Contact Points

```java
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.5", 9042))
    .withLocalDatacenter("datacenter1")
    .build();
```

```python
# Python driver
from cassandra.cluster import Cluster
cluster = Cluster(['10.0.1.5', '10.0.1.6'], port=9042)
session = cluster.connect()
```

### 4. Test Network Connectivity

```bash
# From the application server
telnet 10.0.1.5 9042
nc -zv 10.0.1.5 9042
```

### 5. Check Firewall Rules

```bash
sudo ufw allow from 10.0.0.0/8 to any port 9042
```

### 6. Verify SSL Configuration

```java
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.5", 9042))
    .withSslContext(sslContext)
    .withLocalDatacenter("datacenter1")
    .build();
```

## Common Mistakes

- Forgetting to specify `withLocalDatacenter()` in the driver builder
- Using public IPs in the contact points when nodes communicate over private IPs
- Not waiting for gossip to settle after restarting all nodes simultaneously
- Ignoring that Kubernetes services may need time to route traffic to new pods

## Related Pages

- [Cassandra Connection Error](/tools/cassandra/cassandra-connection-error)
- [Cassandra Authentication Error](/tools/cassandra/cassandra-authentication-error)
- [Cassandra Schema Error](/tools/cassandra/cassandra-schema-error)
