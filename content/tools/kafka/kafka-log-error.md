---
title: "[Solution] Apache Kafka Log Retention Error"
description: "Fix Apache Kafka log retention errors. Learn why this happens and how to resolve it quickly."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Apache Kafka Log Retention Error

Kafka log retention errors occur when log segments fail to be deleted or compacted.

## Why This Happens

- Retention exceeded
- Segment deletion failed
- Compaction error
- Disk full

## Common Error Messages

- `log_retention_error`
- `log_deletion_error`
- `log_compaction_error`
- `log_disk_full`

## How to Fix It

### Solution 1: Check retention settings

View retention configuration:

```properties
log.retention.hours=168
log.retention.bytes=-1
```

### Solution 2: Force log deletion

Delete old segments:

```bash
kafka-delete-records.sh --bootstrap-server localhost:9092 --offset-json-file delete.json
```

### Solution 3: Monitor disk usage

Track log directory disk usage.


## Common Scenarios

- **Retention exceeded:** Check retention configuration.
- **Disk full:** Increase disk space or adjust retention.

## Prevent It

- Set appropriate retention
- Monitor disk usage
- Implement cleanup policies
