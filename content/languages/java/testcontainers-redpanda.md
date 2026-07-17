---
title: "[Solution] RedpandaContainer Startup Failed — Testcontainers Redpanda Fix"
description: "Fix RedpandaContainer startup failure in Testcontainers. Check Docker and Redpanda configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "redpanda", "docker", "container", "kafka"]
weight: 5
---

# RedpandaContainer Startup Failed — Testcontainers Redpanda Fix

A RedpandaContainer fails to start in Testcontainers. This prevents integration tests from running against a real Redpanda instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
RedpandaContainer redpanda = new RedpandaContainer(DockerImageName.parse("docker.redpanda.com/vectorizedio/redpanda:v23.3.1"));
redpanda.start();

// Cause 2: Insufficient resources

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class RedpandaIntegrationTest {

    @Container
    static RedpandaContainer redpanda = new RedpandaContainer(
        DockerImageName.parse("docker.redpanda.com/vectorizedio/redpanda:v23.3.1"));

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.kafka.bootstrap-servers", redpanda::getBootstrapServers);
    }
}
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "testcontainers-kafka" >}} — KafkaContainer startup failed
- {{< relref "kafka-consumer" >}} — CommitFailedException
