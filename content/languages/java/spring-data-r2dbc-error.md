---
title: "[Solution] Spring Data R2DBC Connection Error Fix"
description: "Fix Spring Data R2DBC connection errors. Resolve driver configuration, connection pool issues, and database initialization problems."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring-data", "r2dbc", "reactive", "database", "connection"]
weight: 5
---

# Spring Data R2DBC Connection Error Fix

An R2DBC connection error occurs when Spring Data R2DBC cannot establish or maintain a reactive connection to the database.

## What This Error Means

Common messages:

- `io.r2dbc.spi.R2dbcNonTransientResourceException: Connection refused`
- `R2dbcConnectionException: Failed to obtain R2DBC Connection`
- `PoolAcquisitionTimeoutException: Timeout acquiring connection from pool`
- `CannotAcquireLockException: deadlock detected`

R2DBC (Reactive Relational Database Connectivity) failed to connect to the database or the connection pool is exhausted. This is the reactive equivalent of JDBC connection failures.

## Common Causes

```java
// Cause 1: Wrong R2DBC URL format
// JDBC: jdbc:postgresql://localhost:5432/mydb
// R2DBC: r2dbc:postgresql://localhost:5432/mydb

// Cause 2: Missing R2DBC driver dependency
// Need r2dbc-postgresql, not postgresql (JDBC)

// Cause 3: Connection pool configuration issue
// Too few connections for concurrent requests

// Cause 4: Database not running
R2dbcDataSource dataSource = ...;
Mono.from(dataSource.getConnection())  // Connection refused
```

## How to Fix

### Fix 1: Configure R2DBC connection URL correctly

```yaml
# application.yml
spring:
  r2dbc:
    url: r2dbc:postgresql://localhost:5432/mydb
    username: user
    password: pass
```

### Fix 2: Add correct R2DBC driver dependency

```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>r2dbc-postgresql</artifactId>
</dependency>
<!-- Do NOT use postgresql (JDBC driver) for R2DBC -->
```

### Fix 3: Configure connection pool

```yaml
spring:
  r2dbc:
    url: r2dbc:postgresql://localhost:5432/mydb
    pool:
      initial-size: 5
      max-size: 20
      max-idle-time: 30m
      max-acquire-time: 30s
      max-create-connection-time: 5s
```

### Fix 4: Use ConnectionFactory with custom configuration

```java
@Configuration
public class R2dbcConfig {

    @Bean
    public ConnectionFactory connectionFactory() {
        return ConnectionFactories.get(ConnectionFactoryOptions.builder()
            .option(DRIVER_NAME, "postgresql")
            .option(HOST, "localhost")
            .option(PORT, 5432)
            .option(DATABASE, "mydb")
            .option(USER, "user")
            .option(PASSWORD, "pass")
            .build());
    }
}
```

### Fix 5: Handle connection errors reactively

```java
@Service
public class UserService {

    private final R2dbcEntityTemplate template;

    public Mono<User> findById(Long id) {
        return template.selectOneById(id, User.class)
            .onErrorResume(R2dbcException.class, e -> {
                log.error("Database error: {}", e.getMessage());
                return Mono.empty();
            });
    }
}
```

## Related Errors

- {{< relref "spring-data-r2dbc" >}} — Spring Data R2DBC general error.
- {{< relref "spring-graphql" >}} — Spring GraphQL error.
