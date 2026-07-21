---
title: "[Solution] InfluxDB Consistency Level Error — How to Fix"
description: "Fix InfluxDB consistency level errors when write requests fail due to insufficient node acknowledgments"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Consistency Level Error

Consistency level errors occur when a write request requires a specific number of node acknowledgments but the cluster cannot satisfy the requirement.

## Why It Happens

- Required number of nodes are unavailable for the write
- Consistency level is set higher than available replicas
- Network partition prevents nodes from acknowledging writes
- Replication factor exceeds the number of data nodes
- One or more nodes are lagging behind the consensus

## Common Error Messages

```
error: write failed: consistency level not satisfied
```

```
partial write: not enough replicas available for write, required=2 available=1
```

## How to Fix It

### 1. Lower Consistency Level

```bash
influx -consistency one -execute 'INSERT cpu,host=server01 value=45'
```

### 2. Verify Replication Factor

```bash
influx -database mydb -execute 'SHOW RETENTION POLICY "autogen"'
```

### 3. Check Node Availability

```bash
influxd-ctl show
curl http://node1:8086/ping
curl http://node2:8086/ping
```

### 4. Adjust for Single-Node Setup

```bash
curl -XPOST 'http://localhost:8086/api/v2/write?consistency=any&org=myorg&bucket=mydb' \
  -H 'Authorization: Token mytoken' \
  -d 'cpu,host=s01 value=42'
```

## Examples

```
$ curl -XPOST http://localhost:8086/write?consistency=all -d 'cpu value=1'
{"error":"write failed: consistency level not satisfied, only 1 of 3 nodes responded"}
```

## Prevent It

- Match consistency level to your cluster size
- Use any for single-node deployments
- Monitor node availability and replication lag

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB Cluster Error](/tools/influxdb/influxdb-cluster-error)
