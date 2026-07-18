---
title: "[Solution] ClickHouse Connection Error — How to Fix"
description: "Fix ClickHouse connection errors including refused connections, timeout issues, TLS handshake failures, and max connection limits"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Connection Error

ClickHouse connection errors occur when clients cannot establish TCP or HTTP connections to the ClickHouse server. This includes refused connections, timeouts, authentication failures, and max connection limit issues.

## Why It Happens

- ClickHouse is bound to localhost and the client connects remotely
- The `<listen_host>` config is set to `127.0.0.1` only
- The `max_concurrent_queries` limit is reached
- Firewall blocks port 8123 (HTTP) or 9000 (native TCP)
- TLS/SSL is required but client does not provide certificates
- The ClickHouse service is stopped or crashed
- Network latency or packet loss causes connection timeouts

## Common Error Messages

```
Code: 210. DB::Exception: Connection refused (127.0.0.1:9000)
```

```
Poco::Exception. Code: 1000, e.code() = 111,
e.displayText() = Connection refused
```

```
Code: 202. DB::Exception: Too many simultaneous queries
```

```
Code: 210. DB::Exception: Connection reset by peer
```

## How to Fix It

### 1. Configure listen_host for Remote Access

```xml
<!-- In /etc/clickhouse-server/config.xml -->
<listen_host>::</listen_host>
<!-- Or for specific interface -->
<!-- <listen_host>0.0.0.0</listen_host> -->
```

```bash
sudo systemctl restart clickhouse-server
```

### 2. Increase max_concurrent_queries

```xml
<!-- In config.xml -->
<max_concurrent_queries>200</max_concurrent_queries>
```

```sql
-- Check current setting
SELECT name, value FROM system.settings WHERE name = 'max_concurrent_queries';
```

### 3. Check Firewall and Port

```bash
# Verify ClickHouse is listening
ss -tlnp | grep -E '(8123|9000)'

# Check firewall
sudo ufw status | grep 8123
sudo ufw allow 8123/tcp
sudo ufw allow 9000/tcp
```

### 4. Fix TLS Connection Issues

```xml
<!-- In config.xml -->
<https_port>8443</https_port>
<tcp_port_secure>9440</tcp_port_secure>
<certificateFile>/etc/clickhouse-server/server.crt</certificateFile>
<privateKeyFile>/etc/clickhouse-server/server.key</privateKeyFile>
```

### 5. Test Connection

```bash
# HTTP interface
curl 'http://localhost:8123/?query=SELECT%20version()'

# Native TCP interface
clickhouse-client --query "SELECT version()"

# With credentials
clickhouse-client --user default --password mypass --query "SELECT 1"
```

## Common Scenarios

- **New deployment with remote access**: Set `listen_host` to `::` and open firewall ports.
- **Connection pool exhaustion**: Increase `max_concurrent_queries` or add connection pooling.
- **TLS handshake failure**: Ensure server certificate is valid and trusted by client.

## Prevent It

- Use connection pooling (ClickHouse native protocol pool) for high-concurrency applications
- Monitor `CurrentConnection` and `MaxConnection` metrics
- Set up health checks that verify connectivity on both HTTP and native ports

## Related Pages

- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse HTTP Error](/tools/clickhouse/clickhouse-http-error)
- [ClickHouse TCP Error](/tools/clickhouse/clickhouse-tcp-error)
