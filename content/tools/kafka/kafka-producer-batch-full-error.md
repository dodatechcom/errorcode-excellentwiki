---
title: "[Solution] Kafka Producer Batch Full Error"
description: "Fix Kafka producer batch full errors. Resolve RecordTooLargeException and batch accumulation issues."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Producer Batch Full Error

Kafka producer batch full errors occur when the producer's in-memory batch buffer fills up before it can be sent to the broker, typically resulting in RecordTooLargeException.

## Common Causes

- batch.size too small for the message throughput
- linger.ms too low, not allowing enough time for batching
- Individual message larger than max.request.size
- Network backpressure preventing batch flush

## How to Fix

1. Increase the batch size and linger time:

```properties
batch.size=65536
linger.ms=50
buffer.memory=67108864
```

2. Increase max.request.size for large messages:

```properties
max.request.size=10485760
```

3. Check if broker has message size limits:

```properties
# On broker
message.max.bytes=10485760
replica.fetch.max.bytes=10485760
```

4. Handle the exception in the producer:

```java
producer.send(record, (metadata, exception) -> {
    if (exception != null) {
        log.error("Failed to send record: {}", exception.getMessage());
    }
});
```

## Examples

```bash
# Monitor producer metrics
kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 --topic my-topic --time -1

# Check broker message size limit
kafka-configs.sh --describe --bootstrap-server localhost:9092 \
  --entity-type brokers --entity-default --all
```
