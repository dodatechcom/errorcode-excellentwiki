---
title: "[Solution] Testcontainers Container Startup Failure — Docker Test Fix"
description: "Fix Testcontainers container startup failures. Check Docker daemon, image availability, port conflicts, and resource limits."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Testcontainers Container Startup Failure — Docker Test Fix

Testcontainers fails to start a Docker container. This is a common issue in integration testing when Docker is not available, images cannot be pulled, or resources are insufficient.

## What This Error Means

Common messages:

- `Could not start container`
- `Container startup failed`
- `org.testcontainers.containers.ContainerLaunchException`
- `Docker daemon is not running`

## Common Causes

```java
// Cause 1: Docker not running
GenericContainer<?> container = new GenericContainer<>("postgres:15");
container.start();  // DockerException: Cannot connect to Docker daemon

// Cause 2: Port already in use
GenericContainer<?> container = new GenericContainer<>("postgres:15")
    .withFixedExposedPort(5432, 5432);

// Cause 3: Insufficient resources
// Docker container needs more memory than available
```

## How to Fix

### Fix 1: Ensure Docker is running

```bash
docker info
sudo systemctl start docker
```

### Fix 2: Use random ports

```java
GenericContainer<?> container = new GenericContainer<>("postgres:15")
    .withExposedPorts(5432)
    .withDatabaseName("test")
    .withUsername("test")
    .withPassword("test");

container.start();
String jdbcUrl = container.getJdbcUrl();
```

### Fix 3: Use @Container annotation

```java
@Testcontainers
class MyIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
        .withDatabaseName("test")
        .withUsername("test")
        .withPassword("test");

    @Test
    void shouldConnectToDatabase() {
        String jdbcUrl = postgres.getJdbcUrl();
    }
}
```

## Related Errors

- {{< relref "testcontainers-kafka" >}} — KafkaContainer startup failed
- {{< relref "testcontainers-mysql" >}} — MySQLContainer startup failed
- {{< relref "testcontainers-postgres" >}} — PostgreSQLContainer startup failed
