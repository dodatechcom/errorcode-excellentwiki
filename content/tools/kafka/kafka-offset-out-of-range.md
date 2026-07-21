---
title: "[Solution] Kafka Offset Out of Range Error"
description: "Fix Kafka offset out of range error. Resolve consumer offset issues when offsets are expired or invalid."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Offset Out of Range Error

The consumer requests an offset that no longer exists on the broker. This happens when log retention has deleted the segments containing that offset.

## Common Causes

- Log retention deleted segments
- Consumer offset is too old
- Topic retention policy is aggressive

## How to Fix

### Solution 1

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my-group --reset-offsets --to-earliest --all-topics --execute
```

### Solution 2

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
