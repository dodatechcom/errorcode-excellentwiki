---
title: "[Solution] Java SQLTransientConnectionException — Temporary Connection Failure Fix"
description: "Fix Java SQLTransientConnectionException by implementing retry with backoff, checking connection pool health, and handling temporary outages."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 428
---

# SQLTransientConnectionException — Temporary Connection Failure Fix

A `SQLTransientConnectionException` is thrown when a connection to the database fails due to a temporary condition. The connection may succeed if retried after a short delay.

## Description

`java.sql.SQLTransientConnectionException` extends `SQLTransientException` and indicates a recoverable connection failure. The database server may be temporarily overloaded, the connection pool may be exhausted, or a network glitch may have caused the failure.

Common message variants:

- `SQLTransientConnectionException: Connection is not available`
- `SQLTransientConnectionException: Timed out waiting for connection`
- `SQLTransientConnectionException: Connection pool exhausted`
- `SQLTransientConnectionException: Unable to acquire JDBC Connection`

## Common Causes

```java
// Cause 1: Connection pool exhausted — all connections in use
HikariDataSource ds = new HikariDataSource();
ds.setMaximumPoolSize(5);
// 5 active connections, 6th request
Connection conn = ds.getConnection();  // SQLTransientConnectionException after timeout

// Cause 2: Database momentarily unreachable due to network blip
Properties props = new Properties();
props.setProperty("user", "dbuser");
props.setProperty("password", "dbpass");
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://remote-host:3306/mydb?connectTimeout=5000", props);
// Brief network interruption — SQLTransientConnectionException

// Cause 3: Database under heavy load — accepting connections slowly
HikariDataSource ds = new HikariDataSource();
ds.setConnectionTimeout(10000);  // 10 second pool timeout
Connection conn = ds.getConnection();  // Under load — SQLTransientConnectionException

// Cause 4: DNS resolution temporarily failing
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://db-primary.internal:3306/mydb", props);
// DNS blip — SQLTransientConnectionException

// Cause 5: Database restart in progress
Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/mydb", props);
// Server restarting — temporary failure
```

## Solutions

### Fix 1: Implement retry with exponential backoff

```java
public static Connection getConnectionWithRetry(DataSource ds, int maxRetries) throws SQLException {
    long delay = 500;  // Start with 500ms
    for (int attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            return ds.getConnection();
        } catch (SQLTransientConnectionException e) {
            if (attempt == maxRetries) throw e;
            System.err.println("Connection failed (attempt " + (attempt + 1) + "), retrying in " + delay + "ms");
            try {
                Thread.sleep(delay);
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
                throw e;
            }
            delay = Math.min(delay * 2, 15000);  // Cap at 15 seconds
        }
    }
    throw new SQLException("Could not obtain connection after " + maxRetries + " retries");
}
```

### Fix 2: Configure connection pool for resilience

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
config.setMaximumPoolSize(20);
config.setMinimumIdle(5);
config.setConnectionTimeout(30000);    // 30 seconds to wait for connection
config.setIdleTimeout(600000);         // 10 minutes idle timeout
config.setMaxLifetime(1800000);        // 30 minutes max lifetime
config.setLeakDetectionThreshold(60000); // Detect connection leaks after 60s

// Connection validation
config.setConnectionTestQuery("SELECT 1");
config.setValidationTimeout(5000);

HikariDataSource ds = new HikariDataSource(config);

// Monitor pool health
HikariPoolMXBean poolMXBean = ds.getHikariPoolMXBean();
if (poolMXBean != null) {
    System.out.println("Active: " + poolMXBean.getActiveConnections());
    System.out.println("Idle: " + poolMXBean.getIdleConnections());
    System.out.println("Waiting: " + poolMXBean.getThreadsAwaitingConnection());
}
```

### Fix 3: Handle transient failures with circuit breaker pattern

```java
public class ResilientDataSource {
    private final DataSource delegate;
    private int consecutiveFailures = 0;
    private long lastFailureTime = 0;
    private static final int FAILURE_THRESHOLD = 5;
    private static final long RESET_TIMEOUT_MS = 30000;

    public ResilientDataSource(DataSource delegate) {
        this.delegate = delegate;
    }

    public Connection getConnection() throws SQLException {
        if (isCircuitOpen()) {
            throw new SQLException("Circuit breaker open — database temporarily unavailable");
        }

        try {
            Connection conn = delegate.getConnection();
            consecutiveFailures = 0;  // Reset on success
            return conn;
        } catch (SQLTransientConnectionException e) {
            consecutiveFailures++;
            lastFailureTime = System.currentTimeMillis();
            if (consecutiveFailures >= FAILURE_THRESHOLD) {
                System.err.println("Circuit breaker tripped after " + consecutiveFailures + " failures");
            }
            throw e;
        }
    }

    private boolean isCircuitOpen() {
        if (consecutiveFailures < FAILURE_THRESHOLD) return false;
        return System.currentTimeMillis() - lastFailureTime < RESET_TIMEOUT_MS;
    }
}
```

### Fix 4: Validate connection before use

```java
public static Connection getValidatedConnection(DataSource ds) throws SQLException {
    Connection conn = ds.getConnection();
    try {
        if (!conn.isValid(5)) {  // 5 second validation timeout
            conn.close();
            throw new SQLException("Connection validation failed");
        }
        return conn;
    } catch (SQLException e) {
        try { conn.close(); } catch (SQLException ignored) {}
        throw e;
    }
}
```

## Prevention Checklist

- Implement retry with exponential backoff for transient connection failures.
- Configure connection pools with appropriate sizes and timeouts.
- Use connection validation (`isValid()` or validation queries) before use.
- Monitor pool metrics and set up alerts for exhaustion.
- Implement circuit breaker patterns for high-availability systems.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLNonTransientConnectionException](../sqlnontransientconnectionexception) — persistent connection failure.
- [SQLTransientException](../sqltransientexception) — parent class for transient SQL failures.
