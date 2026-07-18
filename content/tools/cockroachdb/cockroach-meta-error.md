---
title: "[Solution] CockroachDB Meta Error - Fix Meta Ranges Unavailable"
description: "Fix CockroachDB meta range unavailability errors. Resolve system range issues, meta2 range problems, and cluster metadata failures."
tools: ["cockroachdb"]
error-types: ["meta-error"]
severities: ["critical"]
weight: 5
---

This error means CockroachDB's meta ranges (system ranges) are unavailable or have issues. Meta ranges store cluster metadata and their failure affects the entire cluster.

## What This Error Means

When meta ranges are unavailable, you see:

```
ERROR: meta range unavailable; could not determine table ID
# or
ERROR: range 1 not found on any live nodes
# or
SQLSTATE 57P01: node unavailable
```

Meta ranges (range ID 1) store cluster metadata. Their unavailability prevents all operations that require metadata lookup.

## Why It Happens

- All replicas of meta range 1 are on down nodes
- Network partitions isolated the meta range replicas
- The node hosting the meta range lease is overloaded
- Disk failures corrupted meta range data
- Too many nodes are down to maintain quorum for meta ranges

## How to Fix It

### Check node status

```bash
cockroach node status --insecure
```

Ensure enough nodes are up to serve meta ranges.

### Check meta range status

```sql
SELECT range_id, start_key, end_key, lease_holder, replicas
FROM [SHOW RANGES FROM DATABASE system]
WHERE range_id = 1;
```

### Verify quorum for meta ranges

```sql
SELECT * FROM crdb_internal.ranges_no_leases
WHERE range_id = 1;
```

At least 3 replicas must be available for quorum.

### Restart down nodes

```bash
sudo systemctl start cockroach
```

Recovering down nodes restores meta range availability.

### Check network connectivity

```bash
ping <node-ip>
telnet <node-ip> 26257
```

### Use the debug range API

```bash
curl http://localhost:8080/ranges/1
```

Check the meta range status via the debug API.

### Recover from node failures

```bash
cockroach node decommission <node-id> --insecure
```

If a node is permanently down, decommission it to remove its replicas.

### Check disk space on meta range nodes

```bash
df -h /var/lib/cockroach/
```

Meta range nodes need available disk space.

### Monitor meta range health

```sql
SELECT * FROM crdb_internal.ranges
WHERE range_id IN (1, 2, 3);
```

Ranges 1-3 are system ranges that must remain healthy.

### Enable range GC

```sql
SHOW CLUSTER SETTING jobs.gc.ttlseconds;
```

Expired meta range data can cause issues.

## Common Mistakes

- Not monitoring the health of system ranges
- Running too few nodes to maintain quorum for meta ranges
- Not checking disk space on nodes hosting meta ranges
- Assuming CockroachDB will automatically recover from meta range failures
- Not decommissioning permanently down nodes

## Related Pages

- [CockroachDB Node Unavailable]({{< relref "/tools/cockroachdb/cockroach-node-unavailable" >}}) -- node issues
- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
- [CockroachDB Gossip Error]({{< relref "/tools/cockroachdb/cockroach-gossip-error" >}}) -- gossip issues
