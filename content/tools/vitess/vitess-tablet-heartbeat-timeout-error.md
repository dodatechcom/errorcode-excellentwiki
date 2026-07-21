---
title: "[Solution] Vitess Tablet Heartbeat Timeout Error"
description: "Fix Vitess tablet heartbeat timeout errors when replicas cannot keep up with heartbeat writes"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Heartbeat Timeout Error

Heartbeat timeout errors occur when the primary tablet cannot write heartbeat rows within the expected interval, indicating replication or IO issues.

## Common Causes

- Primary disk IO saturated with writes
- Replication lag causing heartbeat table delay
- Heartbeat interval too short for workload
- InnoDB flushing bottleneck on primary

## How to Fix

Check heartbeat status:

```sql
SELECT * FROM _vt.heartbeat ORDER BY ts DESC LIMIT 5;
```

Increase heartbeat interval:

```bash
vttablet -heartbeat_enable -heartbeat_interval 1s
```

Monitor primary IO:

```bash
iostat -x 1 5
```

## Examples

```sql
SHOW STATUS LIKE 'Innodb_data_writes';
```
