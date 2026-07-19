---
title: "[Solution] Java AccessControlException — security manager denies read/write of system properties"
description: "Fix Java AccessControlException when security manager denies read/write of system properties with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# AccessControlException — security manager denies read/write of system properties

A `AccessControlException` occurs when String home = System.getProperty("user.home");  // AccessControlException.

## Common Causes

```java
String home = System.getProperty("user.home");  // AccessControlException
```

## Solutions

```java
// Fix: check permission
SecurityManager sm = System.getSecurityManager();
if (sm != null) {
    sm.checkPropertyAccess("user.home");
}

// Fix: use fallback
String home = AccessController.doPrivileged((PrivilegedAction<String>)
    () -> System.getProperty("user.home", "/tmp"));

// Fix: handle gracefully
try {
    String home = System.getProperty("user.home");
} catch (AccessControlException e) {
    home = "/default";
}
```

## Prevention Checklist

- Use AccessController.doPrivileged() for privileged access.
- Provide fallback values for system properties.
- Handle AccessControlException in catch blocks.
- Configure security policies appropriately.

## Related Errors

SecurityException, NullPointerException
