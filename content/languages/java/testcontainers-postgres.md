---
title: "[Solution] PostgreSQLContainer Startup Failed — Testcontainers PostgreSQL Fix"
description: "Fix PostgreSQLContainer startup failure in Testcontainers. Check Docker, image, and PostgreSQL configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "postgresql", "docker", "container", "database"]
weight: 5
---

# PostgreSQLContainer Startup Failed — Testcontainers PostgreSQL Fix

A PostgreSQLContainer fails to start in Testcontainers. This prevents integration tests from running against a real PostgreSQL instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(DockerImageName.parse("postgres:15"));
postgres.start();

// Cause 2: Insufficient resources
// PostgreSQL needs at least 256MB memory

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class PostgreSQLIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(DockerImageName.parse("postgres:15"))
        .withDatabaseName("testdb")
        .withUsername("test")
        .withPassword("test");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }
}
```

### Fix 2: Use init script

```java
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(DockerImageName.parse("postgres:15"))
    .withDatabaseName("testdb")
    .withInitScript("schema.sql");
```

### Fix 3: Configure with PostGIS extension

```java
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(DockerImageName.parse("postgis/postgis:15-3.4"))
    .withDatabaseName("testdb");
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "testcontainers-mysql" >}} — MySQLContainer startup failed
- {{< relref "hibernate-dialect" >}} — SQLDialect not found
