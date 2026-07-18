---
title: "[Solution] Apache Kafka Log Cleaner Error"
description: "Fix Apache Kafka log cleaner errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka Log Cleaner Error

Kafka log cleaner errors occur when log compaction fails or is misconfigured.

## Why This Happens

- Cleaner not running
- Compaction failed
- Disk full
- Cleaner lag

## Common Error Messages

- `log_cleaner_not_running_error`
- `log_compaction_error`
- `log_disk_full_error`
- `log_cleaner_lag_error`

## How to Fix It

### Solution 1: Check cleaner status

Monitor log cleaner metrics:

```bash
kafka-log-dirs.sh --bootstrap-server localhost:9092 --describe
```

### Solution 2: Fix compaction issues

Check cleaner logs for errors.

### Solution 3: Monitor disk usage

Track log directory disk usage.


## Common Scenarios

- **Cleaner not running:** Check cleaner process.
- **Compaction failed:** Verify cleaner configuration.

## Prevent It

- Monitor cleaner health
- Set up alerts
- Plan capacity
