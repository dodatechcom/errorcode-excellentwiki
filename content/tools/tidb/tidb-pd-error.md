---
title: "[Solution] TiDB PD Error — How to Fix"
description: "Fix TiDB PD errors by resolving Placement Driver failures, fixing PD cluster quorum, and handling PD metadata issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB PD Error

TiDB PD (Placement Driver) errors occur when the central cluster manager fails to coordinate, schedule, or allocate resources.

## Why It Happens

- PD server process crashed or is not running
- PD quorum is lost (need 2 of 3 PD nodes)
- PD metadata is corrupted
- PD cannot schedule region operators
- PD disk is full or has I/O errors
- PD configuration is incorrect

## Common Error Messages

```
ERROR: PD cluster is not healthy
```

```
ERROR: PD cannot schedule regions
```

```
FATAL: PD is not running
```

```
ERROR: PD metadata corruption
```

## How to Fix It

### 1. Check PD Status

```bash
# Check PD process
sudo systemctl status pd-server

# Check PD cluster status
curl http://pd1:2379/pd/api/v1/cluster/status

# Check PD members
curl http://pd1:2379/pd/api/v1/members

# Check PD health
curl http://pd1:2379/pd/api/v1/health
```

### 2. Restart PD

```bash
# Restart PD server
sudo systemctl restart pd-server

# Check PD logs
tail -50 /var/log/pd/pd.log

# Verify PD is serving requests
curl http://pd1:2379/pd/api/v1/cluster/status
```

### 3. Fix PD Quorum

```bash
# If majority of PD nodes are down
# For 3-PD setup: need at least 2 PDs

# Check PD addresses
# In pd.toml:
[initial-cluster]
name = "pd1"
client-urls = "http://pd1:2379"
peer-urls = "http://pd1:2380"

# Restart PD nodes one by one
for pd in pd1 pd2 pd3; do
  ssh $pd "sudo systemctl restart pd-server"
  sleep 10
done
```

### 4. Monitor PD Health

```bash
# Check PD metrics
curl http://pd1:2379/pd/api/v1/metrics

# Monitor region status
curl http://pd1:2379/pd/api/v1/stats/region

# Check scheduler status
curl http://pd1:2379/pd/api/v1/schedulers
```

## Common Scenarios

- **PD quorum lost**: Restart PD nodes and verify Raft consensus.
- **PD cannot schedule**: Check region status and operator queue.
- **PD disk full**: Free disk space or move PD data directory.

## Prevent It

- Use odd number of PD nodes (3 or 5)
- Monitor PD health with health endpoint
- Back up PD metadata regularly

## Related Pages

- [TiDB TSO Error](/tools/tidb/tidb-tso-error)
- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
