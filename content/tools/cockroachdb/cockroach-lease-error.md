---
title: "[Solution] CockroachDB Lease Error - Fix Range Lease Acquisition Failed"
description: "Fix CockroachDB range lease acquisition failures. Resolve leaseholder issues, lease transfers, and range unavailability."
tools: ["cockroachdb"]
error-types: ["lease-error"]
severities: ["error"]
weight: 5
---

This error means a CockroachDB range cannot acquire or maintain a lease. The leaseholder is responsible for serving reads and writes for a range.

## What This Error Means

When lease acquisition fails, you see:

```
ERROR: range has no lease holder
# or
ERROR: lease acquisition failed: node unavailable
# or
NotLeaseHolderError: r1: not leaseholder
```

Each range has one leaseholder that handles all read and write requests. Without a lease, the range is unavailable.

## Why It Happens

- The leaseholder node is down
- Network partitions prevent the leaseholder from communicating
- The lease expired due to a long-running operation
- Another node is trying to take over the lease
- Clock skew between nodes affects lease timing
- The lease transfer was interrupted

## How to Fix It

### Check leaseholder status

```sql
SELECT range_id, lease_holder, replicas
FROM [SHOW RANGES FROM TABLE my_table]
WHERE lease_holder IS NULL;
```

### Find the leaseholder for a specific range

```sql
SELECT * FROM crdb_internal.ranges
WHERE table_name = 'my_table';
```

### Restart the leaseholder node

```bash
sudo systemctl restart cockroach
```

### Check for clock skew

```bash
# On each node
timedatectl status
```

CockroachDB uses hybrid logical clocks. Clock skew affects leases.

### Transfer lease manually

```sql
ALTER TABLE my_table EXPERIMENTAL_RELOCATE TO 2;
```

Transfer the range lease to a specific node.

### Check node health

```bash
cockroach node status --insecure --ranges
```

Verify nodes are healthy and serving ranges.

### Monitor lease status

```sql
SELECT * FROM crdb_internal.leases
WHERE table_name = 'my_table';
```

### Check for clock offset

```sql
SHOW CLUSTER SETTING server.clock.offset.mean;
SHOW CLUSTER SETTING server.clock.offset.max;
```

### Increase lease duration

```sql
SHOW CLUSTER SETTING server.lease.duration;
```

Longer leases reduce renewal frequency but increase failover time.

### Use follower reads to reduce lease pressure

```sql
SELECT * FROM my_table AS OF SYSTEM TIME follower_read_timestamp();
```

Follower reads do not require a lease.

## Common Mistakes

- Not monitoring leaseholder availability as a key cluster metric
- Not having nodes in multiple availability zones for lease failover
- Assuming lease acquisition is instant
- Not checking clock synchronization between nodes
- Not using follower reads to reduce leaseholder pressure

## Related Pages

- [CockroachDB Node Unavailable]({{< relref "/tools/cockroachdb/cockroach-node-unavailable" >}}) -- node issues
- [CockroachDB Raft Error]({{< relref "/tools/cockroachdb/cockroach-raft-error" >}}) -- Raft issues
- [CockroachDB Timeout]({{< relref "/tools/cockroachdb/cockroach-timeout" >}}) -- timeouts
