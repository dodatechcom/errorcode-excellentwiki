---
title: "[Solution] Spring HikariCP Error"
description: "Fix Spring HikariCP connection pool errors when connections are exhausted, timeout, or fail to initialize."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

HikariCP errors occur when the connection pool is exhausted, connections cannot be acquired, or pool configuration is incorrect.

## Common Causes

- Pool size too small for traffic
- Connections not returned to pool (leak)
- Connection timeout too short
- Database server rejecting connections
- Idle connections expired by database

## How to Fix

### Configure HikariCP

```yaml
# application.yml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      idle-timeout: 300000
      connection-timeout: 20000
      max-lifetime: 1800000
      leak-detection-threshold: 60000
      pool-name: MyHikariPool
```

### Monitor Pool Statistics

```java
@Component
public class DataSourceMonitor {
    @Autowired
    private HikariDataSource dataSource;

    public Map<String, Object> getPoolStats() {
        HikariPoolMXBean poolMXBean = dataSource.getHikariPoolMXBean();
        Map<String, Object> stats = new HashMap<>();
        stats.put("totalConnections", poolMXBean.getTotalConnections());
        stats.put("activeConnections", poolMXBean.getActiveConnections());
        stats.put("idleConnections", poolMXBean.getIdleConnections());
        stats.put("threadsAwaitingConnection", poolMXBean.getThreadsAwaitingConnection());
        return stats;
    }
}
```

### Handle Connection Leaks

```java
// Always close connections in finally block
try (Connection conn = dataSource.getConnection();
     PreparedStatement stmt = conn.prepareStatement(sql)) {
    ResultSet rs = stmt.executeQuery();
    // Process results
}
```

## Examples

```yaml
# Bug -- pool too small
spring:
  datasource:
    hikari:
      maximum-pool-size: 5  # Too small for production

# Fix -- appropriate pool size
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      idle-timeout: 300000
```

Monitor pool in logs: set `spring.datasource.hikari.leak-detection-threshold=60000`
