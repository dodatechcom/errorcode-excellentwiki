---
title: "[Solution] Kafka ZooKeeper Connection Loss Error"
description: "Fix Kafka ZooKeeper connection loss error. Resolve ZooKeeper connectivity issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka ZooKeeper Connection Loss Error

The Kafka broker loses connection to ZooKeeper. This can be caused by network issues, ZooKeeper overload, or session timeout expiry.

## Common Causes

- ZooKeeper is down or overloaded
- Network issues between broker and ZK
- Session timeout expired

## How to Fix

### Solution 1

```bash
echo ruok | nc localhost 2181
```

### Solution 2

```bash
echo stat | nc localhost 2181
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
