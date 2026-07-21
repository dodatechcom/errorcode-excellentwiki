---
title: "[Solution] Kafka Processor Not Connected Error"
description: "Fix Kafka processor not connected error. Resolve Streams processor wiring issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Processor Not Connected Error

A processor in the Streams topology is not connected to other processors. The topology graph is broken.

## Common Causes

- Processor was not added to topology
- Edges are missing between processors
- Branch predicate is wrong

## How to Fix

### Solution 1

```bash
grep -i 'processor\|topology' /path/to/streams-logs/stderr.log
```

## Related Pages

- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})
- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})
- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})
- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})
