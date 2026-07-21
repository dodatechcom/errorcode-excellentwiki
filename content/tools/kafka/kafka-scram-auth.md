---
title: "[Solution] Kafka SCRAM Authentication Error"
description: "Fix Kafka SCRAM authentication error. Resolve SCRAM-SHA-256/512 authentication issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka SCRAM Authentication Error

SCRAM authentication fails. The SCRAM credentials were not properly created or the mechanism name is incorrect.

## Common Causes

- SCRAM credentials were not created
- Mechanism name is wrong
- Broker does not store SCRAM credentials

## How to Fix

### Solution 1

```bash
kafka-configs.sh --bootstrap-server localhost:9092 --describe --user myuser --all
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
