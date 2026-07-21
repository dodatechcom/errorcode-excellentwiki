---
title: "[Solution] Kafka Heartbeat Failure Error"
description: "Fix Kafka heartbeat failure error. Resolve consumer heartbeat delivery issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Heartbeat Failure Error

The consumer fails to send heartbeats to the group coordinator. This can be caused by network issues, long GC pauses, or the coordinator being unavailable.

## Common Causes

- Network connectivity issues
- Long GC pauses
- Coordinator broker is down

## How to Fix

### Solution 1

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
