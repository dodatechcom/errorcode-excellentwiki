---
title: "[Solution] JDBC Connection Pool Exhausted — Timeout Waiting for Idle Object"
description: "Fix java.sql.SQLException Cannot get a connection pool error Timeout waiting for idle object. Tune HikariCP connection pool settings."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# JDBC Connection Pool Exhausted — Timeout Waiting for Idle Object

A `SQLException` with message `Cannot get a connection, pool error Timeout waiting for idle object` is thrown when all connections in the pool are currently in use and no idle connection is available within the configured timeout period.

## What This Error Means

This error originates from the connection pool (typically HikariCP or Apache DBCP) when a thread requests a database connection but every connection in the pool is already checked out by other threads. The pool waits for the configured timeout, then throws this exception.

## Common Causes

```java
// Cause 1: Connections not properly closed (leak)
Connection conn = dataSource.getConnection();
// ... forgot to close or close() not reached due to exception

// Cause 2: Pool size too small for workload
HikariConfig config = new HikariConfig();
config.setMaximumPoolSize(5);  // Too few connections for high concurrency

// Cause 3: Long-running queries holding connections
Connection conn = dataSource.getConnection();
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM large_table"); // Runs for minutes
```

## How to Fix

### Fix 1: Ensure connections are always closed with try-with-resources

```java
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?")) {
    ps.setLong(1, userId);
    ResultSet rs = ps.executeQuery();
    while (rs.next()) {
        processUser(rs);
    }
} // Connection automatically returned to pool
```

### Fix 2: Increase pool size and tune timeouts

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setUsername("dbuser");
config.setPassword("dbpass");
config.setMaximumPoolSize(20);
config.setMinimumIdle(5);
config.setConnectionTimeout(30000);  // 30 seconds
config.setIdleTimeout(600000);        // 10 minutes
config.setMaxLifetime(1800000);       // 30 minutes
HikariDataSource ds = new HikariDataSource(config);
```

### Fix 3: Monitor and detect connection leaks

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setLeakDetectionThreshold(5000);  // Log warning if connection held > 5s
config.setPoolName("MyAppPool");
```

### Fix 4: Reduce connection hold time with shorter transactions

```java
@Transactional(timeout = 10)  // Spring: timeout after 10 seconds
public List<Order> getOrdersForUser(Long userId) {
    return orderRepository.findByUserId(userId);
}
```

## Prevention Tips

- Always use try-with-resources for JDBC connections, statements, and result sets.
- Configure connection pool metrics and monitor active vs idle connections.
- Set `leakDetectionThreshold` in HikariCP during development.
- Keep transactions short; avoid holding connections during I/O or user input.

## Related Errors

- {{< relref "jdbc-conn" >}} — Cannot establish JDBC connection
- {{< relref "jdbc-pool-timeout" >}} — Pool timeout acquiring connection
- {{< relref "connection-timeout" >}} — Connection timeout error
