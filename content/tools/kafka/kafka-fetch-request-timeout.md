---
title: "[Solution] Kafka Fetch Request Timeout Error"
description: "Fix Kafka fetch request timeout error. Resolve consumer fetch timeout issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Fetch Request Timeout Error

The fetch request from the consumer times out. This happens when the broker is slow to respond, the fetch size is too large, or network latency is high.

## Common Causes

- Broker is overloaded
- fetch.size is too large
- Network latency is high

## How to Fix

### Solution 1

```bash
grep 'fetch.max.wait.ms\|fetch.min.bytes\|fetch.size' /path/to/consumer.config
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
