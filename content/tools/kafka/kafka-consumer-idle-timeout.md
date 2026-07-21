---
title: "[Solution] Kafka Consumer Idle Timeout Error"
description: "Fix Kafka consumer idle timeout errors. Resolve consumers being ejected from group due to inactivity."
tools: ["kafka"]
error-types: ["tool-error"]
severities: ["error"]
---

# Kafka Consumer Idle Timeout Error

Kafka consumer idle timeout errors occur when a consumer is removed from the group by the coordinator because it has not sent a heartbeat within the session timeout window.

## Common Causes

- Session timeout is too short for the processing workload
- Consumer thread blocked on a long-running processing task
- Network partition between consumer and coordinator
- Consumer poll interval exceeds max.poll.interval.ms

## How to Fix

1. Increase session timeout in consumer config:

```properties
session.timeout.ms=30000
heartbeat.interval.ms=10000
```

2. Increase max.poll.interval.ms for slow processors:

```properties
max.poll.interval.ms=600000
max.poll.records=50
```

3. Ensure poll() is called frequently enough:

```java
while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(10000));
    processRecords(records);
}
```

4. Check consumer group status:

```bash
kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group my-consumer-group --describe
```

## Examples

```bash
# Monitor consumer group liveness
watch -n 5 "kafka-consumer-groups.sh --bootstrap-server localhost:9092 \
  --group my-consumer-group --describe"
```
