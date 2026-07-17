---
title: "[Solution] CommitFailedException — Kafka Consumer Fix"
description: "Fix CommitFailedException when Kafka consumer fails to commit offsets. Handle rebalancing and offset management."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# CommitFailedException — Kafka Consumer Fix

A `CommitFailedException` is thrown when a Kafka consumer fails to commit offsets. This typically happens during rebalancing when the consumer takes too long to process records.

## What This Error Means

Common message:

- `CommitFailedException: offset commit failed on group`
- `CommitFailedException: This consumer has already been unsubscribed`

## Common Causes

```java
// Cause 1: Processing takes too long
@KafkaListener(topics = "my-topic")
public void listen(ConsumerRecord<String, String> record) {
    Thread.sleep(60000);  // Exceeds max.poll.interval.ms
    // Rebalance triggered, commit fails
}

// Cause 2: Session timeout expired
// Consumer didn't heartbeat in time
```

## How to Fix

### Fix 1: Configure poll interval

```properties
spring.kafka.consumer.max-poll-interval=60000
spring.kafka.listener.ack-mode=manual
```

### Fix 2: Process records asynchronously

```java
@KafkaListener(topics = "my-topic")
public void listen(ConsumerRecord<String, String> record) {
    asyncProcessor.process(record);
}
```

### Fix 3: Increase session timeout

```properties
spring.kafka.consumer.session-timeout=30000
spring.kafka.consumer.heartbeat-interval=10000
```

### Fix 4: Use manual commit

```java
@KafkaListener(topics = "my-topic", containerFactory = "kafkaListenerContainerFactory")
public void listen(ConsumerRecord<String, String> record,
                   Acknowledgment acknowledgment) {
    processRecord(record);
    acknowledgment.acknowledge();
}
```

## Related Errors

- {{< relref "spring-kafka-concurrency" >}} — IllegalContainerGroupIdException
- {{< relref "testcontainers-kafka" >}} — KafkaContainer startup failed
- {{< relref "connection-timeout" >}} — Connection timeout
