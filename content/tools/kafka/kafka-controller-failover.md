---
title: "[Solution] Kafka Controller Failover Error"
description: "Fix Kafka controller failover error. Resolve issues during controller election and failover."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Controller Failover Error

The controller failover process fails or takes too long. This happens when ZooKeeper or KRaft cannot elect a new controller, or the new controller cannot load partition metadata.

## Common Causes

- ZooKeeper session expired
- KRaft quorum is unavailable
- Controller metadata is corrupted

## How to Fix

### Solution 1

```bash
kafka-metadata.sh --snapshot /path/to/metadata.log
```

### Solution 2

```bash
echo ruok | nc localhost 2181
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
