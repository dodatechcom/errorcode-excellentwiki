---
title: "[Solution] GenericContainer Redis Startup Failed — Testcontainers Redis Fix"
description: "Fix Redis container startup failure in Testcontainers. Check Docker and Redis configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GenericContainer Redis Startup Failed — Testcontainers Redis Fix

A Redis container fails to start in Testcontainers. This prevents integration tests from running against a real Redis instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
GenericContainer<?> redis = new GenericContainer<>(DockerImageName.parse("redis:7-alpine"));
redis.start();

// Cause 2: Port conflict
// Port 6379 already in use
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class RedisIntegrationTest {

    @Container
    static GenericContainer<?> redis = new GenericContainer<>(DockerImageName.parse("redis:7-alpine"))
        .withExposedPorts(6379);

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.data.redis.host", redis::getHost);
        registry.add("spring.data.redis.port", () -> redis.getMappedPort(6379));
    }
}
```

### Fix 2: Use RedisStack for modules

```java
GenericContainer<?> redis = new GenericContainer<>(DockerImageName.parse("redis/redis-stack-server:latest"))
    .withExposedPorts(6379);
```

### Fix 3: Configure with password

```java
GenericContainer<?> redis = new GenericContainer<>(DockerImageName.parse("redis:7-alpine"))
    .withExposedPorts(6379)
    .withCommand("redis-server", "--requirepass", "testpass");
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "spring-cache" >}} — CacheAccessException
- {{< relref "spring-data-elasticsearch" >}} — ElasticsearchException
