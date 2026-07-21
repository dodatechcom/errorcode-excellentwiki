---
title: "[Solution] Vitess Tablet Restore Timeout Error"
description: "Fix Vitess tablet restore timeout errors when restoring from backup takes too long"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Restore Timeout Error

Restore timeout errors happen when a tablet cannot complete the restore operation within the configured time window.

## Common Causes

- Backup too large for available disk IO
- Network bandwidth limitation during restore
- Restore timeout configured too low
- Compression/decompression CPU bottleneck

## How to Fix

Increase restore timeout:

```bash
vttablet -restore_concurrency=4 -init_timeout 300s
```

Check restore progress:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SELECT * FROM _vt.restore_status"
```

Restore with parallel threads:

```bash
vttablet -restore_concurrency=8 -init_dbt -init_keyspace keyspace1 -init_shard 0
```

## Examples

```bash
cat /var/log/vttablet/vttablet.INFO | grep restore
```
