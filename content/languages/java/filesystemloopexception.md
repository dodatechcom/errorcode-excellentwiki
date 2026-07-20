---
title: "[Solution] Java FileSystemLoopException — Symlink Cycle Detected Fix"
description: "Fix Java FileSystemLoopException by detecting cycles with visited set, using --follow with caution, and fixing symlink structure."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# FileSystemLoopException — Symlink Cycle Detected Fix

A `FileSystemLoopException` is thrown when a symlink (symbolic link) cycle is encountered during file system traversal. This prevents infinite loops when following symbolic links that eventually point back to themselves or an ancestor.

## Description

`java.nio.file.FileSystemLoopException` extends `FileSystemException` and is thrown by `Files.walkFileTree()`, `Files.walk()`, `Files.list()`, and `Files.readAttributes()` when a circular chain of symbolic links is detected.

Common message variants:

- `java.nio.file.FileSystemLoopException: /path`
- `Cycle detected`

## Common Causes

```java
// Cause 1: Direct self-referencing symlink
// ln -s /app/data /app/data/link
Path path = Path.of("/app/data/link/link/link...");
Files.walkFileTree(path, new SimpleFileVisitor<Path>() {
    // FileSystemLoopException when cycle detected
});

// Cause 2: Indirect cycle between two directories
// /a/link -> /b
// /b/link -> /a
Path path = Path.of("/a");
Files.walk(path).forEach(System.out::println);  // FileSystemLoopException

// Cause 3: Circular symlink in classpath or library
Path libDir = Path.of("/opt/libs");
Files.walk(libDir).forEach(p -> {
    // FileSystemLoopException if symlinks form a cycle
});

// Cause 4: Docker or container mount point cycles
// Container volume mount creates circular reference
Path containerPath = Path.of("/var/lib/docker/overlay2/...");
Files.walkFileTree(containerPath, visitor);

// Cause 5: Backup or archive symlink cycle
// Backup tool created symlinks that form a cycle
Path backupDir = Path.of("/backups/2024-01");
Files.walk(backupDir).forEach(System.out::println);
```

## Solutions

### Fix 1: Track visited paths to detect cycles

```java
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.Set;
import java.util.HashSet;

Set<Path> visited = new HashSet<>();

Files.walkFileTree(startPath, new SimpleFileVisitor<Path>() {
    @Override
    public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
            throws IOException {
        if (!visited.add(dir.toRealPath())) {
            System.err.println("Cycle detected at: " + dir);
            return FileVisitResult.SKIP_SUBTREE;
        }
        return FileVisitResult.CONTINUE;
    }

    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
            throws IOException {
        System.out.println(file);
        return FileVisitResult.CONTINUE;
    }
});
```

### Fix 2: Use Files.walk() with cycle detection

```java
Set<Path> visited = new HashSet<>();

Files.walk(startPath)
    .filter(path -> {
        try {
            return visited.add(path.toRealPath());
        } catch (IOException e) {
            return false;
        }
    })
    .forEach(System.out::println);
```

### Fix 3: Limit traversal depth to prevent infinite loops

```java
public static void walkWithDepthLimit(Path start, int maxDepth) {
    try (DirectoryStream<Path> stream = Files.newDirectoryStream(start)) {
        for (Path entry : stream) {
            if (maxDepth > 0 && Files.isDirectory(entry)) {
                walkWithDepthLimit(entry, maxDepth - 1);
            }
            System.out.println(entry);
        }
    } catch (IOException e) {
        System.err.println("Error: " + e.getMessage());
    }
}

// Usage — limit to 10 levels deep
walkWithDepthLimit(Path.of("/app"), 10);
```

### Fix 4: Use realpath resolution to detect cycles early

```java
public static boolean hasCycle(Path path) {
    try {
        Path realPath = path.toRealPath();
        Path parent = path.getParent();
        while (parent != null) {
            if (parent.toRealPath().equals(realPath)) {
                return true;
            }
            parent = parent.getParent();
        }
        return false;
    } catch (IOException e) {
        return false;
    }
}

// Usage
Path target = Path.of("/app/data/link");
if (hasCycle(target)) {
    System.err.println("Symlink cycle detected: " + target);
} else {
    Files.walk(target).forEach(System.out::println);
}
```

### Fix 5: Follow symlinks selectively

```java
// Don't follow symlinks — avoids cycles entirely
Files.walk(startPath, FileVisitOption.FOLLOW_LINKS)  // Risky
    .forEach(System.out::println);

// Safer — detect and skip symlinks
Files.walk(startPath)
    .filter(path -> !Files.isSymbolicLink(path))
    .forEach(System.out::println);

// Or handle with follow but detect cycles
Set<String> visitedRealPaths = new HashSet<>();
Files.walk(startPath, FileVisitOption.FOLLOW_LINKS)
    .filter(path -> {
        try {
            return visitedRealPaths.add(path.toRealPath().toString());
        } catch (IOException e) {
            return false;
        }
    })
    .forEach(System.out::println);
```

## Prevention Checklist

- Always detect and handle symlink cycles during file tree traversal.
- Use `Set<Path>` with `toRealPath()` to track visited directories.
- Consider limiting traversal depth as a safety measure.
- Avoid following symlinks unless absolutely necessary.
- Use `FileVisitOption.FOLLOW_LINKS` only with cycle detection in place.

## Related Errors

- [NoSuchFileException](../nosuchfileexception) — symlink target does not exist.
- [AccessDeniedException](../accessdeniedexception) — insufficient permissions to follow symlink.
- [NotLinkException](../notlinkexception) — file is not a symbolic link.
- [IOException](../ioexception) — parent class for all I/O failures.
