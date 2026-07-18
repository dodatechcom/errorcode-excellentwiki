---
title: "[Solution] TiDB TiDB Node Error — How to Fix"
description: "Fix TiDB node errors by recovering from TiDB server failures, resolving node startup issues, and fixing memory and CPU problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TiDB Node Error

TiDB node errors occur when the SQL processing layer (TiDB server) fails, crashes, or cannot handle requests.

## Why It Happens

- TiDB server process crashed (OOM or bug)
- TiDB cannot connect to PD
- TiDB runs out of file descriptors
- TiDB configuration is incorrect
- TiDB port is already in use
- Too many concurrent sessions

## Common Error Messages

```
ERROR: TiDB server is not running
```

```
FATAL: TiDB server out of memory
```

```
ERROR: cannot connect to PD
```

```
ERROR: TiDB port already in use
```

## How to Fix It

### 1. Check TiDB Status

```bash
# Check TiDB process
sudo systemctl status tidb-server

# Check TiDB health
curl http://tidb1:10080/status

# Check TiDB logs
tail -50 /var/log/tidb/tidb.log

# Check listening port
ss -tlnp | grep 4000
```

### 2. Restart TiDB Server

```bash
# Restart TiDB
sudo systemctl restart tidb-server

# Verify TiDB is running
curl http://tidb1:10080/status

# Test MySQL connection
mysql -h tidb1 -P 4000 -u root
```

### 3. Fix Configuration Issues

```toml
# In tidb.toml
[server]
addr = "0.0.0.0:4000"
max_connections = 1000

[performance]
max-memory = 10737418240  # 10GB

[tikv-client]
# tikv.grpc-concurrency = 4
```

### 4. Monitor TiDB Node

```bash
# Check TiDB metrics
curl http://tidb1:10080/metrics

# Monitor connection count
curl http://tidb1:10080/status | jq '.connection'

# Check file descriptors
ls /proc/$(pgrep tidb-server)/fd | wc -l
```

## Common Scenarios

- **TiDB keeps crashing**: Check memory limits and logs for root cause.
- **TiDB cannot start**: Verify PD is running and port is not in use.
- **TiDB OOM**: Increase memory limits or add more TiDB nodes.

## Prevent It

- Monitor TiDB node health with /status endpoint
- Set up systemd to auto-restart TiDB
- Configure appropriate memory and connection limits

## Related Pages

- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
- [TiDB OOM Error](/tools/tidb/tidb-oom-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
