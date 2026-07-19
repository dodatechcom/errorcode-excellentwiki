---
title: "[Solution] JDBC ResultSet Is Closed — Accessing Closed ResultSet"
description: "Fix java.sql.SQLException ResultSet is closed. Handle ResultSet lifecycle properly in JDBC code."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ResultSet Is Closed — Accessing Closed ResultSet

A `SQLException` with message `ResultSet is closed` occurs when code attempts to read data from a `ResultSet` that has already been closed, typically because its parent `Statement` or `Connection` was closed.

## What This Error Means

A `ResultSet` is associated with the `Statement` that created it. When the statement is closed, all its result sets are closed automatically. Similarly, closing a connection closes all statements and result sets. Attempting to iterate or read from a closed result set throws this exception.

## Common Causes

```java
// Cause 1: Closing statement before reading result set
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
stmt.close();           // Closes ResultSet too!
rs.next();              // SQLException: ResultSet is closed

// Cause 2: Processing result set after connection close
ResultSet rs;
try (Connection conn = dataSource.getConnection();
     Statement stmt = conn.createStatement()) {
    rs = stmt.executeQuery("SELECT * FROM users");
}  // Connection closed, ResultSet closed
rs.next();  // SQLException

// Cause 3: Multiple next() calls across method boundaries
public ResultSet getUser(Connection conn) throws SQLException {
    Statement stmt = conn.createStatement();
    return stmt.executeQuery("SELECT * FROM users");
    // stmt is garbage collected, ResultSet may become invalid
}
```

## How to Fix

### Fix 1: Process result set before closing statement

```java
List<User> users = new ArrayList<>();
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users")) {
    ResultSet rs = ps.executeQuery();
    while (rs.next()) {
        users.add(new User(rs.getLong("id"), rs.getString("name")));
    }
}  // Auto-closes in reverse order: rs, ps, conn
```

### Fix 2: Extract data before closing resources

```java
public List<Order> fetchOrders(long userId) {
    String sql = "SELECT id, product, amount FROM orders WHERE user_id = ?";
    try (Connection conn = dataSource.getConnection();
         PreparedStatement ps = conn.prepareStatement(sql)) {
        ps.setLong(1, userId);
        try (ResultSet rs = ps.executeQuery()) {
            List<Order> orders = new ArrayList<>();
            while (rs.next()) {
                orders.add(mapOrder(rs));
            }
            return orders;  // Data extracted, resources safe to close
        }
    } catch (SQLException e) {
        throw new DataAccessException("Failed to fetch orders", e);
    }
}
```

### Fix 3: Avoid returning result sets from methods

```java
// Bad: returns ResultSet that depends on open connection
public ResultSet query(Connection conn, String sql) throws SQLException {
    return conn.createStatement().executeQuery(sql);
}

// Good: return extracted data
public List<Map<String, Object>> query(Connection conn, String sql) throws SQLException {
    List<Map<String, Object>> results = new ArrayList<>();
    try (Statement stmt = conn.createStatement();
         ResultSet rs = stmt.executeQuery(sql)) {
        ResultSetMetaData meta = rs.getMetaData();
        int cols = meta.getColumnCount();
        while (rs.next()) {
            Map<String, Object> row = new LinkedHashMap<>();
            for (int i = 1; i <= cols; i++) {
                row.put(meta.getColumnLabel(i), rs.getObject(i));
            }
            results.add(row);
        }
    }
    return results;
}
```

### Fix 4: Use RowMapper to extract data immediately

```java
List<User> users = jdbcTemplate.query(
    "SELECT * FROM users WHERE active = ?",
    (rs, rowNum) -> new User(rs.getLong("id"), rs.getString("name")),
    true
);
```

## Prevention Tips

- Always use try-with-resources for `ResultSet`, `Statement`, and `Connection`.
- Extract data from result sets into POJOs or DTOs before closing resources.
- Never store `ResultSet` references in fields or return them from methods.

## Related Errors

- {{< relref "jdbc-statement-closed" >}} — Statement closed error
- {{< relref "jdbc-closed-connection" >}} — Connection already closed
- {{< relref "jdbc-meta-data" >}} — ResultSetMetaData not available
