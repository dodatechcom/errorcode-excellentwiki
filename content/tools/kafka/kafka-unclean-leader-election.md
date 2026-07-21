---
title: "[Solution] Kafka Unclean Leader Election Error"
description: "Fix Kafka unclean leader election error. Resolve data loss risk from unclean leader elections."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Unclean Leader Election Error

An out-of-sync replica was elected leader because all in-sync replicas are unavailable. This can cause data loss when unclean.leader.election.enable is true.

## Common Causes

- All in-sync replicas are down
- unclean.leader.election.enable is true
- No ISR members available

## How to Fix

### Solution 1

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --alter --topic my-topic --add-config unclean.leader.election.enable=false
```

### Solution 2

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
