---
title: "[Solution] Kafka Coordinator Not Available Error"
description: "Fix Kafka coordinator not available error. Resolve group coordinator lookup issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Coordinator Not Available Error

The group coordinator for the consumer group is not available. The coordinator broker may have failed or the group metadata is not yet propagated.

## Common Causes

- Coordinator broker is down
- Group metadata not propagated
- Broker just restarted

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
