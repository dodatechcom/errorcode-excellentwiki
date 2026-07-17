---
title: "[Solution] IllegalContainerGroupIdException — Spring Kafka Concurrency Fix"
description: "Fix IllegalContainerGroupIdException in Spring Kafka when container group configuration conflicts. Configure consumer groups properly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# IllegalContainerGroupIdException — Spring Kafka Concurrency Fix

An `IllegalContainerGroupIdException` is thrown when Spring Kafka detects an illegal or conflicting container group ID configuration. This typically happens when multiple listeners share the same group but have different configurations.

## What This Error Means

Common messages:

- `IllegalContainerGroupIdException: Container group ID conflict`

## Common Causes

```java
// Cause 1: Conflicting group IDs
@KafkaListener(topics = "topic1", groupId = "my-group")
public void listen1(String message) { }

@KafkaListener(topics = "topic2", groupId = "my-group")
public void listen2(String message) { }
// Same group, different topics — may cause conflicts

// Cause 2: Container factory mismatch
@Bean
public ConcurrentKafkaListenerContainerFactory<String, String> factory() {
    ConcurrentKafkaListenerContainerFactory<String, String> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConcurrency(3);
    return factory;
}
```

## How to Fix

### Fix 1: Use different consumer groups

```java
@KafkaListener(topics = "topic1", groupId = "group-topic1")
public void listen1(String message) { }

@KafkaListener(topics = "topic2", groupId = "group-topic2")
public void listen2(String message) { }
```

### Fix 2: Configure container factory properly

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<String, String> kafkaListenerContainerFactory() {
    ConcurrentKafkaListenerContainerFactory<String, String> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.setConcurrency(3);
    factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL_IMMEDIATE);
    return factory;
}
```

### Fix 3: Use separate container factories

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<String, String> topic1Factory() {
    ConcurrentKafkaListenerContainerFactory<String, String> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.setConcurrency(3);
    return factory;
}

@Bean
public ConcurrentKafkaListenerContainerFactory<String, String> topic2Factory() {
    ConcurrentKafkaListenerContainerFactory<String, String> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.setConcurrency(5);
    return factory;
}

@KafkaListener(topics = "topic1", containerFactory = "topic1Factory")
public void listen1(String message) { }

@KafkaListener(topics = "topic2", containerFactory = "topic2Factory")
public void listen2(String message) { }
```

## Related Errors

- {{< relref "kafka-consumer" >}} — CommitFailedException
- {{< relref "testcontainers-kafka" >}} — KafkaContainer startup failed
- {{< relref "spring-amqp" >}} — AmqpException
