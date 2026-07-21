---
title: "[Solution] Kafka Topic Deletion Failed Error"
description: "Fix Kafka topic deletion failed errors. Resolve issues preventing topic removal from the cluster."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Topic Deletion Failed Error

Kafka topic deletion failed errors occur when the controller cannot fully remove a topic due to ongoing replication, open file handles, or authorization issues.

## Common Causes

- delete.topic.enable is set to false on the broker
- Replicas still consuming from the topic during deletion
- Authorization denied for topic deletion
- Topic marked for deletion but log segments not cleaned up

## How to Fix

1. Enable topic deletion in server.properties:

```properties
delete.topic.enable=true
```

2. Delete the topic via admin client:

```bash
kafka-topics.sh --bootstrap-server localhost:9092 \
  --delete --topic my-old-topic
```

3. If stuck in deletion state, force delete by removing log directories:

```bash
# Stop the broker first, then:
rm -rf /var/kafka-logs/my-old-topic-*
```

4. Check authorization for deletion:

```bash
kafka-acls.sh --list --bootstrap-server localhost:9092 \
  --topic my-old-topic
```

## Examples

```bash
# List topics pending deletion
kafka-topics.sh --list --bootstrap-server localhost:9092 | grep __deleted

# Verify topic is gone after deletion
kafka-topics.sh --describe --bootstrap-server localhost:9092 \
  --topic my-old-topic 2>&1
```
