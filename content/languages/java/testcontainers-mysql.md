---
title: "[Solution] MySQLContainer Startup Failed — Testcontainers MySQL Fix"
description: "Fix MySQLContainer startup failure in Testcontainers. Check Docker, image, and MySQL configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MySQLContainer Startup Failed — Testcontainers MySQL Fix

A MySQLContainer fails to start in Testcontainers. This prevents integration tests from running against a real MySQL instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
MySQLContainer<?> mysql = new MySQLContainer<>(DockerImageName.parse("mysql:8.0"));
mysql.start();

// Cause 2: Insufficient resources
// MySQL needs at least 256MB memory

// Cause 3: Port conflict
// Port 3306 already in use
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class MySQLIntegrationTest {

    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>(DockerImageName.parse("mysql:8.0"))
        .withDatabaseName("testdb")
        .withUsername("test")
        .withPassword("test");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
    }
}
```

### Fix 2: Use MariaDB as alternative

```java
MariaDBContainer<?> mariaDB = new MariaDBContainer<>(DockerImageName.parse("mariadb:11"))
    .withDatabaseName("testdb")
    .withUsername("test")
    .withPassword("test");
```

### Fix 3: Initialize with SQL script

```java
MySQLContainer<?> mysql = new MySQLContainer<>(DockerImageName.parse("mysql:8.0"))
    .withDatabaseName("testdb")
    .withInitScript("schema.sql");
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "testcontainers-postgres" >}} — PostgreSQLContainer startup failed
- {{< relref "sql-exception" >}} — SQL exception
