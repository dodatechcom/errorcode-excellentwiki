---
title: "[Solution] Kafka Consumer Rebalance Failed Error"
description: "Fix Kafka consumer rebalance failed error. Resolve consumer group coordination issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Consumer Rebalance Failed Error

The consumer group fails to complete a rebalance. This can be caused by session timeouts, coordinator failures, or consumers failing to rejoin in time.

## Common Causes

- Session timeout too short
- Coordinator broker is down
- Consumer takes too long to rejoin

## How to Fix

### Solution 1

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

### Solution 2

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --describe --group my-group --all
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
