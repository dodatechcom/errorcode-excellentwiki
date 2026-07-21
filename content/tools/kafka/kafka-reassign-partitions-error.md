---
title: "[Solution] Kafka Reassign Partitions Error"
description: "Fix Kafka reassign partitions error. Resolve partition reassignment failures."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Reassign Partitions Error

Partition reassignment fails. The target broker does not have enough disk space or the reassignment JSON is invalid.

## Common Causes

- Target broker disk space is low
- Reassignment JSON is invalid
- Broker is offline

## How to Fix

### Solution 1

```bash
kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --verify --reassignment-json-file reassignment.json
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
