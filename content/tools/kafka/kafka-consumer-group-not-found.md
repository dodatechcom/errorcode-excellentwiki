---
title: "[Solution] Kafka Consumer Group Not Found Error"
description: "Fix Kafka consumer group not found error. Resolve consumer group reference issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Consumer Group Not Found Error

The specified consumer group does not exist. The group may have expired due to inactivity or was never created.

## Common Causes

- Group expired from inactivity
- Group was never created
- Group coordinator lost metadata

## How to Fix

### Solution 1

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
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
