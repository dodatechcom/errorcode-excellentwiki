---
title: "[Solution] Java IllegalStateException — using a connection, HTTP connection, or stream after it has been closed"
description: "Fix Java IllegalStateException when using a connection, http connection, or stream after it has been closed with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalStateException — using a connection, HTTP connection, or stream after it has been closed

A `IllegalStateException` occurs when Connection conn = dataSource.getConnection();
conn.close();
conn.prepareStatement("...");  // ISE.

## Common Causes

```java
Connection conn = dataSource.getConnection();
conn.close();
conn.prepareStatement("...");  // ISE
```

## Solutions

```java
// Fix: try-with-resources
try (Connection c = dataSource.getConnection();
     PreparedStatement ps = c.prepareStatement("...")) {
    // auto-closed
}

// Fix: check isValid
if (connection.isValid(1)) {
    PreparedStatement ps = connection.prepareStatement("...");
}
```

## Prevention Checklist

- Always use try-with-resources.
- Never close and reuse connections.
- Cache reactive streams with .cache().

## Related Errors

IOException, SQLException
