---
title: "[Solution] Vitess Tablet Transaction Size Error"
description: "Fix Vitess transaction size limit errors when DML statements exceed configured thresholds"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Transaction Size Error

Transaction size errors occur when a single DML statement or transaction affects more rows than vtgate allows.

## Common Causes

- UPDATE or DELETE without WHERE clause affecting too many rows
- Transaction size limit too restrictive for workload
- Batch operation not split into chunks
- vtgate transaction size threshold misconfigured

## How to Fix

Increase transaction size limit:

```bash
vtgate -transaction_mode=multi -shard_gateway_num_go_routines=20
```

Split large batch operations:

```sql
DELETE FROM sessions WHERE created_at < '2023-01-01' LIMIT 1000;
```

Check current setting:

```bash
curl http://localhost:15200/debug/vars
```

## Examples

```sql
-- Process in batches of 1000
DELETE FROM old_logs WHERE ts < NOW() - INTERVAL 90 DAY LIMIT 1000;
```
