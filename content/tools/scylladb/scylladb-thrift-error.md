---
title: "[Solution] ScyllaDB Thrift Error — How to Fix"
description: "Fix ScyllaDB Thrift errors by enabling the Thrift interface, resolving compatibility issues, and migrating to native CQL protocol"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Thrift Error

ScyllaDB Thrift errors occur when clients try to use the legacy Thrift API, which is deprecated in modern ScyllaDB versions. Migration to the native CQL protocol is recommended.

## Why It Happens

- Thrift interface is not enabled in ScyllaDB configuration
- Client application uses legacy Thrift protocol
- Thrift port (9160) is blocked by firewall
- Thrift authentication is not configured
- ScyllaDB version does not support Thrift
- Thrift binary protocol version mismatch

## Common Error Messages

```
ThriftError: Thrift protocol is not enabled
```

```
TTransportException: Cannot connect to host localhost:9160
```

```
AuthenticationError: Thrift authentication failed
```

```
ProtocolError: Unsupported Thrift version
```

## How to Fix It

### 1. Enable Thrift Interface

```yaml
# In scylla.yaml
start_rpc: true
rpc_port: 9160
```

```bash
# Restart ScyllaDB
sudo systemctl restart scylla-server

# Verify Thrift is listening
ss -tlnp | grep 9160

# Test Thrift connection
thrift-cli --host localhost --port 9160
```

### 2. Configure Thrift Authentication

```yaml
# In scylla.yaml
authenticator: PasswordAuthenticator
rpc_server_type: synchronous
thrift_framed_transport_size_in_mb: 15
```

### 3. Migrate to Native CQL Protocol

```python
# OLD: Thrift client (deprecated)
# from cassandra import Cassandra
# client = Cassandra('localhost', 9160)

# NEW: Native CQL protocol
from cassandra.cluster import Cluster
cluster = Cluster(['10.0.0.1'], port=9042)
session = cluster.connect('mykeyspace')
```

```java
// OLD: Thrift client
// CassandraClient client = new CassandraClient("localhost", 9160);

// NEW: Native CQL protocol
CqlSession session = CqlSession.builder()
    .withLocalDatacenter("datacenter1")
    .build();
```

### 4. Disable Thrift (Recommended)

```yaml
# In scylla.yaml - disable Thrift
start_rpc: false

# Restart ScyllaDB
sudo systemctl restart scylla-server

# Verify Thrift is disabled
ss -tlnp | grep 9160
# Should return no results
```

## Common Scenarios

- **Legacy application uses Thrift**: Migrate to native CQL driver.
- **Thrift connection refused**: Enable `start_rpc: true` or migrate to CQL.
- **Performance issues with Thrift**: CQL protocol is faster and more feature-rich.

## Prevent It

- Use native CQL protocol for all new applications
- Plan migration from Thrift to CQL for legacy applications
- Monitor Thrift usage and disable when no longer needed

## Related Pages

- [ScyllaDB Connection Error](/tools/scylladb/scylladb-connection-error)
- [ScyllaDB CQL Error](/tools/scylladb/scylladb-cql-error)
- [ScyllaDB Auth Error](/tools/scylladb/scylladb-auth-error)
