---
title: "[Solution] ScyllaDB Connection Error — How to Fix"
description: "Fix ScyllaDB connection errors by verifying port bindings, adjusting timeout settings, and resolving driver connection pool exhaustion"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Connection Error

ScyllaDB connection errors occur when clients cannot establish or maintain connections to the ScyllaDB cluster. These errors are common during driver configuration, network changes, or high-load scenarios.

## Why It Happens

- ScyllaDB is bound to localhost only (rpc_address not configured)
- Port 9042 (CQL) is blocked by firewall
- Client driver connection pool is exhausted
- Native transport threads are overloaded
- TLS/SSL handshake fails with incorrect certificates
- Contact points in driver config are unreachable

## Common Error Messages

```
NoHostAvailable: All host(s) tried down. Detail: 127.0.0.1:9042: ScyllaTimeoutError
```

```
OperationTimedOut: errors={127.0.0.1:9042: 'Client request timeout'}
```

```
AuthenticationError: Error from server: code=0010 [Unauthorized] ... Invalid credentials
```

```
UnavailableError: Not enough replicas available for query at consistency ONE
```

## How to Fix It

### 1. Configure rpc_address for Remote Access

```yaml
# In /etc/scylla/scylla.yaml
rpc_address: 0.0.0.0
native_transport_port: 9042
native_transport_max_threads: 128
```

```bash
sudo systemctl restart scylla-server

# Verify listening on all interfaces
ss -tlnp | grep 9042
```

### 2. Configure Driver Connection Pool

```python
# Python driver with proper pool settings
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

cluster = Cluster(
    ['10.0.0.1', '10.0.0.2', '10.0.0.3'],
    port=9042,
    connect_timeout=10,
    control_connection_timeout=30,
    protocol_version=4,
    load_balancing_policy=DCAWareRoundRobinPolicy(
        local_dc='datacenter1'
    )
)
session = cluster.connect()
```

### 3. Increase Native Transport Limits

```yaml
# In scylla.yaml
native_transport_max_threads: 128
native_transport_max_frame_size_in_mb: 16
```

```bash
# Check current connections
nodetool clientstats

# Monitor native transport metrics
nodetool tpstats | grep Native
```

### 4. Fix Firewall Rules

```bash
# Open ScyllaDB ports
sudo ufw allow 9042/tcp    # CQL native
sudo ufw allow 7000/tcp    # Inter-node
sudo ufw allow 9160/tcp    # Thrift
sudo ufw allow 7001/tcp    # SSL inter-node

# Test connection
cqlsh 10.0.0.1 9042
```

## Common Scenarios

- **Docker ScyllaDB not reachable**: Map port 9042:9042 and set `rpc_address: 0.0.0.0`.
- **Connection pool exhaustion**: Increase `pool_size` or use `DCAwareRoundRobinPolicy`.
- **Timeout after network blip**: Implement reconnection policy with exponential backoff.

## Prevent It

- Use connection pooling in your driver with appropriate pool sizes
- Monitor `ConnectedClients` and `NativeTransportMaxThreads` metrics
- Set up health checks that verify connectivity to all contact points

## Related Pages

- [ScyllaDB Auth Error](/tools/scylladb/scylladb-auth-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
- [ScyllaDB Timeout Error](/tools/scylladb/scylladb-timeout-error)
