---
title: "[Solution] Kafka Connector Not Found Error"
description: "Fix Kafka connector not found error. Resolve connector reference issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Connector Not Found Error

The requested connector does not exist in the Connect cluster. It may have been deleted or never created.

## Common Causes

- Connector was never created
- Connector was deleted
- Connector name is misspelled

## How to Fix

### Solution 1

```bash
curl http://localhost:8083/connectors
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
