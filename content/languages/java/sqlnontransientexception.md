---
title: "[Solution] Java SQLNonTransientException — Permanent SQL Failure Fix"
description: "Fix Java SQLNonTransientException by fixing root cause, checking SQL syntax, verifying data types, and handling permanent errors."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 429
---

# SQLNonTransientException — Permanent SQL Failure Fix

An `SQLNonTransientException` is thrown when a SQL operation fails and retrying without fixing the underlying cause will not help. The problem is permanent and requires code or configuration changes.

## Description

`java.sql.SQLNonTransientException` extends `SQLException` and signals a non-recoverable SQL failure. Unlike `SQLTransientException`, this exception indicates a problem that will persist across retries. Common subclasses include:

- `SQLDataException` — invalid data or data conversion error
- `SQLIntegrityConstraintViolationException` — constraint violation
- `SQLSyntaxErrorException` — SQL syntax error
- `SQLFeatureNotSupportedException` — unsupported JDBC feature

Common message variants:

- `SQLNonTransientException: Column 'X' cannot be null`
- `SQLNonTransientException: Unknown column 'X' in field list`
- `SQLNonTransientException: Data truncation`
- `SQLNonTransientException: Duplicate entry for key`

## Common Causes

```java
// Cause 1: SQL syntax error
Statement stmt = conn.createStatement();
stmt.executeQuery("SELECT * FORM users");  // Typo: FORM instead of FROM
// SQLNonTransientException: SQL syntax error

// Cause 2: Inserting null into NOT NULL column
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, 1);
ps.setNull(2, Types.VARCHAR);  // name column is NOT NULL
ps.executeUpdate();
// SQLNonTransientException: Column 'name' cannot be null

// Cause 3: Wrong data type for column
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (age) VALUES (?)");
ps.setString(1, "not a number");  // age is INTEGER
ps.executeUpdate();
// SQLNonTransientException: Data type mismatch

// Cause 4: Referencing non-existent table or column
Statement stmt = conn.createStatement();
stmt.executeQuery("SELECT col FROM nonexistent_table");
// SQLNonTransientException: Table 'nonexistent_table' doesn't exist

// Cause 5: Unique constraint violation
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, 1);  // id=1 already exists
ps.setString(2, "Alice");
ps.executeUpdate();
// SQLNonTransientException: Duplicate entry for key
```

## Solutions

### Fix 1: Validate SQL syntax before execution

```java
public class SqlValidator {
    public static boolean isValidSyntax(String sql) {
        if (sql == null || sql.trim().isEmpty()) return false;

        String upper = sql.trim().toUpperCase();
        String[] validStarts = {"SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER"};
        for (String start : validStarts) {
            if (upper.startsWith(start)) return true;
        }
        return false;
    }

    public static void executeSafe(Statement stmt, String sql) throws SQLException {
        if (!isValidSyntax(sql)) {
            throw new IllegalArgumentException("Invalid SQL syntax: " + sql);
        }
        stmt.execute(sql);
    }
}
```

### Fix 2: Handle permanent errors with informative messages

```java
public static void safeInsert(Connection conn, int id, String name) throws SQLException {
    try {
        PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
        ps.setInt(1, id);
        ps.setString(2, name);
        ps.executeUpdate();
    } catch (SQLNonTransientException e) {
        if (e.getMessage().contains("Duplicate entry")) {
            throw new IllegalArgumentException("User with id " + id + " already exists", e);
        } else if (e.getMessage().contains("cannot be null")) {
            throw new IllegalArgumentException("Required field is null", e);
        } else if (e.getMessage().contains("Data truncation")) {
            throw new IllegalArgumentException("Data too long for column", e);
        }
        throw e;
    }
}
```

### Fix 3: Use database metadata to verify schema compatibility

```java
public static void verifyTableSchema(Connection conn, String tableName, Map<String, String> expectedColumns)
        throws SQLException {
    DatabaseMetaData meta = conn.getMetaData();

    for (Map.Entry<String, String> entry : expectedColumns.entrySet()) {
        try (ResultSet rs = meta.getColumns(null, null, tableName, entry.getKey())) {
            if (!rs.next()) {
                throw new IllegalStateException(
                    "Column '" + entry.getKey() + "' does not exist in table '" + tableName + "'");
            }
            String actualType = rs.getString("TYPE_NAME");
            System.out.println("Column " + entry.getKey() + ": type=" + actualType +
                " (expected " + entry.getValue() + ")");
        }
    }
}
```

### Fix 4: Build SQL with proper parameter binding to prevent type errors

```java
// Instead of string concatenation (error-prone)
String sql = "INSERT INTO users (id, name) VALUES (" + userId + ", '" + userName + "')";

// Use PreparedStatement with parameter binding
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, userId);       // Type-safe binding
ps.setString(2, userName);  // Type-safe binding
ps.executeUpdate();
```

## Prevention Checklist

- Always use PreparedStatement with parameter binding instead of string concatenation.
- Validate SQL syntax before executing dynamically constructed queries.
- Verify table and column existence at application startup.
- Handle `SQLNonTransientException` with specific, actionable error messages.
- Test SQL queries against a staging database before deployment.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLTransientException](../sqltransientexception) — temporary SQL failure (retry may work).
- [SQLSyntaxErrorException](../sqlsyntaxerrorsexception) — SQL syntax error.
- [SQLIntegrityConstraintViolationException](../sqlintegrityconstraintviolationexception) — constraint violation.
