---
title: "[Solution] Testcontainers Kafka Container Failed Fix"
description: "Fix Testcontainers Kafka container startup failures. Resolve image pull issues, port conflicts, and readiness check problems."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "kafka", "docker", "integration-test", "container"]
weight: 5
---

# Testcontainers Kafka Container Failed Fix

A Testcontainers Kafka container failure occurs when the Kafka container cannot start, become ready, or maintain stability during integration tests.

## What This Error Means

Common messages:

- `ContainerLaunchException: Container failed to start`
- `IllegalStateException: Kafka container failed to start`
- `org.testcontainers.containers.ContainerLaunchException: Timed out waiting for container port`
- `DockerException: Error response from daemon: Ports are not available`

The Testcontainers library started a Kafka Docker container but it failed to reach a healthy state within the timeout period, or the container crashed immediately after starting.

## Common Causes

```java
// Cause 1: Docker daemon not running
KafkaContainer kafka = new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:7.5.0"));
kafka.start();  // ContainerLaunchException

// Cause 2: Port conflict with existing Kafka
KafkaContainer kafka = new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:7.5.0"));
kafka.start();  // 9093 already in use

// Cause 3: Insufficient resources (CPU/memory)
// Container OOM killed by Docker

// Cause 4: Image pull failure (no internet or wrong registry)
KafkaContainer kafka = new KafkaContainer(
    DockerImageName.parse("wrong-registry.example.com/kafka:latest")
);
```

## How to Fix

### Fix 1: Ensure Docker is running

```bash
# Verify Docker daemon
docker info

# If not running
sudo systemctl start docker
```

### Fix 2: Use @Container annotation for automatic lifecycle

```java
@Testcontainers
class KafkaIntegrationTest {

    @Container
    static KafkaContainer kafka = new KafkaContainer(
        DockerImageName.parse("confluentinc/cp-kafka:7.5.0")
    ).withEmbeddedZookeeper();

    @Test
    void testKafkaProducer() {
        String bootstrapServers = kafka.getBootstrapServers();
        // Use bootstrapServers in producer config
    }
}
```

### Fix 3: Configure resource limits

```java
KafkaContainer kafka = new KafkaContainer(
    DockerImageName.parse("confluentinc/cp-kafka:7.5.0")
).withCreateContainerCmdModifier(cmd -> {
    cmd.getHostConfig().withMemory(2048L * 1024 * 1024);  // 2GB
    cmd.getHostConfig().withCpuPeriod(100000L);
    cmd.getHostConfig().withCpuQuota(50000L);  // 50% CPU
});
```

### Fix 4: Wait for readiness with custom strategy

```java
KafkaContainer kafka = new KafkaContainer(
    DockerImageName.parse("confluentinc/cp-kafka:7.5.0")
).waitingFor(Wait.forLogMessage(".*started.*KafkaServer.*", 1)
    .withStartupTimeout(Duration.ofSeconds(60)));
```

### Fix 5: Use shared container across test classes

```java
@Container
static KafkaContainer kafka = new KafkaContainer(
    DockerImageName.parse("confluentinc/cp-kafka:7.5.0")
).withReuse(true);  // Reuse across test runs
```

## Related Errors

- {{< relref "testcontainers" >}} — Testcontainers general error.
- {{< relref "testcontainers-localstack" >}} — Testcontainers LocalStack error.
