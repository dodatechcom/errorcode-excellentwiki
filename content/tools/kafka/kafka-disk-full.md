---
title: "[Solution] Kafka Disk Full Error"
description: "Fix Kafka disk full error. Resolve disk space exhaustion on broker nodes."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Disk Full Error

The broker runs out of disk space. New message production fails and the broker may go offline if log.dirs is full.

## Common Causes

- Disk usage has reached capacity
- Log retention is not cleaning up
- Topics have grown too large

## How to Fix

### Solution 1

```bash
df -h /var/lib/kafka
```

### Solution 2

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
