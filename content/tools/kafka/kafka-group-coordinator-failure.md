---
title: "[Solution] Kafka Group Coordinator Failure Error"
description: "Fix Kafka group coordinator failure error. Resolve group coordination service issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Group Coordinator Failure Error

The group coordinator service fails. The broker hosting the coordinator has issues or the group metadata is corrupted.

## Common Causes

- Coordinator broker has issues
- Group metadata is corrupted
- __consumer_offsets topic has issues

## How to Fix

### Solution 1

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

### Solution 2

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic __consumer_offsets
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
