---
title: "[Solution] Vitess Tablet Replication Heartbeat Error"
description: "Fix Vitess replication heartbeat errors when heartbeat-based lag detection fails"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Replication Heartbeat Error

Replication heartbeat errors occur when the primary cannot write heartbeat rows, preventing accurate lag measurement.

## Common Causes

- Primary disk full preventing writes
- Heartbeat table locked by long-running transaction
- IO thread saturated on primary
- Heartbeat mechanism disabled on replica

## How to Fix

Check heartbeat table:

```sql
SELECT * FROM _vt.heartbeat ORDER BY ts DESC LIMIT 1;
```

Check primary disk space:

```bash
df -h /var/lib/mysql/
```

Kill blocking transaction:

```sql
SHOW PROCESSLIST;
KILL <blocking_thread_id>;
```

Enable heartbeat on replica:

```bash
vttablet -heartbeat_enable -heartbeat_interval 1s -heartbeat_on_demand
```

## Examples

```sql
SHOW STATUS LIKE 'Innodb_rows_writes';
```
