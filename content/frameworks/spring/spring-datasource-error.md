---
title: "[Solution] Spring DataSource Error"
description: "Fix Spring DataSource configuration errors when database connections fail or pooling is misconfigured."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

DataSource errors occur when the database connection cannot be established, the pool is exhausted, or the JDBC URL is incorrect.

## Common Causes

- JDBC URL or credentials incorrect
- Database driver not in classpath
- Connection pool size too small
- Driver class name not specified
- HikariCP or DBCP2 not configured

## How to Fix

### Configure DataSource

```yaml
# application.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: postgres
    password: secret
    driver-class-name: org.postgresql.Driver
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      idle-timeout: 300000
      connection-timeout: 20000
```

### Configure HikariCP

```java
@Configuration
public class DataSourceConfig {
    @Bean
    public HikariDataSource dataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
        config.setUsername("postgres");
        config.setPassword("secret");
        config.setMaximumPoolSize(20);
        config.setMinimumIdle(5);
        return new HikariDataSource(config);
    }
}
```

### Test DataSource Connection

```java
@Component
public class DataSourceHealthCheck {
    @Autowired
    private DataSource dataSource;

    public boolean isHealthy() {
        try (Connection conn = dataSource.getConnection()) {
            return conn.isValid(5);
        } catch (SQLException e) {
            return false;
        }
    }
}
```

## Examples

```yaml
# Bug -- wrong driver class
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    driver-class-name: com.mysql.cj.jdbc.Driver  # Wrong!

# Fix -- correct driver
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    driver-class-name: org.postgresql.Driver
```

Ensure the JDBC driver JAR is in the classpath.
