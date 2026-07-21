---
title: "[Solution] Kafka Consumer Lag Error"
description: "Fix Kafka consumer lag error. Resolve consumer falling behind issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Consumer Lag Error

Consumer lag increases over time. The consumer processes messages slower than they are produced.

## Common Causes

- Consumer processing is slow
- Not enough consumers for partitions
- Message production rate is high

## How to Fix

### Solution 1

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
