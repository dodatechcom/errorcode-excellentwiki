---
title: "[Solution] Java AccessDeniedException — File Permission Denied Fix"
description: "Fix Java AccessDeniedException by checking file permissions, running with appropriate user, using chmod/chown, and handling security policy."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# AccessDeniedException — File Permission Denied Fix

An `AccessDeniedException` is thrown when a file system operation is denied due to insufficient permissions. This is a common security-related exception when the JVM process does not have the required read, write, or execute permissions on a file or directory.

## Description

`java.nio.file.AccessDeniedException` extends `FileSystemException` and is thrown by `java.nio.file.Files` methods, `FileChannel`, and other file operations when the OS denies access.

Common message variants:

- `java.nio.file.AccessDeniedException: /path/to/file`
- `Access denied`
- `Permission denied`

This is the NIO equivalent of `java.io.FileNotFoundException` with permission issues, and is also related to `java.security.AccessControlException`.

## Common Causes

```java
// Cause 1: Reading a file without read permission
Path path = Path.of("/etc/shadow");
Files.readString(path);  // AccessDeniedException

// Cause 2: Writing to a read-only directory
Path readOnlyDir = Path.of("/usr/local/readonly");
Path file = readOnlyDir.resolve("output.txt");
Files.writeString(file, "data");  // AccessDeniedException

// Cause 3: Creating file in directory without write permission
Path restrictedDir = Path.of("/etc");
Path newFile = restrictedDir.resolve("myconfig.conf");
Files.createFile(newFile);  // AccessDeniedException

// Cause 4: Executing a script without execute permission
Path script = Path.of("/opt/app/run.sh");
Files.setPosixFilePermissions(script,
    Set.of(PosixFilePermission.OWNER_READ));  // No execute bit
Runtime.getRuntime().exec(script.toString());  // AccessDeniedException

// Cause 5: Accessing another user's home directory
Path otherHome = Path.of("/home/otheruser/private");
Files.list(otherHome);  // AccessDeniedException
```

## Solutions

### Fix 1: Check and set file permissions before operations

```java
Path path = Path.of("/var/data/output.txt");

// Check permissions
if (!Files.isReadable(path)) {
    throw new AccessDeniedException("Cannot read: " + path);
}

// Set permissions (POSIX systems)
Set<PosixFilePermission> perms = Set.of(
    PosixFilePermission.OWNER_READ,
    PosixFilePermission.OWNER_WRITE);
Files.setPosixFilePermissions(path, perms);
```

### Fix 2: Run with appropriate user or use sudo

```bash
# Check current user
whoami

# Run Java application with correct user
sudo -u appuser java -jar myapp.jar

# Or use setfacl for fine-grained access
setfacl -R -m u:appuser:rwx /var/data/
```

### Fix 3: Create directories with correct permissions

```java
Path dir = Path.of("/opt/app/data");
if (!Files.exists(dir)) {
    Files.createDirectories(dir, PosixFilePermissions.asFileAttribute(
        Set.of(
            PosixFilePermission.OWNER_READ,
            PosixFilePermission.OWNER_WRITE,
            PosixFilePermission.OWNER_EXECUTE)));
}
```

### Fix 4: Use try-catch with appropriate fallback

```java
public static String readWithFallback(Path path, String defaultValue) {
    try {
        return Files.readString(path);
    } catch (AccessDeniedException e) {
        System.err.println("No permission to read " + path + ": " + e.getMessage());
        return defaultValue;
    } catch (IOException e) {
        System.err.println("I/O error reading " + path + ": " + e.getMessage());
        return defaultValue;
    }
}
```

### Fix 5: Use privileged action for security-manager-controlled environments

```java
import java.security.AccessController;
import java.security.PrivilegedAction;
import java.security.PrivilegedExceptionAction;

String content = AccessController.doPrivileged(
    (PrivilegedExceptionAction<String>) () -> Files.readString(path));
```

### Fix 6: Use temporary files for write-heavy operations

```java
import java.nio.file.Files;

Path tempDir = Files.createTempDirectory("app-work");
Path tempFile = Files.createFile(tempDir.resolve("output.tmp"));

try {
    Files.writeString(tempFile, data);
    // Process or copy to final location
    Files.move(tempFile, finalPath, StandardCopyOption.REPLACE_EXISTING);
} finally {
    Files.deleteIfExists(tempFile);
    Files.deleteIfExists(tempDir);
}
```

## Prevention Checklist

- Verify file permissions before attempting read/write operations.
- Run the application with the minimum required permissions (principle of least privilege).
- Use `Files.exists()`, `Files.isReadable()`, `Files.isWritable()` before operations.
- Create directories with correct permissions using `PosixFilePermissions`.
- Handle `AccessDeniedException` with user-friendly error messages.
- Use temporary directories for intermediate write operations.

## Related Errors

- [FileNotFoundException](../filenotfoundexception) — file not found or inaccessible.
- [SecurityException](../securityexception) — security manager denied operation.
- [FileSystemException](../filesystemexception) — parent class for file system errors.
- [IOException](../ioexception) — parent class for all I/O failures.
