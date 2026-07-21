---
title: "[Solution] Kafka Topic Auto-Create Error"
description: "Fix Kafka topic auto-create errors. Resolve issues when brokers fail to create topics on demand."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Topic Auto-Create Error

Kafka topic auto-create errors occur when a producer or consumer attempts to write to a non-existent topic and the broker does not have auto-creation enabled.

## Common Causes

- auto.create.topics.enable is set to false on the broker
- Topic name typo in producer or consumer configuration
- Insufficient cluster resources to create new partitions
- Authorization denied for topic creation

## How to Fix

1. Enable auto-topic creation in server.properties:

```properties
auto.create.topics.enable=true
```

2. Manually create the topic if auto-creation is disabled:

```bash
kafka-topics.sh --create --bootstrap-server localhost:9092 \
  --topic my-new-topic --partitions 6 --replication-factor 3
```

3. Check if the topic exists:

```bash
kafka-topics.sh --list --bootstrap-server localhost:9092 | grep my-new-topic
```

4. Verify authorization for topic creation:

```bash
kafka-acls.sh --list --bootstrap-server localhost:9092 \
  --topic my-new-topic
```

## Examples

```bash
# Create topic with specific config
kafka-topics.sh --create --bootstrap-server localhost:9092 \
  --topic orders --partitions 12 --replication-factor 3 \
  --config retention.ms=604800000 --config cleanup.policy=compact
```
