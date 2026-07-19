---
title: "[Solution] Java AccessControlException — security manager denies network socket or connection permission"
description: "Fix Java AccessControlException when security manager denies network socket or connection permission with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# AccessControlException — security manager denies network socket or connection permission

A `AccessControlException` occurs when Socket s = new Socket("example.com", 80);  // AccessControlException.

## Common Causes

```java
Socket s = new Socket("example.com", 80);  // AccessControlException
```

## Solutions

```java
// Fix: check permission
SecurityManager sm = System.getSecurityManager();
if (sm != null) {
    sm.checkConnect("example.com", 80);
}

// Fix: handle gracefully
try {
    Socket s = new Socket("example.com", 80);
} catch (AccessControlException e) {
    log.warn("Network access denied", e);
    // fallback to alternative
}

// Fix: configure security policy
// grant { permission java.net.SocketPermission "example.com:80", "connect"; };
```

## Prevention Checklist

- Check network permissions before connection.
- Handle AccessControlException gracefully.
- Configure security policies for required access.
- Use try-catch for security-sensitive operations.

## Related Errors

SocketException, SecurityException
