---
title: "[Solution] ClickHouse ZooKeeper Error — How to Fix"
description: "Fix ClickHouse ZooKeeper errors including session expiry, connection failures, and ZooKeeper coordination issues for replicated tables"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse ZooKeeper Error

ZooKeeper errors in ClickHouse occur when the ZooKeeper ensemble used for replication coordination becomes unavailable, sessions expire, or metadata becomes inconsistent.

## Why It Happens

- ZooKeeper cluster is down or unreachable
- ZooKeeper session has expired due to network issues
- Too many watches or znodes overwhelm ZooKeeper
- ZooKeeper disk is full and cannot write transaction logs
- The ZooKeeper connection string in ClickHouse config is wrong
- ClickHouse server time is not synchronized with ZooKeeper

## Common Error Messages

```
DB::Exception: ZooKeeper session has expired
```

```
Code: 242. DB::Exception: Table is readonly because ZooKeeper is unavailable
```

```
DB::Exception: Could not connect to ZooKeeper
```

```
Code: 999. DB::Exception: Poco::Exception: KeeperException
```

## How to Fix It

### 1. Check ZooKeeper Status

```bash
# Check if ZooKeeper is running
echo ruok | nc localhost 2181
# Should respond with "imok"

# Check ZooKeeper status
echo stat | nc localhost 2181

# Check ClickHouse ZooKeeper connection
clickhouse-client --query "
SELECT * FROM system.zookeeper WHERE path = '/'
FORMAT PrettyCompact"
```

### 2. Fix ZooKeeper Connection

```xml
<!-- In ClickHouse config.xml -->
<zookeeper>
  <node index="1">
    <host>zk1.example.com</host>
    <port>2181</port>
  </node>
  <node index="2">
    <host>zk2.example.com</host>
    <port>2181</port>
  </node>
  <node index="3">
    <host>zk3.example.com</host>
    <port>2181</port>
  </node>
</zookeeper>
```

### 3. Fix ZooKeeper Session Expiry

```bash
# After ZooKeeper restarts, ClickHouse replicas become readonly
# Wait for session reconnection (automatic)

# Or force restart replicas
clickhouse-client --query "SYSTEM RESTART REPLICA mydb.mytable"

# Check replica status after restart
clickhouse-client --query "
SELECT database, table, is_readonly, absolute_delay
FROM system.replicas"
```

### 4. Fix ZooKeeper Disk Issues

```bash
# Check ZooKeeper data directory
df -h /var/lib/zookeeper

# ZooKeeper needs space for transaction logs
# Move data directory or add disk space

# Clean old snapshots
sudo rm /var/lib/zookeeper/version-2/log.*.gz
```

## Common Scenarios

- **ZooKeeper restart causes readonly replicas**: Wait for session reconnection, then `SYSTEM RESTART REPLICA`.
- **ZooKeeper disk full**: Free space and restart ZooKeeper. Replicas will resync automatically.
- **Network partition causes session expiry**: Ensure stable network between ClickHouse and ZooKeeper.

## Prevent It

- Run ZooKeeper cluster with at least 3 nodes for fault tolerance
- Monitor ZooKeeper health and disk usage
- Use NTP to keep clocks synchronized between ClickHouse and ZooKeeper

## Related Pages

- [ClickHouse Replication Error](/tools/clickhouse/clickhouse-replication-error)
- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Connection Error](/tools/clickhouse/clickhouse-connection-error)
