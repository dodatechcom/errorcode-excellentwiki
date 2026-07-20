---
title: "[Solution] Java SQLRecoverableException — JDBC Retry Fix"
description: "Fix Java SQLRecoverableException by implementing retry logic, re-establishing connections, and checking connection pool health."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLRecoverableException — JDBC Retry Fix

An `SQLRecoverableException` is thrown when a database connection can be recovered. This exception indicates a transient condition — often a lost or stale connection — that may succeed if the operation is retried with a fresh connection.

## Description

`java.sql.SQLRecoverableException` extends `SQLNonTransientException` (though in practice it behaves transiently in many drivers). It typically indicates:

- Database connection was lost during a transaction
- Connection pool returned a stale connection
- Network interruption caused the connection to drop
- Database server was temporarily unavailable

Common message variants:

- `SQLRecoverableException: IO Error: Socket read timed out`
- `SQLRecoverableException: Connection reset`
- `SQLRecoverableException: Closed Connection`
- `SQLRecoverableException: No more data to read from socket`

## Common Causes

```java
// Cause 1: Stale connection from pool
DataSource ds = getDataSource();
Connection conn = ds.getConnection();  // May be stale
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users");
ps.executeQuery();  // SQLRecoverableException — connection is stale

// Cause 2: Database server restart or failover
Connection conn = dataSource.getConnection();
// DB goes down and comes back up
conn.prepareStatement("SELECT 1").executeQuery();  // SQLRecoverableException

// Cause 3: Network timeout
Connection conn = DriverManager.getConnection(url, props);
conn.setNetworkTimeout(executor, 5000);
PreparedStatement ps = conn.prepareStatement("SELECT * FROM large_table");
ps.executeQuery();  // SQLRecoverableException if network is slow

// Cause 4: Connection pool exhaustion leading to stale connections
HikariConfig config = new HikariConfig();
config.setConnectionTimeout(30000);
config.setKeepaliveTime(0);  // No keepalive — connections may go stale
HikariDataSource ds = new HikariDataSource(config);
```

## Solutions

### Fix 1: Implement retry logic with connection re-establishment

```java
public static <T> T executeWithRetry(DatabaseOperation<T> operation, int maxRetries)
        throws SQLException {
    for (int attempt = 0; attempt <= maxRetries; attempt++) {
        try (Connection conn = dataSource.getConnection()) {
            return operation.execute(conn);
        } catch (SQLRecoverableException e) {
            if (attempt == maxRetries) {
                throw e;
            }
            System.err.println("Recoverable error, retrying (attempt " + (attempt + 1) + ")");
            Thread.sleep(1000L * (attempt + 1));
        }
    }
    throw new SQLException("Max retries exceeded");
}

@FunctionalInterface
interface DatabaseOperation<T> {
    T execute(Connection conn) throws SQLException;
}
```

### Fix 2: Validate connection before use

```java
public static Connection getValidConnection(DataSource ds) throws SQLException {
    Connection conn = ds.getConnection();
    try {
        if (!conn.isValid(5)) {  // 5 second timeout
            conn.close();
            conn = ds.getConnection();  // Get a new connection
        }
    } catch (SQLException e) {
        conn.close();
        conn = ds.getConnection();
    }
    return conn;
}
```

### Fix 3: Configure connection pool to detect stale connections

```java
// HikariCP configuration
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
config.setUsername("user");
config.setPassword("pass");

config.setConnectionTimeout(30000);     // Max wait for connection
config.setValidationTimeout(5000);      // Max wait for validation
config.setKeepaliveTime(30000);         // Keepalive every 30 seconds
config.setMaxLifetime(1800000);         // Max connection lifetime: 30 min
config.setLeakDetectionThreshold(60000); // Detect leaked connections

HikariDataSource ds = new HikariDataSource(config);
```

### Fix 4: Use try-with-resources and auto-retry for transient failures

```java
public static void executeWithAutoRetry(Runnable operation, int maxRetries)
        throws SQLException {
    for (int attempt = 0; attempt <= maxRetries; attempt++) {
        try {
            operation.run();
            return;
        } catch (SQLRecoverableException e) {
            if (attempt == maxRetries) throw e;
            Thread.sleep(1000L * (attempt + 1));
        }
    }
}
```

## Prevention Checklist

- Configure connection pools with keepalive and validation settings.
- Use `connection.isValid()` before long-running operations.
- Implement retry logic with exponential backoff for recoverable errors.
- Set appropriate connection timeouts and max lifetime in pool configuration.
- Monitor connection pool metrics for stale connection indicators.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLTransientException](../sqltransientexception) — temporary SQL failure.
- [SQLRecoverableException](../sqlrecoverableexception) — connection can be recovered.
