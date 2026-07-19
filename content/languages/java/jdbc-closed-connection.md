---
title: "[Solution] JDBC Connection Has Already Been Closed"
description: "Fix java.sql.SQLException Connection has already been closed. Prevent and handle using closed JDBC connections."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Connection Has Already Been Closed

A `SQLException` with message `Connection has already been closed` occurs when code attempts to use a JDBC connection that has already been explicitly closed or has been closed by the connection pool.

## What This Error Means

Once a `Connection.close()` is called, the connection becomes unusable. Any subsequent attempt to create statements, execute queries, or set properties on it will throw this exception. Connection pools may also reclaim and close idle connections, causing this error in long-running operations.

## Common Causes

```java
// Cause 1: Closing connection then trying to reuse it
Connection conn = dataSource.getConnection();
conn.close();
PreparedStatement ps = conn.prepareStatement("SELECT 1");  // SQLException!

// Cause 2: Connection closed by pool while in use (timeout)
Connection conn = dataSource.getConnection();
// Long processing...
Thread.sleep(120_000);  // Pool closes idle connection after 60s
conn.prepareStatement("SELECT 1").executeQuery();  // Connection closed

// Cause 3: Using connection after try-with-resources block
try (Connection conn = dataSource.getConnection()) {
    // Use connection
}
PreparedStatement ps = conn.prepareStatement("SELECT 1");  // Closed!
```

## How to Fix

### Fix 1: Check connection state before use

```java
public void executeQuerySafely(Connection conn, String sql) throws SQLException {
    if (conn == null || conn.isClosed()) {
        conn = dataSource.getConnection();  // Get a fresh connection
    }
    try (PreparedStatement ps = conn.prepareStatement(sql)) {
        ResultSet rs = ps.executeQuery();
        // Process results
    }
}
```

### Fix 2: Use connection pool validation

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setConnectionTimeout(30000);
config.setValidationTimeout(5000);
config.setMaxLifetime(1800000);  // Close connection before DB timeout
config.setKeepaliveTime(30000);  // Send keepalive ping every 30s
```

### Fix 3: Avoid sharing connections across threads

```java
// Bad: sharing connection across threads
Connection conn = dataSource.getConnection();
ExecutorService pool = Executors.newFixedThreadPool(10);
pool.submit(() -> {
    conn.prepareStatement("SELECT * FROM orders").executeQuery();  // Race condition!
});

// Good: each thread gets its own connection
ExecutorService pool = Executors.newFixedThreadPool(10);
pool.submit(() -> {
    try (Connection c = dataSource.getConnection()) {
        c.prepareStatement("SELECT * FROM orders").executeQuery();
    }
});
```

### Fix 4: Handle gracefully in service layers

```java
public List<User> retryOnClosedConnection(String sql) {
    int maxRetries = 3;
    for (int i = 0; i < maxRetries; i++) {
        try (Connection conn = dataSource.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ResultSet rs = ps.executeQuery();
            return mapResults(rs);
        } catch (SQLException e) {
            if (i == maxRetries - 1) throw new DataAccessException("Failed after retries", e);
        }
    }
    throw new IllegalStateException("Unreachable code");
}
```

## Prevention Tips

- Never close a connection you do not own (pool connections).
- Use try-with-resources to ensure proper cleanup.
- Configure pool `maxLifetime` shorter than the database's `wait_timeout`.
- Do not share connections across threads; obtain a new connection per thread.

## Related Errors

- {{< relref "jdbc-conn" >}} — Cannot establish JDBC connection
- {{< relref "jdbc-closed-connection" >}} — Connection already closed
- {{< relref "connection-timeout" >}} — Connection timeout
