---
title: "[Solution] Kafka Compact Topic Offset Error"
description: "Fix Kafka compact topic offset errors. Resolve offset out of range on compacted topics."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Compact Topic Offset Error

Kafka compact topic offset errors occur when a consumer requests an offset that no longer exists because the log compaction process has deleted older segments.

## Common Causes

- Consumer was idle while compaction removed old log segments
- Retention period shorter than consumer downtime
- Consumer offset pointing to a deleted segment boundary
- Compaction removing records faster than expected

## How to Fix

1. Configure the consumer to start from the beginning if offset is invalid:

```properties
auto.offset.reset=earliest
```

2. Increase log retention period for compacted topics:

```properties
log.retention.hours=168
log.cleaner.min.cleanable.ratio=0.5
```

3. Reset consumer group offsets to a valid position:

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group my-consumer-group \
  --topic my-compacted-topic \
  --reset-offsets --to-earliest --execute
```

4. Check available offsets for the topic:

```bash
kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic my-compacted-topic --time -1
```

## Examples

```bash
# Find the earliest available offset
kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic my-compacted-topic --time -2

# Find the latest available offset
kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic my-compacted-topic --time -1
```
