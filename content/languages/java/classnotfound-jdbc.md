---
title: "[Solution] Java ClassNotFoundException — database driver JAR missing or wrong class name used in Class.forName"
description: "Fix Java ClassNotFoundException when database driver jar missing or wrong class name used in class.forname with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — database driver JAR missing or wrong class name used in Class.forName

A `ClassNotFoundException` occurs when Class.forName("com.mysql.cj.jdbc.Driver");  // ClassNotFoundException.

## Common Causes

```java
Class.forName("com.mysql.cj.jdbc.Driver");  // ClassNotFoundException
```

## Solutions

```java
// JDBC 4.0+ — auto-loading
Connection conn = DriverManager.getConnection(url, user, pass);

// Verify driver
try { Class.forName("com.mysql.cj.jdbc.Driver"); }
catch (ClassNotFoundException e) {
    System.err.println("Classpath: " + System.getProperty("java.class.path"));
}
```

## Prevention Checklist

- Add driver dependency in compile scope.
- Use JDBC 4.0+ auto-loading.
- Verify driver class name.

## Related Errors

ClassNotFoundException, NoClassDefFoundError
