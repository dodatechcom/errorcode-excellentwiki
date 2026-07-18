---
title: "[Solution] ClickHouse TCP Interface Error — How to Fix"
description: "Fix ClickHouse native TCP protocol errors including connection issues, protocol version mismatches, and performance problems"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse TCP Interface Error

TCP interface errors in ClickHouse occur when using the native TCP protocol (port 9000). This is the high-performance protocol used by the clickhouse-client and most drivers.

## Why It Happens

- The TCP port is not enabled in the configuration
- The client and server protocol versions are incompatible
- The connection pool is exhausted
- Network firewall blocks port 9000
- The TCP keepalive settings cause premature disconnection
- The query response exceeds the TCP buffer size

## Common Error Messages

```
Code: 210. DB::Exception: Connection refused (localhost:9000)
```

```
Code: 227. DB::Exception: Packet too large
```

```
Code: 1000. DB::Exception: Poco::Net::NetException: Connection reset by peer
```

```
Code: 33. DB::Exception: Cannot read all data in TCP packet
```

## How to Fix It

### 1. Enable TCP Interface

```xml
<tcp_port>9000</tcp_port>
<tcp_port_secure>9440</tcp_port_secure>
```

### 2. Fix Protocol Version Mismatch

```bash
# Check server version
clickhouse-client --query "SELECT version()"

# Update client driver to match server version
pip install clickhouse-connect  # Python
# Or update the JDBC/ODBC driver
```

### 3. Fix Connection Pool Issues

```bash
# Increase max connections on server
<max_concurrent_queries>200</max_concurrent_queries>

# Use connection pooling in the client application
# Example with Python:
# pool = ClickHousePool(host='localhost', port=9000, min_size=2, max_size=10)
```

### 4. Fix TCP Keepalive Settings

```bash
# Check TCP keepalive settings
sysctl net.ipv4.tcp_keepalive_time
sysctl net.ipv4.tcp_keepalive_intvl
sysctl net.ipv4.tcp_keepalive_probes

# Adjust for ClickHouse connections
sudo sysctl -w net.ipv4.tcp_keepalive_time=60
sudo sysctl -w net.ipv4.tcp_keepalive_intvl=10
sudo sysctl -w net.ipv4.tcp_keepalive_probes=6
```

## Common Scenarios

- **Client connects to wrong port**: Ensure client uses port 9000 (TCP) or 8123 (HTTP).
- **Connection reset after idle period**: Configure TCP keepalive on both client and server.
- **Protocol mismatch after upgrade**: Update client drivers to match the new server version.

## Prevent It

- Use connection pooling for high-throughput applications
- Monitor TCP connection count and pool health
- Test TCP connectivity as part of deployment validation

## Related Pages

- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
- [ClickHouse HTTP Error](/tools/clickhouse/clickhouse-http-error)
- [ClickHouse User Error](/tools/clickhouse/clickhouse-user-error)
