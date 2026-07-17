---
title: "[Solution] KafkaContainer Startup Failed — Testcontainers Kafka Fix"
description: "Fix KafkaContainer startup failure in Testcontainers. Check Docker, image availability, and configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# KafkaContainer Startup Failed — Testcontainers Kafka Fix

A KafkaContainer fails to start in Testcontainers. This prevents integration tests from running against a real Kafka instance.

## What This Error Means

Common message:

- `Container startup failed`
- `org.testcontainers.containers.ContainerLaunchException: Container startup failed`

## Common Causes

```java
// Cause 1: Docker not running
KafkaContainer kafka = new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:7.5.0"));
kafka.start();  // DockerException

// Cause 2: Image not available
// Cannot pull confluentinc/cp-kafka

// Cause 3: Port conflict

// Cause 4: Insufficient memory
// Kafka needs at least 512MB
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class KafkaIntegrationTest {

    @Container
    static KafkaContainer kafka = new KafkaContainer(
        DockerImageName.parse("confluentinc/cp-kafka:7.5.0"));

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.kafka.bootstrap-servers", kafka::getBootstrapServers);
    }

    @Test
    void shouldProduceAndConsume() {
        // Test with real Kafka
    }
}
```

### Fix 2: Configure with KRaft mode

```java
KafkaContainer kafka = new KafkaContainer(
    DockerImageName.parse("confluentinc/cp-kafka:7.5.0"))
    .withKraft();  // Use KRaft instead of Zookeeper
```

### Fix 3: Set resource limits

```java
KafkaContainer kafka = new KafkaContainer(
    DockerImageName.parse("confluentinc/cp-kafka:7.5.0"))
    .withCreateContainerCmdModifier(cmd -> {
        cmd.getHostConfig().withMemory(1024L * 1024 * 1024);
    });
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "kafka-consumer" >}} — CommitFailedException
- {{< relref "spring-kafka-concurrency" >}} — IllegalContainerGroupIdException
