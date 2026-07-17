---
title: "[Solution] Testcontainers MySQL Container Failed Fix"
description: "Fix Testcontainers MySQL container startup failures. Resolve image issues, initialization script errors, and connection problems."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "mysql", "docker", "integration-test", "database"]
weight: 5
---

# Testcontainers MySQL Container Failed Fix

A Testcontainers MySQL container failure occurs when the MySQL container cannot start, complete initialization, or accept connections within the expected timeout.

## What This Error Means

Common messages:

- `ContainerLaunchException: Container failed to start`
- `Communications link failure: The last packet sent successfully was 0 ms ago`
- `MYSQL CommunicationsException: Connection refused`
- `MySQLNonTransientConnectionException: Unable to connect to database`

The MySQL Docker container started but failed to initialize within the timeout, or the JDBC connection cannot reach the containerized MySQL instance.

## Common Causes

```java
// Cause 1: Docker image not available locally and pull fails
MySQLContainer<?> mysql = new MySQLContainer<>(
    DockerImageName.parse("mysql:8.0")
);
mysql.start();  // ContainerLaunchException

// Cause 2: Init script with SQL errors
MySQLContainer<?> mysql = new MySQLContainer<>(
    DockerImageName.parse("mysql:8.0")
).withInitScript("bad-init.sql");  // SQL syntax error in script

// Cause 3: Insufficient memory for MySQL
// MySQL needs ~512MB+ to start

// Cause 4: Port conflict
// MySQL default port 3306 already in use on host
```

## How to Fix

### Fix 1: Use @Container for lifecycle management

```java
@Testcontainers
class MySQLIntegrationTest {

    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>(
        DockerImageName.parse("mysql:8.0")
    )
    .withDatabaseName("testdb")
    .withUsername("test")
    .withPassword("test");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", mysql::getJdbcUrl);
        registry.add("spring.datasource.username", mysql::getUsername);
        registry.add("spring.datasource.password", mysql::getPassword);
    }

    @Test
    void testDatabase() {
        String jdbcUrl = mysql.getJdbcUrl();
        // Use JDBC URL for testing
    }
}
```

### Fix 2: Use correct init script path

```java
MySQLContainer<?> mysql = new MySQLContainer<>(
    DockerImageName.parse("mysql:8.0")
).withInitScript("db/init.sql");  // Path relative to classpath root
```

### Fix 3: Set sufficient memory

```java
MySQLContainer<?> mysql = new MySQLContainer<>(
    DockerImageName.parse("mysql:8.0")
).withCreateContainerCmdModifier(cmd -> {
    cmd.getHostConfig().withMemory(1024L * 1024 * 1024);  // 1GB
});
```

### Fix 4: Use test-specific database isolation

```java
@Container
static MySQLContainer<?> mysql = new MySQLContainer<>(
    DockerImageName.parse("mysql:8.0")
)
.withDatabaseName("test_" + UUID.randomUUID().toString().substring(0, 8))
.withUsername("test")
.withPassword("test");
```

### Fix 5: Add startup timeout

```java
MySQLContainer<?> mysql = new MySQLContainer<>(
    DockerImageName.parse("mysql:8.0")
).withStartupTimeout(Duration.ofSeconds(120));
```

## Related Errors

- {{< relref "testcontainers" >}} — Testcontainers general error.
- {{< relref "testcontainers-postgres" >}} — Testcontainers PostgreSQL error.
