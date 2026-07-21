---
title: "[Solution] ScyllaDB Uptime Status Error — How to Fix"
description: "Fix ScyllaDB uptime status errors when the node reports incorrect uptime or restart counts"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Uptime Status Error

Uptime status errors occur when ScyllaDB nodes report incorrect uptime values or frequent unexpected restarts that indicate underlying stability issues.

## Why It Happens

- Node has crashed and restarted unexpectedly
- OOM killer terminated the ScyllaDB process
- Watchdog timeout caused automatic restart
- Configuration error triggers immediate shutdown
- Systemd service keeps restarting ScyllaDB

## Common Error Messages

```
Node restarted 5 times in the last hour
```

```
ERROR: ScyllaDB process terminated unexpectedly
```

```
watchdog: restarting ScyllaDB due to timeout
```

## How to Fix It

### 1. Check System Logs

```bash
sudo journalctl -u scylla-server --since "1 hour ago" | grep -i -E "restart|crash|oom|killed"
```

### 2. Check OOM Killer

```bash
dmesg | grep -i "oom\|killed process"
sudo journalctl -k | grep -i "oom"
```

### 3. Monitor Restart Count

```bash
systemctl show scylla-server -p NRestarts
```

### 4. Fix Configuration Issues

```bash
# Validate configuration
scylla --validate /etc/scylla/scylla.yaml
```

## Examples

```
$ systemctl show scylla-server -p NRestarts
NRestarts=12

$ dmesg | grep oom
[12345.678] Out of memory: Killed process 1234 (scylla) total-vm:8388608kB
```

## Prevent It

- Monitor node restart counts with Scylla Monitoring
- Set up OOM killer score adjustments for ScyllaDB
- Review logs after any unexpected restart

## Related Pages

- [ScyllaDB Uptime Error](/tools/scylladb/scylladb-uptime-error)
- [ScyllaDB Memory Error](/tools/scylladb/scylladb-memory-error)
- [ScyllaDB Node Error](/tools/scylladb/scylladb-node-error)
