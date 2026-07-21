---
title: "[Solution] Kafka Min ISR Not Met Error"
description: "Fix Kafka min ISR not met error. Resolve produce failures when insufficient in-sync replicas exist."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Min ISR Not Met Error

Produce requests fail because the number of in-sync replicas is below min.insync.replicas. Writes are rejected to prevent data loss when too many replicas are down.

## Common Causes

- Too many replicas are down
- Replicas cannot keep up with leader
- Network issues between replicas and leader

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic
```

### Solution 2

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --alter --topic my-topic --add-config min.insync.replicas=1
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
