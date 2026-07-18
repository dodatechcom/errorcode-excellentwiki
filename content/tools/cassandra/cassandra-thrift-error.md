---
title: "[Solution] Cassandra Thrift Error — How to Fix"
description: "Fix Cassandra Thrift protocol errors by migrating to CQL, updating client libraries, enabling native transport, and resolving serialization issues."
tools: ["cassandra"]
error-types: ["thrift-error"]
severities: ["error"]
weight: 5
comments: true
---

A Cassandra Thrift error occurs when clients use the legacy Thrift RPC protocol to communicate with Cassandra. Thrift was the original client protocol but has been deprecated since Cassandra 2.1 and removed in Cassandra 4.0.

## Why It Happens

Thrift errors are migration-related issues that affect legacy applications still using the old protocol. The root cause is almost always that the client library or application code has not been updated to use the CQL native protocol.

- The application uses an old Cassandra client library that communicates via Thrift
- Thrift is disabled in cassandra.yaml but clients still attempt Thrift connections
- Cassandra 4.0+ has removed Thrift support entirely
- Serialization format differences between Thrift and CQL cause data interpretation errors
- The Thrift port (default 9160) is not configured or is blocked
- Old schema definitions created via Thrift are incompatible with CQL queries
- Thrift authentication uses different mechanisms than CQL authentication

## Common Error Messages

```text
TTransportException: Cannot read, connection is closed
```

The Thrift server is not running or the port is not listening. Thrift has been disabled or removed.

```text
InvalidRequestException: org.apache.thrift.protocol.TProtocolException: Invalid map key type
```

The Thrift client is sending data in a format that the CQL layer cannot interpret.

```text
UnsupportedOperationException: Thrift protocol is not supported in Cassandra 4.x
```

Cassandra 4.0 and later do not include Thrift support. The client must migrate to CQL.

```text
AuthenticationException: Thrift authentication is not supported. Use CQL native protocol.
```

The Thrift authentication mechanism is no longer available. Use CQL native transport instead.

## How to Fix It

### 1. Migrate to CQL Native Protocol

```python
# Old: Thrift client (deprecated)
from cassandra import ThriftClient
client = ThriftClient('10.0.1.1', 9160)
client.get_slice('users', key, slice_predicate)

# New: CQL native protocol
from cassandra.cluster import Cluster
cluster = Cluster(['10.0.1.1'], port=9042)
session = cluster.connect('my_keyspace')
rows = session.execute("SELECT * FROM users WHERE id = %s", [user_id])
```

```java
// Old: Hector or Astyanax Thrift client
// New: DataStax Java driver with CQL
CqlSession session = CqlSession.builder()
    .addContactPoint(new InetSocketAddress("10.0.1.1", 9042))
    .withLocalDatacenter("datacenter1")
    .build();
ResultSet rs = session.execute("SELECT * FROM users WHERE id = 12345");
```

### 2. Enable Native Transport if Disabled

```yaml
# cassandra.yaml — ensure native transport is enabled
native_transport_port: 9042
native_transport_max_threads: 128
native_transport_max_frame_size_in_mb: 16
```

```bash
# Verify native transport is listening
ss -tlnp | grep 9042

# Check if Thrift is still enabled (should be disabled)
ss -tlnp | grep 9160
```

### 3. Disable Thrift in cassandra.yaml

```yaml
# cassandra.yaml
start_rpc: false
rpc_port: 9160
```

```bash
# After changing cassandra.yaml, restart the node
nodetool drain
sudo systemctl restart cassandra
```

Disabling Thrift frees resources (thread pool, memory) that can be used by the CQL native transport.

### 4. Convert Thrift Schema to CQL

```cql
-- If you have Thrift-created column families, describe them first
DESCRIBE KEYSPACE my_keyspace;

-- Create equivalent CQL tables
CREATE TABLE IF NOT EXISTS users (
    user_id text PRIMARY KEY,
    name text,
    email text,
    created_at timestamp
);

-- Copy data from Thrift tables to CQL tables
INSERT INTO users (user_id, name, email)
SELECT key, name, email FROM thrift_users_table;
```

```bash
# Use sstableloader to migrate data from Thrift SSTables
sstableloader -d 10.0.1.1:9042 /var/lib/cassandra/data/my_keyspace/thrift_table-*
```

## Common Scenarios

**Legacy application stuck on Thrift after Cassandra upgrade.** Upgrade the client library first, then the Cassandra server. Test the new CQL queries against a staging cluster with the same data model before deploying to production.

**Mixed cluster with Thrift and CQL clients.** Run Cassandra 3.x with Thrift disabled (`start_rpc: false`) and all clients on CQL. This allows a phased migration without downtime.

**Data written via Thrift not readable via CQL.** Thrift stores column metadata differently. Use `sstable2json` to inspect Thrift SSTables, then write a migration script to load the data into CQL tables.

## Prevent It

- Audit all Cassandra client libraries across the organization and ensure none depend on Thrift before upgrading to Cassandra 4.0
- Use a proxy layer like the DataStax proxy to translate legacy Thrift calls to CQL during migration
- Add integration tests that verify all client connections use port 9042 (CQL) and not port 9160 (Thrift)
