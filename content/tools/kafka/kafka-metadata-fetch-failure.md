---
title: "[Solution] Kafka Metadata Fetch Failure Error"
description: "Fix Kafka metadata fetch failure error. Resolve metadata request issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Metadata Fetch Failure Error

The client cannot fetch topic metadata from the broker. The broker may not have the topic metadata or the request is being rejected.

## Common Causes

- Topic metadata is not available
- Client lacks permissions
- Broker cannot serve metadata

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
