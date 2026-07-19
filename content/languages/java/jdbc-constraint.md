---
title: "[Solution] Java SQLIntegrityConstraintViolationException — INSERT/UPDATE violates PRIMARY KEY, FOREIGN KEY, or UNIQUE constraints"
description: "Fix Java SQLIntegrityConstraintViolationException when insert/update violates primary key, foreign key, or unique constraints with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLIntegrityConstraintViolationException — INSERT/UPDATE violates PRIMARY KEY, FOREIGN KEY, or UNIQUE constraints

A `SQLIntegrityConstraintViolationException` occurs when PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, 1); ps.setString(2, "Alice");
ps.executeUpdate();  // SQLIntegrityConstraintViolationException if id=1 exists.

## Common Causes

```java
PreparedStatement ps = conn.prepareStatement("INSERT INTO users (id, name) VALUES (?, ?)");
ps.setInt(1, 1); ps.setString(2, "Alice");
ps.executeUpdate();  // SQLIntegrityConstraintViolationException if id=1 exists
```

## Solutions

```java
// Fix: UPSERT
String sql = "INSERT INTO users (id, name) VALUES (?, ?) " +
    "ON DUPLICATE KEY UPDATE name = VALUES(name)";

// Fix: catch constraint violation
try { ps.executeUpdate(); }
catch (SQLIntegrityConstraintViolationException e) {
    // duplicate — use UPDATE instead
}

// Fix: check existence first
ResultSet rs = ps2.executeQuery("SELECT 1 FROM users WHERE id = ?");
if (!rs.next()) { /* INSERT */ } else { /* UPDATE */ }
```

## Prevention Checklist

- Use UPSERT/MERGE for idempotent inserts.
- Handle SQLIntegrityConstraintViolationException gracefully.
- Validate foreign key references before insert.
- Use database-specific upsert syntax.

## Related Errors

SQLException, DataIntegrityViolationException
