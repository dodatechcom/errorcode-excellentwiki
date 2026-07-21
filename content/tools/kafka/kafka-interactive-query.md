---
title: "[Solution] Kafka Interactive Query Error"
description: "Fix Kafka interactive query error. Resolve Streams interactive query issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Interactive Query Error

Interactive queries to a Kafka Streams application fail. The state store is not available or the query is incorrectly formed.

## Common Causes

- State store is not queryable
- Streams app is not running
- Store name does not match

## How to Fix

### Solution 1

```bash
grep -i 'interactive.query\|queryable' /path/to/streams-logs/stderr.log
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
