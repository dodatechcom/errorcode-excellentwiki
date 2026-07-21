---
title: "[Solution] Kafka Connect Offset Storage Topic Error"
description: "Fix Kafka offset storage topic error. Resolve Connect offset tracking issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Connect Offset Storage Topic Error

The offset storage topic is not available or misconfigured. Connect cannot track source connector offsets.

## Common Causes

- Offset topic does not exist
- Offset topic config is wrong
- Topic retention is too short

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic connect-cluster-offsets
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
