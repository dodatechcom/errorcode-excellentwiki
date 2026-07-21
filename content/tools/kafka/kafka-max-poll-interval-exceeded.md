---
title: "[Solution] Kafka Max Poll Interval Exceeded Error"
description: "Fix Kafka max.poll.interval.ms exceeded error. Resolve consumer eviction from group."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Max Poll Interval Exceeded Error

The consumer is removed from the group because it failed to call poll() within max.poll.interval.ms. The processing time between polls exceeds the configured interval.

## Common Causes

- Processing time between polls is too long
- max.poll.interval.ms is set too low
- Consumer is doing heavy processing

## How to Fix

### Solution 1

```bash
grep max.poll /path/to/consumer.config
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
