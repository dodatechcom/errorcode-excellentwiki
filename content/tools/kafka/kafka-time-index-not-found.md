---
title: "[Solution] Kafka Time Index Not Found Error"
description: "Fix Kafka time index not found error. Resolve time-based index lookup issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Time Index Not Found Error

The time index for a log segment is missing or corrupt. Time-based lookups fall back to linear search, degrading performance.

## Common Causes

- Time index was deleted during cleanup
- Segment was created without index
- Index corruption caused deletion

## How to Fix

### Solution 1

```bash
kafka-log-dirs.sh --bootstrap-server localhost:9092 --describe --broker-ids 0
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
