---
title: "[Solution] Kafka Punctuation Not Scheduled Error"
description: "Fix Kafka punctuation not scheduled error. Resolve Streams periodic task scheduling issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Punctuation Not Scheduled Error

The punctuation (periodic callback) in Kafka Streams is not being scheduled. The processor does not execute timed operations.

## Common Causes

- Punctuation was not registered
- Scheduler is not started
- Interval is too large

## How to Fix

### Solution 1

```bash
grep -i 'punctuation\|scheduler' /path/to/streams-logs/stderr.log
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
