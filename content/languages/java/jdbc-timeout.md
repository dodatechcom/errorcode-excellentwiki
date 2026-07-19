---
title: "[Solution] Java SQLTransientException — database query exceeds configured timeout"
description: "Fix Java SQLTransientException when database query exceeds configured timeout with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SQLTransientException — database query exceeds configured timeout

A `SQLTransientException` occurs when Statement stmt = conn.createStatement();
stmt.setQueryTimeout(30);
ResultSet rs = stmt.executeQuery("SELECT * FROM large_table");.

## Common Causes

```java
Statement stmt = conn.createStatement();
stmt.setQueryTimeout(30);
ResultSet rs = stmt.executeQuery("SELECT * FROM large_table");
```

## Solutions

```java
// Fix: set timeout
stmt.setQueryTimeout(30);  // 30 seconds

// Fix: connection timeout in pool
HikariConfig cfg = new HikariConfig();
cfg.setConnectionTimeout(30000); cfg.setLoginTimeout(10);

// Fix: add indexes
// CREATE INDEX idx_email ON users(email);
```

## Prevention Checklist

- Set setQueryTimeout() for all queries.
- Add indexes for frequently queried columns.
- Monitor slow query logs.
- Use EXPLAIN to analyze performance.

## Related Errors

SQLException, SQLRecoverableException
