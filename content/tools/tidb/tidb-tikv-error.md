---
title: "[Solution] TiDB TiKV Error — How to Fix"
description: "Fix TiDB TiKV errors by resolving store failures, fixing Raft consensus issues, and handling TiKV node crashes"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TiKV Error

TiDB TiKV errors occur when the distributed key-value storage engine fails. TiKV stores all data and serves read/write operations via Raft consensus.

## Why It Happens

- TiKV process crashed or is not running
- Raft group cannot elect leader
- Store is marked as down by PD
- TiKV disk is full or has I/O errors
- Region peers are unavailable
- TiKV runs out of memory

## Common Error Messages

```
ERROR: TiKV is not available
```

```
ERROR: region peer not found
```

```
ERROR: Raft leader not found for region
```

```
FATAL: TiKV store is down
```

## How to Fix It

### 1. Check TiKV Status

```bash
# Check TiKV process
sudo systemctl status tikv-server

# Check TiKV status
curl http://tikv1:20180/status

# Check TiKV logs
tail -50 /var/log/tikv/tikv.log

# Check region status via PD
curl http://pd1:2379/pd/api/v1/regions | jq '.total_count'
```

### 2. Restart TiKV

```bash
# Restart TiKV
sudo systemctl restart tikv-server

# Check if TiKV joined cluster
curl http://pd1:2379/pd/api/v1/stores | jq '.stores[].state_name'

# Verify regions are healthy
curl http://pd1:2379/pd/api/v1/regions/check/replication
```

### 3. Fix Raft Issues

```bash
# Check region leaders
curl http://pd1:2379/pd/api/v1/regions | jq '.regions[0].peers'

# Force region leader election
# (PD automatically handles this, but check if operators are pending)
curl http://pd1:2379/pd/api/v1/schedule/operator | jq .
```

### 4. Monitor TiKV Health

```bash
# Check TiKV metrics
curl http://tikv1:20180/metrics

# Monitor region health
curl http://pd1:2379/pd/api/v1/regions/check/replication

# Check store status
curl http://pd1:2379/pd/api/v1/stores | jq '.stores[] | {id, state_name, labels}'
```

## Common Scenarios

- **TiKV down causes read/write failures**: Restart TiKV and wait for region recovery.
- **Region leader lost**: PD automatically elects new leader.
- **TiKV disk full**: Add disk space or move data to new store.

## Prevent It

- Use at least 3 TiKV nodes for redundancy
- Monitor TiKV health with PD API
- Set up alerts for store down events

## Related Pages

- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB Region Error](/tools/tidb/tidb-region-error)
- [TiDB Connection Error](/tools/tidb/tidb-connection-error)
