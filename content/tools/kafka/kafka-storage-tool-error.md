---
title: "[Solution] Kafka Storage Tool Error"
description: "Fix Kafka storage tool error. Resolve kafka-storage.sh command issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Storage Tool Error

The kafka-storage.sh tool fails to format or verify storage. The cluster ID is wrong or the directory is not empty.

## Common Causes

- Cluster ID is wrong
- Storage directory is not empty
- Config file is wrong

## How to Fix

### Solution 1

```bash
kafka-metadata.sh --snapshot /path/to/metadata.log
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
