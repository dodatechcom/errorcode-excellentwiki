---
title: "[Solution] Java FileAlreadyExistsException — File Conflict Fix"
description: "Fix Java FileAlreadyExistsException by using CREATE, CREATE_NEW, or TRUNCATE_EXISTING options, checking file existence, or handling duplicate file names."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["filealreadyexistsexception", "file", "nio", "filesystem", "create"]
weight: 5
---

# FileAlreadyExistsException — File Conflict Fix

A `FileAlreadyExistsException` is thrown when an attempt is made to create a file that already exists. This is an NIO.2 exception (`java.nio.file.FileAlreadyExistsException`) and is a subclass of `FileSystemException`.

## Description

The exception occurs when using `Files.createFile()`, `Files.createDirectory()`, or writing with `StandardOpenOption.CREATE_NEW` on a path that already exists:

- `java.nio.file.FileAlreadyExistsException: /path/to/file.txt`
- `java.nio.file.FileAlreadyExistsException: /path/to/directory`

## Common Causes

```java
// Cause 1: Creating a file that already exists
Path path = Paths.get("/data/output.txt");
Files.createFile(path);  // FileAlreadyExistsException if file exists

// Cause 2: Using CREATE_NEW option on existing file
Files.writeString(path, "data", StandardOpenOption.CREATE_NEW);  // Throws if exists

// Cause 3: Creating a directory that already exists as a file
Path dir = Paths.get("/data/subdir");
Files.createDirectory(dir);  // Throws if "subdir" is a file, not a directory

// Cause 4: Race condition — two threads creating the same file
// Thread A and Thread B both call Files.createFile(path)
```

## Solutions

### Fix 1: Check existence before creating

```java
Path path = Paths.get("/data/output.txt");

if (!Files.exists(path)) {
    Files.createFile(path);
}

// Or use CREATE (creates if not exists, does nothing if exists)
Files.writeString(path, "data", StandardOpenOption.CREATE);
```

### Fix 2: Use appropriate open options

```java
Path path = Paths.get("/data/output.txt");

// CREATE: create if not exists, open if exists (no truncation)
Files.writeString(path, "new data", StandardOpenOption.CREATE);

// CREATE_NEW: fail if exists (what createFile does)
// Files.writeString(path, "data", StandardOpenOption.CREATE_NEW);

// TRUNCATE_EXISTING: create if not exists, truncate if exists
Files.writeString(path, "new data",
    StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
```

### Fix 3: Use atomic file operations to avoid race conditions

```java
Path tempPath = Files.createTempFile(dir, "output", ".tmp");
try {
    Files.writeString(tempPath, "data");
    // Atomically move into place
    Files.move(tempPath, targetPath, StandardCopyOption.REPLACE_EXISTING,
        StandardCopyOption.ATOMIC_MOVE);
} catch (IOException e) {
    Files.deleteIfExists(tempPath);
    throw e;
}
```

### Fix 4: Create directories safely

```java
Path dir = Paths.get("/data/subdir");

// createDirectories creates all missing parent directories too
Files.createDirectories(dir);  // No exception if dir already exists

// createDirectory only creates the final component — throws if parents missing
// Files.createDirectory(dir);  // Fails if /data doesn't exist
```

## Prevention Checklist

- Use `StandardOpenOption.CREATE` instead of `CREATE_NEW` when you want to overwrite silently.
- Always call `Files.exists()` before `Files.createFile()` if the file may already exist.
- Use `Files.createDirectories()` instead of `Files.createDirectory()` for nested paths.
- Use temp files and atomic moves to avoid race conditions in concurrent environments.

## Related Errors

- [FileNotFoundException](../filenotfoundexception) — file not found when trying to read.
- [IOException](../ioexception) — general I/O failure.
- [InvalidPathException](../invalidpathexception) — malformed path string.
- [AccessDeniedException](../filenotfoundexception) — permission denied (subclass of FileSystemException).
