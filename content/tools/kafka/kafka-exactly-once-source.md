---
title: "[Solution] Kafka Exactly-Once Source Connector Error"
description: "Fix Kafka exactly-once source connector error. Resolve EOS source connector issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Exactly-Once Source Connector Error

The exactly-once source connector fails. The offset and record tracking are not properly coordinated.

## Common Causes

- exactly.once.support is not enabled
- Connector does not support EOS
- Offset flush is misconfigured

## How to Fix

### Solution 1

```bash
grep 'exactly.once\|offset.flush' /etc/kafka/connect-distributed.properties
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
