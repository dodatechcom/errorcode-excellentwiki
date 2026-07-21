---
title: "[Solution] Kafka Message Too Large Error"
description: "Fix Kafka message too large error. Resolve individual message size limit issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Message Too Large Error

A single message exceeds the broker message.max.bytes or the topic max.message.bytes. The broker rejects the oversized message.

## Common Causes

- Single message exceeds broker limit
- Topic max.message.bytes is too low
- Producer sends unbounded messages

## How to Fix

### Solution 1

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --alter --topic my-topic --add-config message.max.bytes=10485760
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
