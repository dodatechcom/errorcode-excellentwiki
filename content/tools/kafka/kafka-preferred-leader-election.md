---
title: "[Solution] Kafka Preferred Leader Election Error"
description: "Fix Kafka preferred leader election error. Resolve leader balance issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Preferred Leader Election Error

Preferred leader election fails or does not complete. The preferred leader may not be in the ISR or the election is not triggered.

## Common Causes

- Preferred leader is not in ISR
- auto.leader.rebalance.enable is false
- Controller is not available

## How to Fix

### Solution 1

```bash
kafka-leader-election.sh --bootstrap-server localhost:9092 --election-type preferred --all-topic-partitions
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
