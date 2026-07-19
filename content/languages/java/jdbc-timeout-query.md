---
title: "[Solution] JDBC Query Timeout Expired"
description: "Fix java.sql.SQLException Query timeout expired. Configure and handle JDBC query execution timeouts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Query Timeout Expired

A `SQLException` with message `Query timeout expired` is thrown when a JDBC statement exceeds the configured query timeout limit. The database driver interrupts the query and raises this exception.

## What This Error Means

Each JDBC statement can have a timeout (in seconds) that limits how long the database can execute it. If the query takes longer than the specified timeout, the driver cancels it and throws this exception. This is a safety mechanism to prevent runaway queries from consuming database resources indefinitely.

## Common Causes

```java
// Cause 1: Query timeout set too low for complex queries
PreparedStatement ps = conn.prepareStatement("SELECT * FROM large_table t1 JOIN huge_table t2 ON ...");
ps.setQueryTimeout(2);  // 2 seconds — too short for complex join
ps.executeQuery();       // QueryTimeoutException

// Cause 2: Missing database indexes causing slow queries
PreparedStatement ps = conn.prepareStatement(
    "SELECT * FROM orders WHERE customer_name LIKE '%John%'");
ps.setQueryTimeout(30);
ps.executeQuery();  // Full table scan exceeds 30 seconds

// Cause 3: Database under heavy load
// Normal query exceeds timeout due to resource contention
```

## How to Fix

### Fix 1: Increase query timeout for complex operations

```java
PreparedStatement ps = conn.prepareStatement(complexQuery);
ps.setQueryTimeout(120);  // 2 minutes for reporting queries
ResultSet rs = ps.executeQuery();
```

### Fix 2: Optimize the query with proper indexes

```java
// Before: slow full table scan
PreparedStatement ps = conn.prepareStatement(
    "SELECT * FROM orders WHERE customer_id = ? AND order_date > ?");

// Add database index:
// CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date);

// After: query uses index, runs in milliseconds
```

### Fix 3: Handle timeout gracefully with retry logic

```java
public List<Order> queryWithRetry(String sql, Object... params) {
    int retries = 3;
    for (int attempt = 1; attempt <= retries; attempt++) {
        try (Connection conn = dataSource.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setQueryTimeout(30);
            for (int i = 0; i < params.length; i++) {
                ps.setObject(i + 1, params[i]);
            }
            try (ResultSet rs = ps.executeQuery()) {
                return mapResults(rs);
            }
        } catch (SQLException e) {
            if (e.getMessage().contains("timeout") && attempt < retries) {
                log.warn("Query timeout on attempt {}, retrying...", attempt);
                continue;
            }
            throw new DataAccessException("Query failed after " + retries + " attempts", e);
        }
    }
    throw new IllegalStateException("Unreachable");
}
```

### Fix 4: Set global query timeout at connection pool level

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:postgresql://localhost:5432/mydb");
config.setConnectionTimeout(30000);  // Time to get connection from pool
// Query timeout is per-statement, set via:
// Statement.setQueryTimeout() or Spring's JdbcTemplate.setQueryTimeout()
```

### Fix 5: Use streaming for large result sets

```java
Statement stmt = conn.createStatement();
stmt.setFetchSize(1000);  // Fetch in batches
stmt.setQueryTimeout(300);
ResultSet rs = stmt.executeQuery("SELECT * FROM large_table");
while (rs.next()) {
    processRow(rs);
    // Processing is streaming, avoids loading entire result into memory
}
```

## Prevention Tips

- Set appropriate query timeouts for different types of operations (OLTP vs reporting).
- Always index columns used in WHERE, JOIN, and ORDER BY clauses.
- Monitor slow query logs in the database.
- Use query timeout as a safety net, not a performance solution.

## Related Errors

- {{< relref "jdbc-conn" >}} — Connection errors
- {{< relref "connection-timeout" >}} — Connection timeout
- {{< relref "jdbc-batch-update" >}} — Batch update errors
