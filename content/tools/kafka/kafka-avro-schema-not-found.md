---
title: "[Solution] Kafka Avro Schema Not Found Error"
description: "Fix Kafka Avro schema not found error. Resolve Schema Registry lookup failures."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Avro Schema Not Found Error

The Avro schema is not found in the Schema Registry. The schema may not have been registered or the schema ID is incorrect.

## Common Causes

- Schema was never registered
- Schema ID is wrong in message header
- Schema Registry is unreachable

## How to Fix

### Solution 1

```bash
curl http://localhost:8081/subjects
```

### Solution 2

```bash
curl http://localhost:8081/subjects/my-topic-value/versions
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
