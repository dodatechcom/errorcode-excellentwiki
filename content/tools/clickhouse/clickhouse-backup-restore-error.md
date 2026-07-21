---
title: "[Solution] ClickHouse Backup Restore Error"
description: "How to fix ClickHouse backup restore failures"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Backup corrupted
- Table already exists during restore
- Version mismatch between backup and restore
- ZooKeeper state mismatch

## How to Fix

Restore with --rm flag:

```bash
clickhouse-backup restore --rm my-backup
```

## Examples

```bash
clickhouse-backup restore my-backup --table my_table
clickhouse-backup list
```
