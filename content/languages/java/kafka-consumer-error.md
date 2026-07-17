---
title: "[Solution] Kafka CommitFailedException Fix"
description: "Fix Kafka CommitFailedException on consumer. Handle rebalance, adjust session timeouts, and manage offset commits."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["kafka", "consumer", "commit", "rebalance", "offset"]
weight: 5
---

# Kafka CommitFailedException Fix

A `CommitFailedException` is thrown when a Kafka consumer fails to commit offsets, typically because the consumer has been rebalanced or the group coordinator is unavailable.

## What This Error Means

Common messages:

- `org.apache.kafka.clients.consumer.CommitFailedException: Commit cannot be completed since the group has already started rebalancing`
- `CommitFailedException: the offset batch is empty`
- `WakeUpException: Consumer interrupted`

The consumer attempted to commit offsets but the group coordinator rejected the commit because a rebalance is in progress or the consumer's session has timed out.

## Common Causes

```java
// Cause 1: Processing takes too long, exceeding max.poll.interval.ms
consumer.subscribe(List.of("my-topic"));
while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    processRecords(records);  // Takes > 5 minutes (default max.poll.interval.ms)
    consumer.commitSync();    // CommitFailedException — rebalance already started
}

// Cause 2: Too many records per poll (exceeds max.poll.records)
// Consumer polls 100K records, processing triggers rebalance

// Cause 3: Coordinator unavailable during commit
consumer.commitSync();  // Group coordinator not responding

// Cause 4: Consumer died during processing
// OutOfMemoryError kills consumer, rebalance occurs
```

## How to Fix

### Fix 1: Increase session and poll timeouts

```properties
# consumer config
max.poll.interval.ms=600000  # 10 minutes
session.timeout.ms=45000     # 45 seconds
heartbeat.interval.ms=15000  # 15 seconds
max.poll.records=500
```

### Fix 2: Process records in smaller batches

```java
while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        processSingleRecord(record);
    }
    consumer.commitSync();
}
```

### Fix 3: Use manual partition assignment instead of subscribe

```java
consumer.assign(List.of(new TopicPartition("my-topic", 0)));
// No group rebalancing with manual assignment
```

### Fix 4: Handle rebalance with consumer rebalance listener

```java
consumer.subscribe(List.of("my-topic"), new ConsumerRebalanceListener() {
    @Override
    public void onPartitionsRevoked(Collection<TopicPartition> partitions) {
        commitCurrentOffsets();  // Commit before rebalance
    }

    @Override
    public void onPartitionsAssigned(Collection<TopicPartition> partitions) {
        // Reset state if needed
    }
});
```

### Fix 5: Use async commit for better performance

```java
consumer.commitAsync((offsets, exception) -> {
    if (exception != null) {
        log.error("Commit failed: {}", exception.getMessage());
    }
});
```

## Related Errors

- {{< relref "kafka-consumer" >}} — Kafka consumer general error.
- {{< relref "testcontainers-kafka" >}} — Testcontainers Kafka container error.
