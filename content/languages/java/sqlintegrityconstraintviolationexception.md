---
title: "[Solution] Java SQLIntegrityConstraintViolationException — SQL Constraint Fix"
description: "Fix Java SQLIntegrityConstraintViolationException by checking constraints, validating references, and handling duplicates properly."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLIntegrityConstraintViolationException — SQL Constraint Fix

An `SQLIntegrityConstraintViolationException` is thrown when a SQL integrity constraint is violated. This includes foreign key violations, unique constraint violations, NOT NULL violations, and CHECK constraint failures.

## Description

`java.sql.SQLIntegrityConstraintViolationException` extends `SQLIntegrityConstraintViolationException` (which extends `SQLNonTransientException`). It indicates a permanent constraint violation that will not resolve without changing the data or schema.

Common constraint types that trigger this exception:

- **UNIQUE constraint** — duplicate key value
- **FOREIGN KEY constraint** — reference to non-existent parent row
- **NOT NULL constraint** — null value in a required column
- **CHECK constraint** — value fails check expression

Common message variants:

- `Duplicate entry 'X' for key 'PRIMARY'`
- `Cannot add or update a child row: a foreign key constraint fails`
- `Column 'X' cannot be null`
- `Check constraint 'X' is violated`
- `Duplicate key on index 'X'`

## Common Causes

```java
// Cause 1: Duplicate primary key
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, 1);  // Already exists
ps.setString(2, "Alice");
ps.executeUpdate();  // SQLIntegrityConstraintViolationException: Duplicate entry

// Cause 2: Foreign key violation — referencing non-existent parent
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO orders (user_id, product) VALUES (?, ?)");
ps.setInt(1, 9999);  // No user with id 9999
ps.setString(2, "Widget");
ps.executeUpdate();  // SQLIntegrityConstraintViolationException: FK fails

// Cause 3: NOT NULL constraint violation
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (name) VALUES (?)");
ps.setString(1, null);  // Column has NOT NULL constraint
ps.executeUpdate();  // SQLIntegrityConstraintViolationException: Column 'name' cannot be null

// Cause 4: CHECK constraint violation
PreparedStatement ps = conn.prepareStatement("INSERT INTO products (price) VALUES (?)");
ps.setDouble(1, -10.0);  // CHECK (price > 0)
ps.executeUpdate();  // SQLIntegrityConstraintViolationException: Check constraint
```

## Solutions

### Fix 1: Check for existence before inserting

```java
public static void insertUser(Connection conn, int id, String name) throws SQLException {
    // Check if user already exists
    try (PreparedStatement check = conn.prepareStatement(
            "SELECT COUNT(*) FROM users WHERE id = ?")) {
        check.setInt(1, id);
        try (ResultSet rs = check.executeQuery()) {
            if (rs.next() && rs.getInt(1) > 0) {
                throw new IllegalArgumentException("User with id " + id + " already exists");
            }
        }
    }

    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO users (id, name) VALUES (?, ?)")) {
        ps.setInt(1, id);
        ps.setString(2, name);
        ps.executeUpdate();
    }
}
```

### Fix 2: Use INSERT ... ON DUPLICATE KEY (database-specific)

```java
// MySQL
String sql = "INSERT INTO users (id, name) VALUES (?, ?) ON DUPLICATE KEY UPDATE name = ?";
PreparedStatement ps = conn.prepareStatement(sql);
ps.setInt(1, 1);
ps.setString(2, "Alice");
ps.setString(3, "Alice");
ps.executeUpdate();

// PostgreSQL — use INSERT ... ON CONFLICT
String sql = "INSERT INTO users (id, name) VALUES (?, ?) ON CONFLICT (id) DO UPDATE SET name = ?";
```

### Fix 3: Handle foreign key references

```java
public static void insertOrder(Connection conn, int userId, String product) throws SQLException {
    // Verify parent exists
    try (PreparedStatement check = conn.prepareStatement(
            "SELECT id FROM users WHERE id = ?")) {
        check.setInt(1, userId);
        try (ResultSet rs = check.executeQuery()) {
            if (!rs.next()) {
                throw new IllegalArgumentException("User " + userId + " does not exist");
            }
        }
    }

    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO orders (user_id, product) VALUES (?, ?)")) {
        ps.setInt(1, userId);
        ps.setString(2, product);
        ps.executeUpdate();
    }
}
```

### Fix 4: Handle NOT NULL and CHECK constraints with validation

```java
public static void insertProduct(Connection conn, String name, double price) throws SQLException {
    if (name == null) {
        throw new IllegalArgumentException("Product name cannot be null");
    }
    if (price <= 0) {
        throw new IllegalArgumentException("Product price must be positive");
    }

    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO products (name, price) VALUES (?, ?)")) {
        ps.setString(1, name);
        ps.setDouble(2, price);
        ps.executeUpdate();
    }
}
```

## Prevention Checklist

- Always validate data before inserting to prevent constraint violations.
- Use `INSERT ... ON CONFLICT` / `ON DUPLICATE KEY UPDATE` for upsert patterns.
- Verify foreign key references exist before inserting child rows.
- Enforce NOT NULL and CHECK constraints at both application and database levels.
- Handle `SQLIntegrityConstraintViolationException` with user-friendly error messages.

## Related Errors

- [SQLDataException](../sqldataexception) — general data access error.
- [BatchUpdateException](../batchupdateexception) — constraint violation in batch operation.
- [SQLSyntaxErrorException](../sqlsyntaxerrorsexception) — SQL syntax error.
