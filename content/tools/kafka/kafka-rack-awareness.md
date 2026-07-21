---
title: "[Solution] Kafka Rack Awareness Error"
description: "Fix Kafka rack awareness error. Resolve cross-rack replication placement issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Rack Awareness Error

Partition replicas are not distributed across racks as expected. The rack configuration is incorrect or broker.rack is not set.

## Common Causes

- broker.rack is not configured
- Rack IDs are wrong
- Replication does not respect rack placement

## How to Fix

### Solution 1

```bash
grep broker.rack /etc/kafka/server.properties
```

### Solution 2

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
