---
title: "[Solution] Kafka KRaft Mode Error"
description: "Fix Kafka KRaft mode error. Resolve KRaft metadata log and mode transition issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka KRaft Mode Error

The broker encounters errors in KRaft mode. The metadata log may be corrupted, or the mode transition from ZooKeeper was incomplete.

## Common Causes

- Metadata log is corrupted
- ZK migration was incomplete
- process.roles is misconfigured

## How to Fix

### Solution 1

```bash
kafka-metadata.sh --snapshot /path/to/metadata.log
```

### Solution 2

```bash
grep 'process.roles\|node.id\|controller.quorum.voters' /etc/kafka/server.properties
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
