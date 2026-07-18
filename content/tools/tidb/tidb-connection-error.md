---
title: "[Solution] TiDB Connection Error — How to Fix"
description: "Fix TiDB connection errors by verifying TiDB server status, resolving PD connectivity issues, and fixing driver connection pool problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Connection Error

TiDB connection errors occur when clients cannot connect to TiDB servers. TiDB is a distributed SQL database with separate components (TiDB, PD, TiKV).

## Why It Happens

- TiDB server is not running or has crashed
- Port 4000 (MySQL protocol) is blocked by firewall
- PD (Placement Driver) is unreachable
- TiKV stores are not available
- DNS resolution fails for TiDB hostnames
- Connection pool is exhausted

## Common Error Messages

```
ERROR: Cannot connect to TiDB server
```

```
ERROR: PD is not reachable
```

```
ERROR: TiKV store is not available
```

```
FATAL: Connection refused
```

## How to Fix It

### 1. Check TiDB Status

```bash
# Check TiDB server process
sudo systemctl status tidb-server

# Check TiDB logs
tail -50 /var/log/tidb/tidb.log

# Test MySQL connection
mysql -h 127.0.0.1 -P 4000 -u root

# Check all components
curl http://pd1:2379/pd/api/v1/cluster/status
```

### 2. Fix TiDB Server Issues

```bash
# Start TiDB server
sudo systemctl start tidb-server

# Check listening ports
ss -tlnp | grep -E '(4000|2379|20160|20180)'

# Verify TiDB is running
curl http://tidb1:10080/status
```

### 3. Fix PD Connectivity

```bash
# Check PD cluster status
curl http://pd1:2379/pd/api/v1/cluster/status

# Check PD members
curl http://pd1:2379/pd/api/v1/members

# Restart PD if needed
sudo systemctl restart pd-server
```

### 4. Fix Network and Firewall

```bash
# Open required ports
sudo ufw allow 4000/tcp    # TiDB SQL
sudo ufw allow 2379/tcp    # PD client
sudo ufw allow 2380/tcp    # PD peer
sudo ufw allow 20160/tcp   # TiKV
sudo ufw allow 20180/tcp   # TiKV status

# Test connectivity
nc -zv tidb1 4000
nc -zv pd1 2379
```

## Common Scenarios

- **New deployment cannot connect**: Ensure all PD nodes are running first.
- **Connection timeout during peak**: Increase connection pool and TiDB instances.
- **PD down causes connection failures**: Ensure PD quorum is maintained.

## Prevent It

- Use connection pooling for applications
- Monitor PD and TiKV health
- Set up DNS resolution for all TiDB components

## Related Pages

- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
- [TiDB Auth Error](/tools/tidb/tidb-auth-error)
