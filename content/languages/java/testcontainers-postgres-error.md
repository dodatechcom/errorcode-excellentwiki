---
title: "[Solution] Testcontainers PostgreSQL Container Failed Fix"
description: "Fix Testcontainers PostgreSQL container startup failures. Resolve image issues, init script errors, and connection timeouts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "postgresql", "docker", "integration-test", "database"]
weight: 5
---

# Testcontainers PostgreSQL Container Failed Fix

A Testcontainers PostgreSQL container failure occurs when the PostgreSQL container cannot start, execute initialization scripts, or accept JDBC connections.

## What This Error Means

Common messages:

- `ContainerLaunchException: Container failed to start`
- `PSQLException: Connection refused`
- `FATAL: database "test" does not exist`
- `Communications link failure`

The PostgreSQL Docker container either failed to start, crashed during initialization, or the JDBC client cannot connect to the containerized database.

## Common Causes

```java
// Cause 1: Image not pulled correctly
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
    DockerImageName.parse("postgres:16")
);
postgres.start();  // ContainerLaunchException

// Cause 2: Init script has syntax errors
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
    DockerImageName.parse("postgres:16")
).withInitScript("schema.sql");  // SQL error in schema.sql

// Cause 3: Insufficient memory for PostgreSQL
// PostgreSQL needs ~256MB+ to start

// Cause 4: Concurrent container creation race condition
// Multiple test classes creating containers simultaneously
```

## How to Fix

### Fix 1: Use @Container with @DynamicPropertySource

```java
@Testcontainers
class PostgreSQLIntegrationTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
        DockerImageName.parse("postgres:16")
    )
    .withDatabaseName("testdb")
    .withUsername("test")
    .withPassword("test");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }
}
```

### Fix 2: Use valid init scripts

```sql
-- src/test/resources/db/schema.sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);
```

### Fix 3: Share container across test classes

```java
public class TestContainerConfig {
    public static final PostgreSQLContainer<?> postgres =
        new PostgreSQLContainer<>(DockerImageName.parse("postgres:16"))
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test")
            .withReuse(true);

    static {
        postgres.start();
    }
}
```

### Fix 4: Set resource limits

```java
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
    DockerImageName.parse("postgres:16")
).withCreateContainerCmdModifier(cmd -> {
    cmd.getHostConfig().withMemory(512L * 1024 * 1024);
});
```

### Fix 5: Add startup timeout and readiness check

```java
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
    DockerImageName.parse("postgres:16")
).waitingFor(Wait.forLogMessage(".*database system is ready to accept connections.*", 2)
    .withStartupTimeout(Duration.ofSeconds(60)));
```

## Related Errors

- {{< relref "testcontainers" >}} — Testcontainers general error.
- {{< relref "testcontainers-mysql" >}} — Testcontainers MySQL error.
