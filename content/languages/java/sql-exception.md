---
title: "[Solution] Java SQLException: Table Not Found / Connection Refused Fix"
description: "Fix Java SQLException: table not found, connection refused, and other database errors. Verify table names, check connection pools, and handle DB exceptions properly."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["sqlexception", "table-not-found", "connection-refused", "jdbc", "database"]
weight: 5
---

# SQLException: Table Not Found / Connection Refused

A `java.sql.SQLException` is a checked exception that provides information about database access errors. Common variants include "table not found," "connection refused," "connection reset," and "communication link failure." These errors indicate problems at the database layer rather than application logic.

## Description

`SQLException` is the parent exception for all JDBC database errors. It contains a SQL state code, vendor-specific error code, and a descriptive message. The SQL state follows the XOPEN/SQL:1999 standard and helps identify the category of error.

Common variants:

- `SQLException: Table 'dbname.tablename' doesn't exist`
- `SQLException: Connection refused: connect`
- `SQLException: Communication link failure`
- `SQLException: No suitable driver`
- `SQLException: Connection has already been closed`

## Common Causes

```java
// Cause 1: Table doesn't exist
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM nonexistent_table");
// SQLException: Table 'db.nonexistent_table' doesn't exist

// Cause 2: Database server is not running
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/mydb", "user", "pass"
);  // SQLException: Connection refused

// Cause 3: Connection pool exhausted
HikariConfig config = new HikariConfig();
config.setMaximumPoolSize(5);
HikariDataSource ds = new HikariDataSource(config);
// All connections in use — next call blocks or times out

// Cause 4: Wrong database name
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/wrong_db_name", "user", "pass"
);  // SQLException: Unknown database

// Cause 5: Connection timeout
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://remote-server:3306/mydb?connectTimeout=5000", "user", "pass"
);  // SQLException: Connection timed out
```

## How to Fix

### Fix 1: Verify table existence before querying

```java
// Wrong
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");

// Correct — check if table exists first
DatabaseMetaData meta = connection.getMetaData();
ResultSet tables = meta.getTables(null, null, "users", new String[]{"TABLE"});
if (tables.next()) {
    // Table exists, query it
    ResultSet rs = stmt.executeQuery("SELECT * FROM users");
} else {
    System.err.println("Table 'users' does not exist");
}
```

### Fix 2: Use connection pool with proper timeout settings

```java
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/mydb");
config.setUsername("user");
config.setPassword("pass");
config.setMaximumPoolSize(10);
config.setConnectionTimeout(5000);   // 5s to get a connection
config.setValidationTimeout(3000);   // 3s for validation
config.setIdleTimeout(600000);       // 10min idle timeout
config.setKeepaliveTime(300000);     // 5min keepalive

HikariDataSource ds = new HikariDataSource(config);
```

### Fix 3: Handle connection failures gracefully

```java
public Connection getConnection() {
    int retries = 3;
    for (int i = 1; i <= retries; i++) {
        try {
            Connection conn = dataSource.getConnection();
            if (conn.isValid(3)) {
                return conn;
            }
            conn.close();
        } catch (SQLException e) {
            System.err.println("Connection attempt " + i + " failed: " + e.getMessage());
            if (i == retries) {
                throw new RuntimeException("Cannot connect to database after " + retries + " attempts", e);
            }
            try {
                Thread.sleep(1000 * i);  // Exponential backoff
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
    throw new RuntimeException("Cannot obtain database connection");
}
```

### Fix 4: Handle SQL exceptions with proper error codes

```java
try {
    Statement stmt = connection.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT * FROM users");
} catch (SQLException e) {
    String sqlState = e.getSQLState();
    int errorCode = e.getErrorCode();

    if ("42S02".equals(sqlState)) {
        // Table or view not found
        System.err.println("Table does not exist: " + e.getMessage());
    } else if ("08S01".equals(sqlState)) {
        // Communication link failure
        System.err.println("Database connection lost: " + e.getMessage());
    } else {
        System.err.println("SQL error [" + sqlState + "]: " + e.getMessage());
    }
}
```

### Fix 5: Use PreparedStatement to avoid SQL injection and syntax errors

```java
// Wrong — string concatenation
String table = userInput;
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM " + table);  // SQL injection risk

// Correct — use PreparedStatement
PreparedStatement stmt = connection.prepareStatement("SELECT * FROM users WHERE id = ?");
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();
```

## Examples

This error commonly occurs when:

- Database migration scripts haven't been run yet
- Application connects to wrong database schema
- Connection pool is misconfigured and exhausted
- Database server is restarted while application is running

## Related Errors

- [Connection refused](connection-timeout) — TCP-level connection failure
- [ClassNotFoundException](#) — JDBC driver not on classpath
- [SQLTransientConnectionException](#) — connection pool timeout
