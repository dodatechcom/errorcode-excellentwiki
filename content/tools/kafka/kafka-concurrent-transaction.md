---
title: "[Solution] Kafka Concurrent Transaction Error"
description: "Fix Kafka concurrent transaction error. Resolve multiple concurrent transaction issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Concurrent Transaction Error

Two producers with the same transactional.id attempt concurrent transactions. One producer fences the other.

## Common Causes

- Multiple producers share same transactional.id
- Producer instances not managed
- Application restart caused duplicate ID

## How to Fix

### Solution 1

```bash
grep 'transactional.id' /path/to/producer.config
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
