---
title: "[Solution] Kafka Cluster ID Mismatch Error"
description: "Fix Kafka cluster ID mismatch error. Resolve KRaft cluster identity issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Cluster ID Mismatch Error

The cluster ID in the metadata log does not match the expected ID. This happens when a broker is mistakenly added to the wrong cluster.

## Common Causes

- Broker added to wrong cluster
- Metadata log was copied from another cluster
- Cluster ID was changed

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
