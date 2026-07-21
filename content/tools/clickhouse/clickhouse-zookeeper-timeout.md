---
title: "[Solution] ClickHouse ZooKeeper Timeout Error"
description: "How to fix ClickHouse ZooKeeper timeout errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- ZooKeeper responding slowly
- Network latency
- ZooKeeper GC pauses
- Too many znodes

## How to Fix

Increase session timeout:

```xml
<zookeeper>
  <session_timeout_ms>30000</session_timeout_ms>
</zookeeper>
```

## Examples

```bash
clickhouse-client --query "SELECT * FROM system.replicas WHERE is_readonly = 1"
```
