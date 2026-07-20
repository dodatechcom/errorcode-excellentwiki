---
title: "[Solution] Java SQLFeatureNotSupportedException — JDBC Feature Not Supported Fix"
description: "Fix Java SQLFeatureNotSupportedException by checking driver capabilities, using alternative methods, and handling gracefully with fallback."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 423
---

# SQLFeatureNotSupportedException — JDBC Feature Not Supported Fix

A `SQLFeatureNotSupportedException` is thrown when the JDBC driver does not support a requested feature. This indicates that the operation is valid in the JDBC specification but the specific driver has not implemented it.

## Description

`java.sql.SQLFeatureNotSupportedException` extends `SQLException` and signals that a JDBC method or feature is not supported by the driver. This is a permanent condition — retrying will not help.

Common message variants:

- `SQLFeatureNotSupportedException: Method not supported`
- `SQLFeatureNotSupportedException: Not supported by driver`
- `SQLFeatureNotSupportedException: Type scroll type X not supported`
- `SQLFeatureNotSupportedException: Update result set not supported`

## Common Causes

```java
// Cause 1: Attempting scrollable ResultSet on a driver that only supports forward-only
Statement stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
// Driver only supports TYPE_FORWARD_ONLY — throws SQLFeatureNotSupportedException

// Cause 2: Calling returnGeneratedKeys on driver that doesn't support it
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (name) VALUES (?)", Statement.RETURN_GENERATED_KEYS);
// Driver doesn't support getGeneratedKeys() — throws SQLFeatureNotSupportedException

// Cause 3: Using NLOB (java.sql.NClob) on driver that doesn't support it
PreparedStatement ps = conn.prepareStatement("INSERT INTO text_col (val) VALUES (?)");
ps.setNClob(1, new StringReader("Hello"));  // Driver lacks NLOB support

// Cause 4: Attempting updatable ResultSet on read-only driver
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
rs.moveToInsertRow();  // Driver doesn't support updatable result sets

// Cause 5: Calling unsupported methods like setQueryTimeout
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(30);  // Driver doesn't support timeouts
```

## Solutions

### Fix 1: Check driver metadata for supported features

```java
public static void checkDriverCapabilities(Connection conn) throws SQLException {
    DatabaseMetaData meta = conn.getMetaData();

    System.out.println("Driver: " + meta.getDriverName() + " " + meta.getDriverVersion());
    System.out.println("Supports transactions: " + meta.supportsTransactions());
    System.out.println("Supports scrollable: " + meta.supportsResultSetType(ResultSet.TYPE_SCROLL_INSENSITIVE));
    System.out.println("Supports updatable: " + meta.supportsResultSetConcurrency(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_UPDATABLE));
    System.out.println("Supports generated keys: " + meta.supportsGetGeneratedKeys());
    System.out.println("Supports batch updates: " + meta.supportsBatchUpdates());
}
```

### Fix 2: Use fallback methods for unsupported features

```java
public static long safeInsertWithFallback(Connection conn, String name) throws SQLException {
    try {
        // Try using RETURN_GENERATED_KEYS
        PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO users (name) VALUES (?)", Statement.RETURN_GENERATED_KEYS);
        ps.setString(1, name);
        ps.executeUpdate();

        try (ResultSet keys = ps.getGeneratedKeys()) {
            if (keys.next()) return keys.getLong(1);
        }
    } catch (SQLFeatureNotSupportedException e) {
        // Fallback: insert without returning generated key
        System.err.println("Driver doesn't support getGeneratedKeys, using fallback");
        PreparedStatement ps = conn.prepareStatement("INSERT INTO users (name) VALUES (?)");
        ps.setString(1, name);
        ps.executeUpdate();

        // Use separate query to get the key
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT LAST_INSERT_ID()");
        if (rs.next()) return rs.getLong(1);
    }
    return -1;
}
```

### Fix 3: Use only standard JDBC methods supported by the driver

```java
public static ResultSet safeQuery(Connection conn, String sql) throws SQLException {
    Statement stmt = conn.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY);
    // Avoid unsupported scroll types

    try {
        return stmt.executeQuery(sql);
    } catch (SQLFeatureNotSupportedException e) {
        // Fallback: use default statement creation
        System.err.println("Falling back to default statement");
        Statement defaultStmt = conn.createStatement();
        return defaultStmt.executeQuery(sql);
    }
}
```

### Fix 4: Implement feature detection and graceful degradation

```java
public class FeatureDetector {
    private final Connection conn;
    private final boolean supportsScrollable;
    private final boolean supportsGeneratedKeys;
    private final boolean supportsBatchUpdates;

    public FeatureDetector(Connection conn) throws SQLException {
        this.conn = conn;
        DatabaseMetaData meta = conn.getMetaData();
        this.supportsScrollable = meta.supportsResultSetType(ResultSet.TYPE_SCROLL_INSENSITIVE);
        this.supportsGeneratedKeys = meta.supportsGetGeneratedKeys();
        this.supportsBatchUpdates = meta.supportsBatchUpdates();
    }

    public boolean isScrollableSupported() { return supportsScrollable; }
    public boolean isGeneratedKeysSupported() { return supportsGeneratedKeys; }
    public boolean isBatchUpdatesSupported() { return supportsBatchUpdates; }
}

// Usage
FeatureDetector detector = new FeatureDetector(conn);
if (detector.isScrollableSupported()) {
    // Use scrollable result set
} else {
    // Collect results into a list instead
}
```

## Prevention Checklist

- Always check `DatabaseMetaData` for feature support before calling JDBC methods.
- Implement fallback paths for optional JDBC features.
- Handle `SQLFeatureNotSupportedException` with informative error messages.
- Target the least common denominator of JDBC features for broad driver compatibility.
- Document required JDBC features for your application.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLNonTransientException](../sqlnontransientexception) — permanent SQL failure.
- [AbstractMethodError](../abstractmethoderror) — method not implemented in subclass.
