---
title: "[Solution] Java AccessControlException — security manager denies file read/write/execute permission"
description: "Fix Java AccessControlException when security manager denies file read/write/execute permission with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# AccessControlException — security manager denies file read/write/execute permission

A `AccessControlException` occurs when File f = new File("/etc/passwd");
FileInputStream fis = new FileInputStream(f);  // AccessControlException.

## Common Causes

```java
File f = new File("/etc/passwd");
FileInputStream fis = new FileInputStream(f);  // AccessControlException
```

## Solutions

```java
// Fix: check permissions
if (f.canRead()) {
    FileInputStream fis = new FileInputStream(f);
}

// Fix: use SecurityManager API
SecurityManager sm = System.getSecurityManager();
if (sm != null) {
    sm.checkRead(f.getAbsolutePath());
}

// Fix: handle in try-catch
try {
    FileInputStream fis = new FileInputStream(f);
} catch (AccessControlException e) {
    log.warn("Permission denied: "+f, e);
}
```

## Prevention Checklist

- Check file permissions before access.
- Handle AccessControlException in catch blocks.
- Use java.nio.file.Files for NIO access.
- Configure security policies appropriately.

## Related Errors

FileNotFoundException, SecurityException
