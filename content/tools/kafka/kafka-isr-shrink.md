---
title: "[Solution] Kafka ISR Shrink Error"
description: "Fix Kafka ISR shrink error. Resolve in-sync replica set reduction issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka ISR Shrink Error

The ISR shrinks because a replica cannot keep up with the leader. This reduces fault tolerance.

## Common Causes

- Replica is falling behind
- replica.lag.time.max.ms is too short
- Broker is overloaded

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
