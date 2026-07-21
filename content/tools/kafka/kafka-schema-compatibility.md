---
title: "[Solution] Kafka Schema Compatibility Error"
description: "Fix Kafka schema compatibility error. Resolve schema evolution and compatibility issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Schema Compatibility Error

The new schema version is incompatible with the existing schema. Schema Registry rejects the registration due to compatibility rule violations.

## Common Causes

- Schema change is breaking
- Compatibility mode is too strict
- New field has no default value

## How to Fix

### Solution 1

```bash
curl http://localhost:8081/config/my-topic-value
```

### Solution 2

```bash
curl -X PUT -H 'Content-Type: application/json' --data '{"compatibility":"BACKWARD"}' http://localhost:8081/config/my-topic-value
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
