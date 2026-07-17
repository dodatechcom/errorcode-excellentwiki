---
title: "[Solution] PulsarContainer Startup Failed — Testcontainers Pulsar Fix"
description: "Fix PulsarContainer startup failure in Testcontainers. Check Docker and Pulsar configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PulsarContainer Startup Failed — Testcontainers Pulsar Fix

A PulsarContainer fails to start in Testcontainers. This prevents integration tests from running against a real Apache Pulsar instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
PulsarContainer pulsar = new PulsarContainer(DockerImageName.parse("apachepulsar/pulsar:3.1.0"));
pulsar.start();

// Cause 2: Insufficient resources
// Pulsar needs at least 1GB memory

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class PulsarIntegrationTest {

    @Container
    static PulsarContainer pulsar = new PulsarContainer(
        DockerImageName.parse("apachepulsar/pulsar:3.1.0"));

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.pulsar.service-url", pulsar::getPulsarBrokerUrl);
    }
}
```

### Fix 2: Set resource limits

```java
PulsarContainer pulsar = new PulsarContainer(
    DockerImageName.parse("apachepulsar/pulsar:3.1.0"))
    .withCreateContainerCmdModifier(cmd -> {
        cmd.getHostConfig().withMemory(2L * 1024 * 1024 * 1024);
    });
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "kafka-consumer" >}} — CommitFailedException
- {{< relref "spring-kafka-concurrency" >}} — IllegalContainerGroupIdException
