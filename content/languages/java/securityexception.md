---
title: "[Solution] Java SecurityException — Security Manager Violation Fix"
description: "Fix Java SecurityException by granting proper permissions, updating security policy files, and using AccessController.doPrivileged for sensitive operations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 30
---

# SecurityException — Security Manager Violation Fix

A `SecurityException` is thrown when a security manager denies an operation such as file access, network connection, class loading, or reflection. In modern Java, it can also arise from module-system access restrictions.

## Description

`java.lang.SecurityException` extends `RuntimeException`. Common variants include:

- `java.lang.SecurityException: Access denied`
- `java.lang.SecurityException: Can't access field "xxx" in class "yyy"`
- `java.lang.SecurityException: Prohibited package name: java.lang`
- `java.lang.SecurityException: class "com.example.MyClass"'s signer information does not match signer information of other classes in the same package`

When a `SecurityManager` is active, many JVM operations are checked against the current `AccessControlContext`. In Java 17+ and especially Java 21, the `SecurityManager` is deprecated for removal, but module-level restrictions still produce similar errors.

## Common Causes

```java
// Cause 1: File system access without permission
System.setSecurityManager(new SecurityManager());
File f = new File("/etc/passwd");
f.canRead();  // SecurityException: read access denied

// Cause 2: Network access without permission
URL url = new URL("http://example.com");
URLConnection conn = url.openConnection();  // SecurityException: network access

// Cause 3: Reflection access to restricted class
Field field = String.class.getDeclaredField("value");
field.setAccessible(true);  // SecurityException: illegal reflective access

// Cause 4: Loading a class from a restricted package
Class.forName("sun.misc.Unsafe");  // SecurityException in sandboxed environments

// Cause 5: Thread manipulation
Thread t = new Thread();
t.setContextClassLoader(null);  // SecurityException: class loader access
```

## Solutions

### Fix 1: Grant permissions in the security policy file

```java
// policy.file
grant codeBase "file:${APP_HOME}/lib/-" {
    permission java.io.FilePermission "${APP_HOME}/data/-", "read,write";
    permission java.net.SocketPermission "example.com:80", "connect";
    permission java.lang.RuntimePermission "accessClassInPackage.sun.misc";
};
```

### Fix 2: Use AccessController.doPrivileged for sensitive operations

```java
import java.security.AccessController;
import java.security.PrivilegedAction;

String result = AccessController.doPrivileged(
    (PrivilegedAction<String>) () -> {
        // Code that requires elevated permissions
        return System.getProperty("user.home");
    }
);
```

### Fix 3: Add JVM flags for module access

```bash
java --add-opens java.base/java.lang=ALL-UNNAMED \
     --add-opens java.base/java.io=ALL-UNNAMED \
     -jar app.jar
```

### Fix 4: Handle SecurityException with try-catch

```java
try {
    File file = new File("/restricted/path");
    file.delete();
} catch (SecurityException e) {
    logger.error("Security policy denies this operation: {}", e.getMessage());
    // Fall back to an alternative operation or notify the user
}
```

## Prevention Checklist

- Review security policy files when running in sandboxed environments
- Use `AccessController.doPrivileged` blocks for operations that genuinely need elevated permissions
- Test application in production-like security configuration (not just with all permissions)
- Avoid relying on deprecated `SecurityManager` — migrate to module-based restrictions
- Document required permissions for deployment

## Related Errors

- [IllegalAccessException](/languages/java/illegalaccessexception/) — Thrown when reflective access is denied
- [InaccessibleObjectException](/languages/java/inaccessibleobjectexception/) — Module-system access denial in Java 9+
- [AccessControlException](/languages/java/accesscontrolfile/) — Older variant thrown by SecurityManager
