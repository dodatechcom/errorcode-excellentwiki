---
title: "[Solution] ClickHouse Copier Error"
description: "How to fix ClickHouse clickhouse-copier errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Source or destination unreachable
- Partition boundaries mismatch
- ZooKeeper coordination failure
- Insufficient disk space on destination

## How to Fix

Check copier status:

```bash
clickhouse-copier --config=copier.xml --task-path=/clickhouse/copier/tasks/my_task status
```

## Examples

```bash
clickhouse-copier --config=copier.xml --task-path=/clickhouse/copier/tasks/my_task copy
```
