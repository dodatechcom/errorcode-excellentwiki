---
title: "[Solution] Kafka Unclean Shutdown Error"
description: "Fix Kafka unclean shutdown error. Resolve broker recovery after unclean termination."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Unclean Shutdown Error

The broker was not shut down gracefully. On restart, it needs to recover logs and may encounter data corruption or inconsistent state.

## Common Causes

- Broker was killed with SIGKILL
- Power failure caused shutdown
- OOM killed the broker process

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
