---
title: "[Solution] InfluxDB Rebalance Error — How to Fix"
description: "Fix InfluxDB rebalance errors when the cluster cannot redistribute shards after adding or removing nodes"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Rebalance Error

Rebalance errors occur when the InfluxDB Enterprise cluster fails to redistribute shards across nodes after topology changes like adding or removing data nodes.

## Why It Happens

- Target node is not reachable during rebalance
- Insufficient disk space on the destination node
- Shard is locked by ongoing writes during migration
- Meta store has inconsistent shard ownership records
- Network bandwidth is insufficient for shard transfer

## Common Error Messages

```
error: rebalance failed: node unreachable
```

```
error: cannot move shard 1234: insufficient disk space
```

```
rebalance: shard copy timeout
```

```
error: shard ownership conflict during rebalance
```

## How to Fix It

### 1. Check Node Status

```bash
influxd-ctl show
influxd-ctl ping
```

### 2. Verify Disk Space on Target

```bash
ssh node2 "df -h /var/lib/influxdb"
```

### 3. Stop Writes During Rebalance

```bash
# Pause data ingestion temporarily
# Then rebalance
influxd-ctl copy-shard -src data1:8088 -dst data2:8088 -shard 1234
```

### 4. Force Rebalance

```bash
influxd-ctl remove -data-only node3
sleep 30
influxd-ctl join -meta-server http://meta1:8091 -data-dir /var/lib/influxdb node3
```

## Examples

```
$ influxd-ctl copy-shard -src node1:8088 -dst node2:8088 -shard 1234
Error: destination node insufficient disk space (need 5GB, have 2GB)
```

## Prevent It

- Ensure target nodes have enough disk before adding
- Rebalance during low-traffic periods
- Monitor shard distribution across the cluster

## Related Pages

- [InfluxDB Cluster Error](/tools/influxdb/influxdb-cluster-error)
- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB Node Error](/tools/influxdb/influxdb-node-error)
