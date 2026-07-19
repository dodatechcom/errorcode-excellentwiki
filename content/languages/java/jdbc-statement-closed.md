---
title: "[Solution] JDBC Statement Closed — Using Statement After Close"
description: "Fix java.sql.SQLException Statement closed. Prevent and handle using closed JDBC Statement objects."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Statement Closed — Using Statement After Close

A `SQLException` with message `Statement closed` occurs when code attempts to execute a query or update using a `Statement`, `PreparedStatement`, or `CallableStatement` that has already been closed.

## What This Error Means

JDBC statements are lightweight resources bound to a connection. When a statement is closed (explicitly or via try-with-resources), any subsequent call to `executeQuery()`, `executeUpdate()`, or `execute()` on that statement will fail with this error.

## Common Causes

```java
// Cause 1: Reusing statement after try-with-resources
try (PreparedStatement ps = conn.prepareStatement("SELECT * FROM users")) {
    ResultSet rs = ps.executeQuery();
    // ...
}
ps.setInt(1, 42);  // SQLException: Statement closed

// Cause 2: Closing statement explicitly then reusing
PreparedStatement ps = conn.prepareStatement("INSERT INTO log (msg) VALUES (?)");
ps.setString(1, "hello");
ps.executeUpdate();
ps.close();
ps.setString(1, "world");  // SQLException

// Cause 3: Statement closed by parent connection closure
PreparedStatement ps = conn.prepareStatement("SELECT 1");
conn.close();             // Closes all statements
ps.executeQuery();        // SQLException
```

## How to Fix

### Fix 1: Use try-with-resources for all statements

```java
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?")) {
    ps.setLong(1, userId);
    try (ResultSet rs = ps.executeQuery()) {
        if (rs.next()) {
            return new User(rs.getLong("id"), rs.getString("name"));
        }
    }
}
```

### Fix 2: Create new statements for repeated execution

```java
public void logMessages(List<String> messages) {
    String sql = "INSERT INTO log (message) VALUES (?)";
    for (String msg : messages) {
        try (Connection conn = dataSource.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, msg);
            ps.executeUpdate();
        }
    }
}
```

### Fix 3: Batch operations without closing intermediate statements

```java
try (Connection conn = dataSource.getConnection();
     PreparedStatement ps = conn.prepareStatement("INSERT INTO cache (key, value) VALUES (?, ?)")) {
    for (Map.Entry<String, String> entry : cache.entrySet()) {
        ps.setString(1, entry.getKey());
        ps.setString(2, entry.getValue());
        ps.addBatch();
    }
    ps.executeBatch();
}
```

### Fix 4: Validate statement state before use in utility methods

```java
public static void safeExecute(PreparedStatement ps, String desc) throws SQLException {
    if (ps == null) throw new IllegalArgumentException("PreparedStatement is null");
    // Note: there is no isClosed() check in standard JDBC, so ensure proper lifecycle
    ps.execute();
}
```

## Prevention Tips

- Always use try-with-resources for statements.
- Do not store statements in class fields or collections for later reuse.
- Create a new statement for each distinct query execution cycle.

## Related Errors

- {{< relref "jdbc-resultset-closed" >}} — ResultSet closed error
- {{< relref "jdbc-closed-connection" >}} — Connection already closed
- {{< relref "jdbc-conn" >}} — Connection errors
