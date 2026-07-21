---
title: "[Solution] Kafka Source Connector Error"
description: "Fix Kafka source connector error. Resolve source connector data ingestion issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Source Connector Error

The source connector fails to ingest data from the source system. This can be caused by connectivity issues, authentication failures, or schema problems.

## Common Causes

- Source system is unreachable
- Authentication failed
- Schema does not match

## How to Fix

### Solution 1

```bash
curl http://localhost:8083/connectors/my-source/status
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
