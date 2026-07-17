---
title: "[Solution] ConsulContainer Startup Failed — Testcontainers Consul Fix"
description: "Fix ConsulContainer startup failure in Testcontainers. Check Docker and Consul configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ConsulContainer Startup Failed — Testcontainers Consul Fix

A ConsulContainer fails to start in Testcontainers. This prevents integration tests from running against a real Consul instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
GenericContainer<?> consul = new GenericContainer<>(DockerImageName.parse("consul:1.17"));
consul.start();

// Cause 2: Port conflict
// Port 8500 already in use
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class ConsulIntegrationTest {

    @Container
    static GenericContainer<?> consul = new GenericContainer<>(DockerImageName.parse("consul:1.17"))
        .withExposedPorts(8500)
        .withCommand("agent", "-dev", "-client", "0.0.0.0");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.cloud.consul.host", consul::getHost);
        registry.add("spring.cloud.consul.port", () -> consul.getMappedPort(8500));
    }
}
```

### Fix 2: Use with Spring Cloud Consul

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-consul-config</artifactId>
</dependency>
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "spring-cloud-config" >}} — ConfigDataException
- {{< relref "spring-cloud-gateway" >}} — ResponseStatusException: 502
