---
title: "[Solution] Kafka Commit Offset Failed Error"
description: "Fix Kafka commit offset failed error. Resolve consumer offset commit failures."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Commit Offset Failed Error

The consumer cannot commit offsets to Kafka. This happens when the group coordinator is unavailable, the consumer is not a group member, or there is a rebalance in progress.

## Common Causes

- Group coordinator is unavailable
- Consumer is not a group member
- Rebalance is in progress

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
