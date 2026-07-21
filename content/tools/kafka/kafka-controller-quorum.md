---
title: "[Solution] Kafka Controller Quorum Error"
description: "Fix Kafka controller quorum error. Resolve KRaft quorum formation issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Controller Quorum Error

The KRaft controller quorum cannot form or maintain a majority. This prevents the cluster from electing a controller and serving metadata requests.

## Common Causes

- Not enough controller nodes
- Network partition between controllers
- Quorum voters configuration is wrong

## How to Fix

### Solution 1

```bash
grep 'controller.quorum.voters\|controller.listener.names' /etc/kafka/server.properties
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
