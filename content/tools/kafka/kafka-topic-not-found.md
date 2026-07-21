---
title: "[Solution] Kafka Topic Not Found Error"
description: "Fix Kafka topic not found error. Resolve missing or deleted topic issues in Kafka."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Topic Not Found Error

The requested topic does not exist. The topic may have been deleted, auto.create.topics.enable is false, or the topic name is misspelled.

## Common Causes

- Topic was deleted
- auto.create.topics.enable is false
- Topic name is misspelled

## How to Fix

### Solution 1

```bash
kafka-topics.sh --bootstrap-server localhost:9092 --list
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
