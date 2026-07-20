---
title: "[Solution] Java SQLTimeoutException — Query Timeout Expired Fix"
description: "Fix Java SQLTimeoutException by increasing timeout, optimizing queries, using connection pooling, and handling timeout in application."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 426
---

# SQLTimeoutException — Query Timeout Expired Fix

An `SQLTimeoutException` is thrown when a query or login timeout expires before the database operation completes. This is a specific type of `SQLTransientException` that indicates the operation took too long.

## Description

`java.sql.SQLTimeoutException` extends `SQLTransientException` and indicates that the statement or connection timeout has been exceeded. The operation may succeed if retried with a longer timeout or after optimizing the underlying query.

Common message variants:

- `SQLTimeoutException: Query timed out`
- `SQLTimeoutException: Connection has been cancelled`
- `SQLTimeoutException: Statement cancelled due to timeout`
- `SQLTimeoutException: Login timeout expired`

## Common Causes

```java
// Cause 1: Query timeout too short for a complex query
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(2);  // 2 second timeout
ResultSet rs = stmt.executeQuery("SELECT * FROM huge_table JOIN other_table ON ...");  // SQLTimeoutException

// Cause 2: Lock wait causing query to exceed timeout
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(10);
stmt.executeQuery("UPDATE accounts SET balance = balance + 100 WHERE id = 1");
// Another transaction holds a lock — SQLTimeoutException

// Cause 3: Connection login timeout too short
Properties props = new Properties();
props.setProperty("connectTimeout", "1000");  // 1 second login timeout
Connection conn = DriverManager.getConnection("jdbc:mysql://remote-host:3306/mydb", props);
// Network latency causes SQLTimeoutException

// Cause 4: Slow query with full table scan
PreparedStatement ps = conn.prepareStatement("SELECT * FROM orders WHERE created_date > ?");
ps.setQueryTimeout(5);
ps.setDate(1, Date.valueOf("2020-01-01"));
ResultSet rs = ps.executeQuery();  // No index on created_date — SQLTimeoutException

// Cause 5: Large result set transfer timeout
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(30);
ResultSet rs = stmt.executeQuery("SELECT * FROM logs");  // Millions of rows — timeout
```

## Solutions

### Fix 1: Optimize queries before increasing timeout

```java
// Before: Slow query without index
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(5);
ResultSet rs = stmt.executeQuery(
    "SELECT * FROM orders WHERE customer_id = 123 AND status = 'active'");

// After: Add appropriate indexes and use EXPLAIN to verify
// CREATE INDEX idx_orders_customer_status ON orders(customer_id, status);
PreparedStatement ps = conn.prepareStatement(
    "SELECT id, status, total FROM orders WHERE customer_id = ? AND status = ?");
ps.setInt(1, 123);
ps.setString(2, "active");
ps.setQueryTimeout(5);  // Now this should complete within timeout
ResultSet rs = ps.executeQuery();
```

### Fix 2: Increase timeout for known long-running operations

```java
// For batch/reporting operations with known long execution times
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(300);  // 5 minutes for complex reports
ResultSet rs = stmt.executeQuery(
    "SELECT customer_id, SUM(total) FROM orders GROUP BY customer_id");
processReport(rs);
```

### Fix 3: Handle timeout in application with cancellation support

```java
public class QueryExecutor {
    private final ExecutorService executor = Executors.newSingleThreadExecutor();

    public <T> T executeWithTimeout(Connection conn, String sql, long timeoutSeconds,
                                     QueryHandler<T> handler) throws SQLException, TimeoutException {
        Future<T> future = executor.submit(() -> {
            try (Statement stmt = conn.createStatement();
                 ResultSet rs = stmt.executeQuery(sql)) {
                return handler.process(rs);
            }
        });

        try {
            return future.get(timeoutSeconds, TimeUnit.SECONDS);
        } catch (TimeoutException e) {
            future.cancel(true);
            throw new TimeoutException("Query exceeded " + timeoutSeconds + " seconds");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new SQLException("Query interrupted", e);
        } catch (ExecutionException e) {
            if (e.getCause() instanceof SQLException) {
                throw (SQLException) e.getCause();
            }
            throw new SQLException("Query failed", e.getCause());
        }
    }

    @FunctionalInterface
    interface QueryHandler<T> {
        T process(ResultSet rs) throws SQLException;
    }
}
```

### Fix 4: Use connection pooling with query timeout support

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
config.setConnectionTimeout(30000);  // 30 seconds to get connection from pool
config.setValidationTimeout(5000);   // 5 seconds for connection validation

HikariDataSource ds = new HikariDataSource(config);

try (Connection conn = ds.getConnection();
     Statement stmt = conn.createStatement()) {
    stmt.setQueryTimeout(60);  // 60 seconds for query
    ResultSet rs = stmt.executeQuery("SELECT * FROM large_table");
    processResults(rs);
} catch (SQLTimeoutException e) {
    System.err.println("Query timed out — consider optimizing or increasing timeout");
}
```

## Prevention Checklist

- Always set query timeouts appropriate for the operation type.
- Optimize slow queries using EXPLAIN plans and proper indexing.
- Monitor query execution times in production.
- Use connection pooling with proper timeout configuration.
- Implement query cancellation for long-running operations.

## Related Errors

- [SQLTransientException](../sqltransientexception) — parent class for transient SQL failures.
- [SQLTransientConnectionException](../sqltransientconnectionexception) — temporary connection failure.
- [SQLTransactionRollbackException](../sqltransactionrollbackexception) — transaction was rolled back.
