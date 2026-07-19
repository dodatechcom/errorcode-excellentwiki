---
title: "[Solution] JDBC Unable to Acquire Connection — Pool Timeout"
description: "Fix java.sql.SQLException Unable to acquire JDBC Connection. Resolve connection pool timeout issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Unable to Acquire Connection — Pool Timeout

A `SQLException` with message `Unable to acquire JDBC Connection` indicates the connection pool could not provide a connection within the configured timeout period. This is a variation of pool exhaustion often seen with Spring's `DataSourceUtils` or JPA's `EntityManagerFactory`.

## What This Error Means

When all connections in the pool are in use and no connection becomes available within the timeout, the pool throws this error. It is commonly wrapped by Spring's `DataAccessException` or JPA's `PersistenceException`.

## Common Causes

```java
// Cause 1: High concurrency exhausting pool
// 50 threads compete for 10 connections — 40 will timeout

// Cause 2: Connection leak (not returned to pool)
Connection conn = dataSource.getConnection();
// Exception thrown before conn.close() — connection leaked

// Cause 3: Pool configuration too restrictive
HikariConfig config = new HikariConfig();
config.setMaximumPoolSize(5);
config.setConnectionTimeout(3000);  // Only 3 seconds to wait
```

## How to Fix

### Fix 1: Increase pool size and timeout

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setUsername("dbuser");
config.setPassword("dbpass");
config.setMaximumPoolSize(30);
config.setMinimumIdle(10);
config.setConnectionTimeout(30000);  // 30 seconds to get a connection
config.setIdleTimeout(600000);
config.setMaxLifetime(1800000);
HikariDataSource ds = new HikariDataSource(config);
```

### Fix 2: Detect and fix connection leaks

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setLeakDetectionThreshold(10000);  // Log leak if connection held > 10s
config.setPoolName("LeakDetectionPool");
// Check logs for: "Connection leak detection triggered for connection..."
```

### Fix 3: Use connection pool monitoring

```java
HikariPoolMXBean poolProxy = ds.getHikariPoolMXBean();
log.info("Active connections: {}", poolProxy.getActiveConnections());
log.info("Idle connections: {}", poolProxy.getIdleConnections());
log.info("Threads awaiting connection: {}", poolProxy.getThreadsAwaitingConnection());
log.info("Total connections: {}", poolProxy.getTotalConnections());
```

### Fix 4: Add circuit breaker pattern for database calls

```java
@Service
public class DatabaseService {
    private final CircuitBreaker circuitBreaker = CircuitBreaker.ofDefaults("db");

    public List<User> findUsers() {
        return CircuitBreaker.decorateSupplier(circuitBreaker, () -> {
            try (Connection conn = dataSource.getConnection();
                 PreparedStatement ps = conn.prepareStatement("SELECT * FROM users")) {
                ResultSet rs = ps.executeQuery();
                return mapResults(rs);
            }
        }).get();
    }
}
```

## Prevention Tips

- Right-size your connection pool based on actual concurrency needs.
- Enable leak detection in development and staging environments.
- Monitor pool metrics (active, idle, waiting threads) in production.
- Keep database transactions short to release connections quickly.

## Related Errors

- {{< relref "jdbc-connection-pool-exhausted" >}} — Pool exhausted
- {{< relref "jdbc-conn" >}} — Cannot establish JDBC connection
- {{< relref "connection-timeout" >}} — Connection timeout
