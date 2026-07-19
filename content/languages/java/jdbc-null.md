---
title: "[Solution] Java SQLDataException — accessing database columns with null values without handling"
description: "Fix Java SQLDataException when accessing database columns with null values without handling with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLDataException — accessing database columns with null values without handling

A `SQLDataException` occurs when ResultSet rs = stmt.executeQuery("SELECT name, email FROM users");
while (rs.next()) {
    String email = rs.getString("email");
    int len = email.length();  // NPE if email is null
}.

## Common Causes

```java
ResultSet rs = stmt.executeQuery("SELECT name, email FROM users");
while (rs.next()) {
    String email = rs.getString("email");
    int len = email.length();  // NPE if email is null
}
```

## Solutions

```java
// Fix: null-check
while (rs.next()) {
    String email = rs.getString("email");
    if (email != null) { int len = email.length(); }
}

// Fix: wasNull()
int id = rs.getInt("id");
boolean wasNull = rs.wasNull();

// Fix: Optional
Optional<String> email = Optional.ofNullable(rs.getString("email"));
```

## Prevention Checklist

- Always null-check ResultSet values.
- Use rs.wasNull() for SQL NULL.
- Use Optional for nullable columns.
- Define columns as NOT NULL when possible.

## Related Errors

NullPointerException, SQLException
