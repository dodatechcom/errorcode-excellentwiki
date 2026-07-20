---
title: "[Solution] Java SQLDataException — SQL Data Access Fix"
description: "Fix Java SQLDataException by validating input data, checking data types, handling constraints, and using proper JDBC type mappings."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLDataException — SQL Data Access Fix

An `SQLDataException` is thrown when a data access error occurs during a SQL operation. This is a general-purpose SQL exception indicating problems with data values, types, or constraints during database interactions.

## Description

`java.sql.SQLDataException` extends `SQLNonTransientException` (in most JDBC drivers) and indicates an error related to data that is unlikely to resolve without changing the data or SQL statement.

Common message variants:

- `java.sql.SQLDataException: Data truncation`
- `SQLDataException: Invalid column type`
- `SQLDataException: Out of range value for column`
- `SQLDataException: Cannot convert value`
- `SQLDataException: Data too long for column`

This exception is part of the JDBC 4.0 exception hierarchy, introduced for more granular SQL error classification.

## Common Causes

```java
// Cause 1: Data truncation — value too long for column
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (name) VALUES (?)");
ps.setString(1, "A".repeat(500));  // Column is VARCHAR(255)
ps.executeUpdate();  // SQLDataException: Data truncation

// Cause 2: Invalid data type conversion
PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setString(1, "not_a_number");  // Column is INTEGER
ps.executeQuery();  // SQLDataException: conversion error

// Cause 3: Out of range numeric value
PreparedStatement ps = conn.prepareStatement("INSERT INTO scores (value) VALUES (?)");
ps.setInt(1, 150);  // Column CHECK constraint: value BETWEEN 0 AND 100
ps.executeUpdate();  // SQLDataException: Out of range

// Cause 4: Invalid date/time format
PreparedStatement ps = conn.prepareStatement("INSERT INTO events (event_date) VALUES (?)");
ps.setString(1, "not-a-date");  // Column is DATE
ps.executeUpdate();  // SQLDataException: conversion failed
```

## Solutions

### Fix 1: Validate input data before database operations

```java
public static void insertUser(Connection conn, String name, int age) throws SQLException {
    if (name == null || name.isEmpty()) {
        throw new IllegalArgumentException("Name cannot be null or empty");
    }
    if (name.length() > 255) {
        throw new IllegalArgumentException("Name exceeds 255 characters");
    }
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException("Age must be between 0 and 150");
    }

    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO users (name, age) VALUES (?, ?)")) {
        ps.setString(1, name);
        ps.setInt(2, age);
        ps.executeUpdate();
    }
}
```

### Fix 2: Use correct JDBC type mappings

```java
// Wrong — string for numeric column
ps.setString(1, "42");

// Correct — use proper setter
ps.setInt(1, 42);

// Wrong — string for date column
ps.setString(1, "2024-01-15");

// Correct — use proper setter
ps.setDate(1, Date.valueOf("2024-01-15"));

// For timestamps
ps.setTimestamp(1, Timestamp.from(Instant.now()));
```

### Fix 3: Handle data truncation by checking constraints

```java
public static void safeInsert(Connection conn, String data) throws SQLException {
    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO logs (message) VALUES (?)")) {
        String truncated = data.length() > 1000 ? data.substring(0, 1000) : data;
        ps.setString(1, truncated);
        ps.executeUpdate();
    } catch (SQLDataException e) {
        if (e.getMessage().contains("truncat")) {
            System.err.println("Data too long, truncating further");
            // Handle truncation
        }
        throw e;
    }
}
```

### Fix 4: Use parameterized queries with type safety

```java
// Use TypedQuery or proper parameter binding
public static User findUserById(Connection conn, int id) throws SQLException {
    try (PreparedStatement ps = conn.prepareStatement(
            "SELECT id, name, age FROM users WHERE id = ?")) {
        ps.setInt(1, id);  // Type-safe binding
        try (ResultSet rs = ps.executeQuery()) {
            if (rs.next()) {
                return new User(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getInt("age")
                );
            }
        }
    }
    return null;
}
```

## Prevention Checklist

- Validate all input data types and lengths before executing SQL.
- Use `PreparedStatement` with proper setter methods (`setInt`, `setString`, etc.).
- Check database schema constraints (column types, lengths, ranges) in application code.
- Use `VARCHAR(n)`, `CHECK`, and `NOT NULL` constraints to enforce data rules at the database level.
- Handle `SQLDataException` with specific error message checks for targeted recovery.

## Related Errors

- [SQLException](../sql-exception) — parent class for SQL failures.
- [SQLIntegrityConstraintViolationException](../sqlintegrityconstraintviolationexception) — constraint violations.
- [SQLSyntaxErrorException](../sqlsyntaxerrorsexception) — SQL syntax errors.
- [BatchUpdateException](../batchupdateexception) — batch update failure.
