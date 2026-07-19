---
title: "[Solution] Java SQLSyntaxErrorException — invalid SQL syntax in executeQuery or executeUpdate"
description: "Fix Java SQLSyntaxErrorException when invalid sql syntax in executequery or executeupdate with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLSyntaxErrorException — invalid SQL syntax in executeQuery or executeUpdate

A `SQLSyntaxErrorException` occurs when Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FORM users");  // FORM typo.

## Common Causes

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FORM users");  // FORM typo
```

## Solutions

```java
// Fix: use PreparedStatement
String sql = "SELECT id, name FROM users WHERE active = ?";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setBoolean(1, true);
    ResultSet rs = ps.executeQuery();
}

// Fix: parameterized queries
String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
try (PreparedStatement ps = conn.prepareStatement(sql)) {
    ps.setString(1, name); ps.setString(2, email);
    ps.executeUpdate();
}
```

## Prevention Checklist

- Always use PreparedStatement.
- Validate SQL before deploying.
- Use database-specific SQL validators.
- Log SQL queries for debugging.

## Related Errors

SQLTransientException, DataAccessException
