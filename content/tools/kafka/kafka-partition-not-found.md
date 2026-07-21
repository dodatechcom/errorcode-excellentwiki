---
title: "[Solution] Kafka Partition Not Found Error"
description: "Fix Kafka partition not found error. Resolve partition reference issues in Kafka topics."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Partition Not Found Error

The requested partition does not exist for the given topic. This may indicate topic metadata is stale or the partition was removed during rebalancing.

## Common Causes

- Partition metadata is stale
- Topic was recreated with fewer partitions
- Consumer is using old metadata

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic
```

### Solution 2

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
