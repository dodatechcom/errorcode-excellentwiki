---
title: "[Solution] ClickHouse ZooKeeper Error"
description: "Fix ClickHouse ZooKeeper connection errors when coordination service is unavailable"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse ZooKeeper Error

ZooKeeper errors occur when ClickHouse cannot communicate with the ZooKeeper ensemble for replication coordination.

## Common Causes

- ZooKeeper ensemble down or unreachable
- Network partition between ClickHouse and ZooKeeper
- ZooKeeper session timeout too short
- Firewall blocking ZooKeeper ports

## How to Fix

Check ZooKeeper connectivity:

```bash
echo ruok | nc zookeeper-host 2181
```

Verify ClickHouse ZooKeeper config:

```xml
<zookeeper>
    <node index="1">
        <host>zk1</host>
        <port>2181</port>
    </node>
</zookeeper>
```

Check ZooKeeper logs:

```bash
tail -100 /var/log/zookeeper/zookeeper.out
```

## Examples

```sql
SELECT * FROM system.zookeeper WHERE path = '/clickhouse/tables';
```
