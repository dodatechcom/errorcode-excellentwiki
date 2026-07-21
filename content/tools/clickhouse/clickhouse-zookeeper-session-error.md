---
title: "[Solution] ClickHouse ZooKeeper Session Error"
description: "How to fix ClickHouse ZooKeeper session errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ZooKeeper server down
- Network partition between ClickHouse and ZooKeeper
- Session timeout too short
- ZooKeeper ensemble unhealthy

## How to Fix

Check ZooKeeper connectivity:

```bash
echo ruok | nc localhost 2181
```

Check ClickHouse ZooKeeper config:

```xml
<zookeeper>
  <node index="1">
    <host>zk1</host>
    <port>2181</port>
  </node>
</zookeeper>
```

## Examples

```bash
echo ruok | nc zk1 2181
clickhouse-client --query "SELECT * FROM system.zookeeper WHERE path = '/clickhouse' LIMIT 10"
```
