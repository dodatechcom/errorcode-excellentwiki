---
title: "[Solution] Java InvalidPathException — Path Validation Fix"
description: "Fix Java InvalidPathException by validating file paths, handling platform-specific path separators, and sanitizing user-supplied path strings."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["invalidpathexception", "path", "filesystem", "nio", "security"]
weight: 5
---

# InvalidPathException — Path Validation Fix

An `InvalidPathException` is thrown when a path string cannot be converted to a `Path` because it contains illegal characters, invalid syntax, or is otherwise malformed. This is an NIO.2 exception (`java.nio.file.InvalidPathException`).

## Description

The exception occurs when calling `Paths.get()`, `Path.of()`, or `FileSystems.getDefault().getPath()` with an invalid path string. Common message variants:

- `InvalidPathException: Illegal char <:> at index 2: C:\path`
- `InvalidPathException: Null byte in path`
- `InvalidPathException: ... has an empty name element`
- `InvalidPathException: Trailing file separator`

## Common Causes

```java
// Cause 1: Null byte character in path
Path path = Paths.get("/data/file\u0000.txt");  // InvalidPathException

// Cause 2: Platform-specific illegal characters
// On Windows: < > : " | ? *
Path path = WindowsFileSystem.getPath("file:name.txt");  // Invalid on Windows

// Cause 3: Empty path components
Path path = Paths.get("/data//file.txt");  // May cause issues depending on OS

// Cause 4: Null path string
String userInput = null;
Path path = Paths.get(userInput);  // NullPointerException or InvalidPathException
```

## Solutions

### Fix 1: Validate path before converting to Path

```java
public static Path safePath(String pathString) {
    if (pathString == null || pathString.isBlank()) {
        throw new IllegalArgumentException("Path must not be null or empty");
    }
    if (pathString.contains("\u0000")) {
        throw new InvalidPathException(pathString, "Path contains null byte");
    }
    return Paths.get(pathString);
}
```

### Fix 2: Sanitize user-supplied paths

```java
public static String sanitizePath(String userInput) {
    // Remove null bytes
    String sanitized = userInput.replace("\0", "");

    // Normalize path separators
    sanitized = sanitized.replace("\\", "/");

    // Remove duplicate separators
    sanitized = sanitized.replaceAll("/+", "/");

    // Remove leading/trailing whitespace and separators
    sanitized = sanitized.strip().replaceAll("^/|/$", "");

    return sanitized;
}
```

### Fix 3: Use `Path.of()` with proper error handling

```java
try {
    Path path = Path.of(userInput);
    // Path created successfully
} catch (InvalidPathException e) {
    System.err.println("Invalid path: " + e.getReason());
    // Handle error — log, return default, etc.
}
```

### Fix 4: Resolve paths safely relative to a base directory

```java
import java.nio.file.Path;
import java.nio.file.Paths;

Path basePath = Paths.get("/data/uploads");

public Path resolveSafe(String userInput) {
    Path resolved = basePath.resolve(userInput).normalize();

    // Ensure resolved path is still within basePath (prevent path traversal)
    if (!resolved.startsWith(basePath)) {
        throw new SecurityException("Path traversal detected: " + userInput);
    }

    return resolved;
}
```

## Prevention Checklist

- Always validate user-supplied path strings before converting to `Path`.
- Use `Path.normalize()` to resolve `.` and `..` components safely.
- Check for path traversal attacks when resolving user input relative to a base directory.
- Handle `InvalidPathException` when parsing paths from external sources.

## Related Errors

- [FileNotFoundException](../filenotfoundexception) — valid path but file does not exist.
- [IOException](../ioexception) — I/O error accessing the path.
- [FileAlreadyExistsException](../filealreadyexistsexception) — file already exists at the path.
- [SecurityException](../illegalaccessexception) — security manager denied path access.
