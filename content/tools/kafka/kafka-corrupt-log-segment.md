---
title: "[Solution] Kafka Corrupt Log Segment Error"
description: "Fix Kafka corrupt log segment error. Resolve log file corruption issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Corrupt Log Segment Error

A log segment file is corrupted. The broker cannot read the segment, which may cause data loss or partition unavailability.

## Common Causes

- Disk failure corrupted the segment
- Unclean shutdown caused corruption
- Bug in Kafka log handling

## How to Fix

### Solution 1

```bash
kafka-log-dirs.sh --bootstrap-server localhost:9092 --verify --broker-ids 0
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
