---
title: "DataSource connection error"
description: "Spring fails to establish a database connection through the configured DataSource"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring's DataSource cannot connect to the database, typically due to incorrect JDBC URL, credentials, or the database server being unreachable.

## Common Causes

- Incorrect JDBC URL, username, or password in `application.properties`
- Database server not running or not accessible from the application
- Connection pool exhausted (too many active connections)
- Missing JDBC driver dependency

## How to Fix

1. Verify your `application.yml` configuration:

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: dbuser
    password: dbpass
    hikari:
      maximum-pool-size: 10
      connection-timeout: 30000
```

2. Add retry logic for transient connection failures:

```java
@Configuration
@EnableRetry
public class AppConfig {
    // Spring Retry handles transient failures
}
```

3. Configure a health check endpoint:

```java
@RestController
public class HealthController {
    @Autowired
    private DataSource dataSource;

    @GetMapping("/health")
    public Map<String, String> health() throws SQLException {
        try (Connection conn = dataSource.getConnection()) {
            return Map.of("status", "UP");
        }
    }
}
```

4. Ensure the JDBC driver is in the classpath:

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <scope>runtime</scope>
</dependency>
```

## Examples

```text
org.postgresql.util.PSQLException: Connection refused. Check that the hostname and port are correct and that the postmaster is accepting TCP/IP connections.
```

## Related Errors

- [No qualifying bean of type]({{< relref "/frameworks/spring/bean-not-found" >}})
