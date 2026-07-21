---
title: "[Solution] TiDB TSO Error — How to Fix"
description: "Fix TiDB TSO (Timestamp Oracle) errors when the PD cannot allocate timestamps for transactions"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB TSO Error

TSO errors occur when TiDB cannot allocate timestamps from the PD's Timestamp Oracle, preventing transactions from starting or committing.

## Why It Happens

- PD is overloaded and cannot serve TSO requests
- PD leader is unavailable or has changed
- Network latency to PD causes TSO timeout
- Clock synchronization issues between PD nodes
- PD storage disk is full

## Common Error Messages

```
ERROR 9004: PD server timeout, please try again later
```

```
error: TSO allocation failed: PD is unreachable
```

```
PD: unable to allocate timestamp, leader election in progress
```

## How to Fix It

### 1. Check PD Health

```bash
pd-ctl member list
pd-ctl tso
```

### 2. Verify PD Connectivity

```bash
curl -s http://pd:2379/pd/api/v1/leader
```

### 3. Increase PD Resources

```toml
# In pd.toml
[pd-server]
# Increase TSO update interval if needed
```

### 4. Check PD Disk Usage

```bash
df -h /var/lib/pd
```

## Examples

```
$ pd-ctl tso
2024-01-15 10:30:00.500 +0000 UTC
Physical: 4402801390592
Logical: 0
```

## Prevent It

- Run PD on fast SSD storage
- Maintain 3 PD nodes for high availability
- Monitor PD response time for TSO requests

## Related Pages

- [TiDB TSO Error](/tools/tidb/tidb-tso-error)
- [TiDB PD Error](/tools/tidb/tidb-pd-error)
- [TiDB Transaction Error](/tools/tidb/tidb-transaction-error)
