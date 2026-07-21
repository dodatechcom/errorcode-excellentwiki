---
title: "[Solution] Kafka ACL Authorization Error"
description: "Fix Kafka ACL authorization error. Resolve access control list permission issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka ACL Authorization Error

The client is not authorized to perform the requested operation. The ACL does not grant the required permission for the principal on the resource.

## Common Causes

- ACL does not include the required operation
- Principal does not match
- Authorizer is not configured

## How to Fix

### Solution 1

```bash
kafka-acls.sh --bootstrap-server localhost:9092 --list
```

### Solution 2

```bash
kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:myuser --operation Read --topic my-topic
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
