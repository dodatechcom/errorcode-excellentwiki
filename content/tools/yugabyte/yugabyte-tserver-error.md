---
title: "[Solution] YugabyteDB TServer Error — How to Fix"
description: "Fix YugabyteDB TServer errors by recovering from crashes, resolving tablet leader issues, and fixing memory and disk problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB TServer Error

YugabyteDB TServer errors occur when the Tablet Server process fails, crashes, or cannot serve requests. TServers store data and serve read/write operations.

## Why It Happens

- TServer process crashed due to OOM
- Tablet leader cannot be elected
- Disk space is full on TServer data directory
- Memory limit is exceeded
- Raft consensus is broken
- TServer cannot communicate with Master

## Common Error Messages

```
ERROR: TServer is not running
```

```
ERROR: tablet leader not found
```

```
FATAL: out of memory
```

```
ERROR: failed to write to disk
```

## How to Fix It

### 1. Check TServer Status

```bash
# Check TServer process
ps aux | grep yb-tserver

# Check TServer health
curl http://yb-tserver-1:9000/healthz

# Check TServer logs
tail -100 /home/yugabyte/yugabyte-data/tserver/logs/yb-tserver.INFO

# Check tablet status
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers
```

### 2. Fix TServer Crash

```bash
# Restart TServer
sudo systemctl restart yugabyte-tserver

# Check for OOM kills
dmesg | grep -i oom

# Increase memory limits
# In tserver.gflags:
--memory_limit_hard_bytes=8589934592  # 8GB
--db_mem_limit_bytes=4294967296       # 4GB
```

### 3. Fix Tablet Issues

```bash
# List tablets
/home/yugabyte/tserver/bin/yb-admin list_tables

# Check tablet leader status
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers

# Move tablet leader if needed
/home/yugabyte/tserver/bin/yb-admin move_tablet_leader <tablet_id> <dest_tserver>
```

### 4. Monitor TServer Health

```bash
# Check TServer metrics
curl http://yb-tserver-1:9000/metrics

# Monitor tablet count
/home/yugabyte/tserver/bin/yb-admin list_tablet_servers | wc -l

# Check disk usage
df -h /home/yugabyte/yugabyte-data/tserver/
```

## Common Scenarios

- **TServer keeps crashing**: Check memory limits and disk space.
- **Tablet leader not available**: Ensure enough TServer replicas for Raft quorum.
- **TServer won't start**: Check configuration files and logs for errors.

## Prevent It

- Monitor TServer health with `/healthz` endpoint
- Set up alerts for tablet leader elections
- Reserve adequate disk space for data growth

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Master Error](/tools/yugabyte/yugabyte-master-error)
