---
title: "[Solution] Kafka Leader Not Available Error"
description: "Fix Kafka leader not available error. Resolve leader election failures for Kafka partitions."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Leader Not Available Error

A partition has no elected leader. This happens during broker failures, under-replicated partitions, or when the controller cannot complete leader election.

## Common Causes

- All replicas for a partition are down
- Controller is not elected
- Under-replicated partitions prevent election

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions
```

### Solution 2

```bash
kafka-leader-election.sh --bootstrap-server localhost:9092 --election-type preferred --all-topic-partitions
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
