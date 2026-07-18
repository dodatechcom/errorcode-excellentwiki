---
title: "[Solution] YugabyteDB Connection Error — How to Fix"
description: "Fix YugabyteDB connection errors by verifying TServer status, resolving network issues, and fixing driver connection pool exhaustion"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Connection Error

YugabyteDB connection errors occur when clients cannot establish connections to TServer or Master nodes. These errors are common during cluster setup, network changes, or high-load scenarios.

## Why It Happens

- TServer is not running or has crashed
- Port 5433 (YSQL) or 9042 (YCQL) is blocked by firewall
- Master nodes are not accessible for tablet leader discovery
- Client driver connection pool is exhausted
- DNS resolution fails for node hostnames
- RPC bindings are configured for localhost only

## Common Error Messages

```
FATAL: could not connect to server: Connection refused
```

```
ERROR: Timed out: Failed to connect to TServer
```

```
yb::rpc::RpcError: TCP connection to yb-tserver:9042 failed
```

```
FATAL: no pg_hba.conf entry for host "10.0.0.5"
```

## How to Fix It

### 1. Check TServer Status

```bash
# Check TServer process
sudo systemctl status yugabyte-tserver

# Check TServer logs
tail -50 /home/yugabyte/yugabyte-data/tserver/logs/yb-tserver.INFO

# Verify TServer is listening
ss -tlnp | grep -E '(5433|9042|9100)'

# Test YSQL connection
ysqlsh -h localhost -p 5433 -U yugabyte
```

### 2. Fix RPC Bindings

```bash
# In tserver.gflags:
--rpc_bind_addresses=0.0.0.0:9100
--server_broadcast_addresses=yb-tserver-1:9100

# In master.gflags:
--rpc_bind_addresses=0.0.0.0:7100
--server_broadcast_addresses=yb-master-1:7100
```

### 3. Configure pg_hba.conf

```bash
# Edit YugabyteDB pg_hba.conf
# Located at: /home/yugabyte/yugabyte-data/master/pg_hba.conf

# Allow all connections (development only)
# host all all 0.0.0.0/0 trust

# Allow specific subnet (production)
# host all all 10.0.0.0/8 md5
```

### 4. Fix Network and DNS

```bash
# Verify node connectivity
ping yb-master-1
ping yb-tserver-1

# Check firewall rules
sudo ufw status | grep -E '(5433|9042|7100|9100)'
sudo ufw allow 5433/tcp   # YSQL
sudo ufw allow 9042/tcp   # YCQL
sudo ufw allow 7100/tcp   # Master RPC
sudo ufw allow 9100/tcp   # TServer RPC
```

## Common Scenarios

- **Docker deployment not reachable**: Map ports explicitly and set `rpc_bind_addresses=0.0.0.0`.
- **Connection timeout during high load**: Increase connection pool size and add more TServer nodes.
- **pg_hba.conf rejects connection**: Add appropriate host entries for client IPs.

## Prevent It

- Use connection pooling (PgBouncer) for high-concurrency applications
- Monitor TServer and Master health with `/healthz` endpoint
- Set up DNS resolution for all node hostnames

## Related Pages

- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Master Error](/tools/yugabyte/yugabyte-master-error)
- [YugabyteDB Auth Error](/tools/yugabyte/yugabyte-auth-error)
