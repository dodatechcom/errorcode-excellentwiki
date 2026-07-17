---
title: "[Solution] MariaDBContainer Startup Failed — Testcontainers MariaDB Fix"
description: "Fix MariaDBContainer startup failure in Testcontainers. Check Docker and MariaDB configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "mariadb", "docker", "container", "database"]
weight: 5
---

# MariaDBContainer Startup Failed — Testcontainers MariaDB Fix

A MariaDBContainer fails to start in Testcontainers. This prevents integration tests from running against a real MariaDB instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
MariaDBContainer<?> mariadb = new MariaDBContainer<>(DockerImageName.parse("mariadb:11"));
mariadb.start();

// Cause 2: Insufficient resources

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class MariaDBIntegrationTest {

    @Container
    static MariaDBContainer<?> mariadb = new MariaDBContainer<>(DockerImageName.parse("mariadb:11"))
        .withDatabaseName("testdb")
        .withUsername("test")
        .withPassword("test");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mariadb::getJdbcUrl);
        registry.add("spring.datasource.username", mariadb::getUsername);
        registry.add("spring.datasource.password", mariadb::getPassword);
    }
}
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "testcontainers-mysql" >}} — MySQLContainer startup failed
- {{< relref "sql-exception" >}} — SQL exception
