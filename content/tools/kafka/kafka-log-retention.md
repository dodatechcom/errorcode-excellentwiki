---
title: "[Solution] Kafka Log Retention Error"
description: "Fix Kafka log retention error. Resolve log segment retention and cleanup issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Log Retention Error

Log retention is not working as expected. Segments may not be deleted, or data is being deleted too aggressively.

## Common Causes

- retention.ms or retention.bytes is misconfigured
- Log cleaner is disabled
- Segment files are locked

## How to Fix

### Solution 1

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
