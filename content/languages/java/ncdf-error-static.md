---
title: "[Solution] Java NoClassDefFoundError — class static initializer throws, marking class as failed"
description: "Fix Java NoClassDefFoundError when class static initializer throws, marking class as failed with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoClassDefFoundError — class static initializer throws, marking class as failed

A `NoClassDefFoundError` occurs when public class AppConfig {
    private static final Connection CONN = DriverManager.getConnection("jdbc:...");
    // If throws, AppConfig marked failed
}.

## Common Causes

```java
public class AppConfig {
    private static final Connection CONN = DriverManager.getConnection("jdbc:...");
    // If throws, AppConfig marked failed
}
```

## Solutions

```java
// Fix: lazy init
public class AppConfig {
    private static Connection conn;
    public static Connection getConn() {
        if (conn == null) conn = DriverManager.getConnection("jdbc:...");
        return conn;
    }
}

// Fix: try-catch in static block
static {
    try { cache = loadFromRedis(); }
    catch (Exception e) { cache = new HashMap<>(); }
}
```

## Prevention Checklist

- Avoid heavy static block init.
- Wrap in try-catch with fallback.
- Use Holder pattern for lazy init.

## Related Errors

ExceptionInInitializerError, UnsatisfiedLinkError
