---
title: "IllegalContainerGroupIdException - Kafka concurrency"
description: "Spring Kafka throws IllegalContainerGroupIdException when the consumer group ID is invalid or conflicts"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring Kafka encounters an invalid consumer group ID or when multiple listeners share the same group with conflicting concurrency settings.

## Common Causes

- Consumer group ID is empty or contains invalid characters
- Multiple `@KafkaListener` methods share the same group but different concurrency
- Group ID contains reserved characters for Kafka
- Container factory misconfiguration for the group
- Group ID exceeds the maximum length (255 characters)

## How to Fix

1. Use a valid consumer group ID:

```java
@KafkaListener(
    topics = "orders",
    groupId = "order-processing-group",
    containerFactory = "kafkaListenerContainerFactory"
)
public void processOrder(Order order) {
    // Process the order
}
```

2. Ensure consistent concurrency settings:

```java
@Bean
public ConcurrentKafkaListenerContainerFactory<String, Order> kafkaListenerContainerFactory() {
    ConcurrentKafkaListenerContainerFactory<String, Order> factory =
        new ConcurrentKafkaListenerContainerFactory<>();
    factory.setConsumerFactory(consumerFactory());
    factory.setConcurrency(3); // Must match all listeners in this group
    return factory;
}
```

3. Use unique group IDs for independent consumers:

```java
@KafkaListener(groupId = "analytics-consumer")
public void analyticsListener(Order order) { ... }

@KafkaListener(groupId = "notification-consumer")
public void notificationListener(Order order) { ... }
```

## Examples

```java
// Group ID with invalid character
@KafkaListener(groupId = "order/group")
// IllegalContainerGroupIdException: Invalid group.id
```

## Related Errors

- [Kafka error (Rust)]({{< relref "/languages/rust/rdkafka-error-rs.md" >}})
- [AMQP error]({{< relref "/frameworks/spring/spring-amqp-error" >}})
