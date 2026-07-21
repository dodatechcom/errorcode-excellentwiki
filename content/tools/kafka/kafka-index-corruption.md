---
title: "[Solution] Kafka Index Corruption Error"
description: "Fix Kafka index corruption error. Resolve offset and time index file issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Index Corruption Error

The offset or time index file is corrupted. The broker cannot efficiently locate messages in the log.

## Common Causes

- Disk failure corrupted index
- Unclean shutdown during index write
- Index file exceeded max size

## How to Fix

### Solution 1

```bash
kafka-log-dirs.sh --bootstrap-server localhost:9092 --verify --broker-ids 0
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
