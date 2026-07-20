---
title: "[Solution] Java SQLWarning — Non-Fatal Database Warning Fix"
description: "Fix Java SQLWarning by checking warnings after operations, logging for debugging, using getWarnings() on Statement/Connection, and handling gracefully."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 420
---

# SQLWarning — Non-Fatal Database Warning Fix

An `SQLWarning` is a non-fatal exception indicating that a database access warning occurred. Unlike most `SQLException`s, the operation succeeded, but something unusual happened that you should be aware of.

## Description

`java.sql.SQLWarning` extends `SQLException` and represents informational warnings returned by the database driver. These are not errors — the operation completed — but the warning may indicate data truncation, deprecated feature usage, or other conditions worth investigating.

Common message variants:

- `SQLWarning: Data truncated`
- `SQLWarning: Possible data truncation in column`
- `SQLWarning: Feature not yet fully implemented`
- `SQLWarning: Connection is read-only`

Warnings are chained together. A single operation may produce multiple warnings, each linked to the next via `getNextWarning()`.

## Common Causes

```java
// Cause 1: Data truncation when inserting into a shorter column
Statement stmt = conn.createStatement();
stmt.execute("INSERT INTO short_name_col (val) VALUES ('This is a very long string that exceeds column width')");
SQLWarning warning = stmt.getWarnings();  // Data truncation warning

// Cause 2: Implicit type conversion during a query
PreparedStatement ps = conn.prepareStatement("SELECT CAST(long_value AS VARCHAR(10)) FROM big_table");
ps.execute();
SQLWarning warning = ps.getWarnings();  // Possible truncation warning

// Cause 3: Deprecated SQL syntax or feature usage
Statement stmt = conn.createStatement();
stmt.execute("SELECT * FROM users WHERE userid = 1");  // Using old-style syntax
SQLWarning warning = stmt.getWarnings();  // Syntax deprecation warning

// Cause 4: Connection property warnings (e.g., read-only set unexpectedly)
Connection conn = DriverManager.getConnection(url, props);
SQLWarning warning = conn.getWarnings();  // Connection mode warning

// Cause 5: Batch operation with partial truncation
PreparedStatement ps = conn.prepareStatement("INSERT INTO log (msg) VALUES (?)");
ps.setString(1, "A".repeat(500));
ps.executeUpdate();
SQLWarning warning = ps.getWarnings();  // Column truncation warning
```

## Solutions

### Fix 1: Check and log warnings after every database operation

```java
public static void logWarnings(SQLWarningSupplier supplier) throws SQLException {
    SQLWarning warning = supplier.getWarnings();
    while (warning != null) {
        System.err.println("SQL Warning [" + warning.getSQLState() + "]: " + warning.getMessage());
        System.err.println("  ErrorCode: " + warning.getErrorCode());
        System.err.println("  State: " + warning.getSQLState());
        warning = warning.getNextWarning();
    }
}

@FunctionalInterface
interface SQLWarningSupplier {
    SQLWarning getWarnings() throws SQLException;
}

// Usage
Statement stmt = conn.createStatement();
stmt.execute("INSERT INTO users (name) VALUES ('LongName')");
logWarnings(stmt::getWarnings);
```

### Fix 2: Retrieve warnings from Connection and Statement objects

```java
public class WarningChecker {
    public static void checkAllWarnings(Connection conn) throws SQLException {
        // Check connection-level warnings
        SQLWarning connWarning = conn.getWarnings();
        while (connWarning != null) {
            System.err.println("Connection warning: " + connWarning.getMessage());
            connWarning = connWarning.getNextWarning();
        }
        conn.clearWarnings();  // Clear after processing
    }

    public static void checkStatementWarnings(Statement stmt) throws SQLException {
        SQLWarning warning = stmt.getWarnings();
        while (warning != null) {
            System.err.println("Statement warning: " + warning.getMessage());
            System.err.println("SQL State: " + warning.getSQLState());
            warning = warning.getNextWarning();
        }
        stmt.clearWarnings();
    }
}
```

### Fix 3: Handle truncation warnings by adjusting column sizes

```java
// Check column metadata before inserting
public static void safeInsert(Connection conn, String columnValue) throws SQLException {
    try (Statement stmt = conn.createStatement();
         ResultSet rs = stmt.executeQuery("SELECT CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'users' AND COLUMN_NAME = 'name'")) {
        if (rs.next()) {
            int maxLength = rs.getInt(1);
            if (columnValue.length() > maxLength) {
                System.err.println("Warning: value exceeds column length " + maxLength + ", truncating");
                columnValue = columnValue.substring(0, maxLength);
            }
        }
    }

    try (PreparedStatement ps = conn.prepareStatement("INSERT INTO users (name) VALUES (?)")) {
        ps.setString(1, columnValue);
        ps.executeUpdate();
    }
}
```

### Fix 4: Convert SQLWarning to application-level notification

```java
public class DatabaseWarningListener {
    private final List<String> warnings = new ArrayList<>();

    public void captureWarnings(Statement stmt) throws SQLException {
        SQLWarning warning = stmt.getWarnings();
        while (warning != null) {
            warnings.add(String.format("[%s] %s (code: %d)",
                warning.getSQLState(), warning.getMessage(), warning.getErrorCode()));
            warning = warning.getNextWarning();
        }
    }

    public void reportWarnings() {
        if (!warnings.isEmpty()) {
            System.err.println("Database warnings encountered: " + warnings.size());
            warnings.forEach(w -> System.err.println("  - " + w));
            warnings.clear();
        }
    }
}
```

### Fix 5: Clear warnings to prevent stale data in connection pooling

```java
public Connection getConnectionFromPool() throws SQLException {
    Connection conn = dataSource.getConnection();
    // Clear any stale warnings from pool reuse
    conn.clearWarnings();
    return conn;
}
```

## Prevention Checklist

- Always check `getWarnings()` on `Statement` and `Connection` after critical operations.
- Clear warnings with `clearWarnings()` after processing to avoid stale data.
- Log SQL warnings for debugging even though they are non-fatal.
- Check column sizes from metadata before inserting long values.
- Clear warnings when returning connections to a pool.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [DataTruncation](../datatruncation) — specific truncation warning/error.
- [SQLDataException](../sqldataexception) — data-related SQL error.
