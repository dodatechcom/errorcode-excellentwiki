---
title: "[Solution] RabbitMQContainer Startup Failed — Testcontainers RabbitMQ Fix"
description: "Fix RabbitMQContainer startup failure in Testcontainers. Check Docker and RabbitMQ configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# RabbitMQContainer Startup Failed — Testcontainers RabbitMQ Fix

A RabbitMQContainer fails to start in Testcontainers. This prevents integration tests from running against a real RabbitMQ instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
RabbitMQContainer rabbit = new RabbitMQContainer(DockerImageName.parse("rabbitmq:3.12-management"));
rabbit.start();

// Cause 2: Management plugin not available
// Using non-management image but accessing management UI

// Cause 3: Insufficient resources
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class RabbitMQIntegrationTest {

    @Container
    static RabbitMQContainer rabbit = new RabbitMQContainer(
        DockerImageName.parse("rabbitmq:3.12-management"))
        .withExposedPorts(5672, 15672);

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.rabbitmq.host", rabbit::getHost);
        registry.add("spring.rabbitmq.port", () -> rabbit.getMappedPort(5672));
    }
}
```

### Fix 2: Create exchanges and queues

```java
@Container
static RabbitMQContainer rabbit = new RabbitMQContainer(DockerImageName.parse("rabbitmq:3.12"))
    .withExchange("my-exchange", "direct")
    .withQueue("my-queue")
    .withBinding("my-exchange", "my-queue");
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "spring-amqp" >}} — AmqpException
- {{< relref "spring-kafka-concurrency" >}} — IllegalContainerGroupIdException
