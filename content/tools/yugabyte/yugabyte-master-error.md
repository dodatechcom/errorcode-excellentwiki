---
title: "[Solution] YugabyteDB Master Error — How to Fix"
description: "Fix YugabyteDB Master errors by recovering from Master failures, resolving cluster metadata issues, and fixing Raft consensus problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Master Error

YugabyteDB Master errors occur when the Master process fails. Masters manage cluster metadata, tablet placement, and DDL operations.

## Why It Happens

- Master process crashed or is not running
- Master quorum is lost (need 3 of 5 masters)
- Cluster metadata is corrupted
- Master cannot allocate tablets
- DNS resolution fails for Master nodes
- Master data directory is corrupted

## Common Error Messages

```
ERROR: Master is not running
```

```
ERROR: could not connect to Master
```

```
FATAL: Master quorum lost
```

```
ERROR: cluster metadata corruption
```

## How to Fix It

### 1. Check Master Status

```bash
# Check Master process
ps aux | grep yb-master

# Check Master health
curl http://yb-master-1:7000/healthz

# Check Master logs
tail -100 /home/yugabyte/yugabyte-data/master/logs/yb-master.INFO

# List Master peers
/home/yugabyte/master/bin/yb-admin list_masters
```

### 2. Restart Master

```bash
# Restart Master
sudo systemctl restart yugabyte-master

# Check if Master joined quorum
/home/yugabyte/master/bin/yb-admin list_masters

# Verify cluster health
curl http://yb-master-1:7000/cluster-config
```

### 3. Fix Master Quorum

```bash
# If majority of Masters are down, manual intervention needed
# For 3-Master setup: need at least 2 Masters up

# Check Master addresses
/home/yugabyte/master/bin/yb-admin list_masters

# If Master is unreachable, try restarting with correct flags
# In master.gflags:
--master_addresses=yb-master-1:7100,yb-master-2:7100,yb-master-3:7100
--fs_data_dirs=/home/yugabyte/yugabyte-data/master
```

### 4. Monitor Master Health

```bash
# Check Master metrics
curl http://yb-master-1:7000/metrics

# Monitor tablet allocation
/home/yugabyte/master/bin/yb-admin list_tablet_servers

# Check cluster config
curl http://yb-master-1:7000/cluster-config | jq .
```

## Common Scenarios

- **Master quorum lost**: Restart Masters one by one and verify Raft consensus.
- **Master won't start**: Check `--master_addresses` and data directory permissions.
- **Cluster metadata corrupted**: Restore from backup or rebuild cluster.

## Prevent It

- Use odd number of Masters (3 or 5) for proper quorum
- Monitor Master health with `/healthz` endpoint
- Back up Master data directory regularly

## Related Pages

- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Tablet Error](/tools/yugabyte/yugabyte-tablet-error)
