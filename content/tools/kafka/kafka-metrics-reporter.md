---
title: "[Solution] Kafka Metrics Reporter Error"
description: "Fix Kafka metrics reporter error. Resolve custom metrics reporter issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Metrics Reporter Error

A custom metrics reporter fails to report metrics. The reporter class is missing or misconfigured.

## Common Causes

- Reporter class is missing from classpath
- Reporter config is wrong
- Reporter throws exceptions

## How to Fix

### Solution 1

```bash
grep 'metric.reporters' /etc/kafka/server.properties
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
