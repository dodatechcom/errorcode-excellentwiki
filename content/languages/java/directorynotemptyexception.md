---
title: "[Solution] Java DirectoryNotEmptyException — Non-Empty Directory Fix"
description: "Fix Java DirectoryNotEmptyException by deleting contents first, using Files.walk for recursive delete, and handling file deletion order."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# DirectoryNotEmptyException — Non-Empty Directory Fix

A `DirectoryNotEmptyException` is thrown when an attempt is made to delete, move, or rename a directory that still contains files or subdirectories. The OS prevents removal of non-empty directories.

## Description

`java.nio.file.DirectoryNotEmptyException` extends `FileSystemException` and is thrown by `Files.delete()`, `Files.deleteIfExists()`, `Files.move()`, and `File.delete()` when the target directory is not empty.

Common message variants:

- `java.nio.file.DirectoryNotEmptyException: /path/to/directory`
- `Directory not empty`

## Common Causes

```java
// Cause 1: Attempting to delete non-empty directory
Path dir = Path.of("/var/data/cache");
// dir contains files
Files.delete(dir);  // DirectoryNotEmptyException

// Cause 2: Moving non-empty directory with REPLACE_EXISTING
Path source = Path.of("/tmp/old-build");
Path target = Path.of("/opt/current");
// target is a non-empty directory
Files.move(source, target, StandardCopyOption.REPLACE_EXISTING);  // DirectoryNotEmptyException

// Cause 3: File.delete() on non-empty directory
File dir = new File("/var/log/app");
boolean deleted = dir.delete();  // Returns false, no exception

// Cause 4: Attempting atomic move of directory
Files.move(source, target,
    StandardCopyOption.ATOMIC_MOVE,
    StandardCopyOption.REPLACE_EXISTING);  // May throw DirectoryNotEmptyException

// Cause 5: Deleting directory before all file handles are closed
// Files still open by other threads
Path dir = Path.of("temp/work");
Files.delete(dir);  // DirectoryNotEmptyException if files still open
```

## Solutions

### Fix 1: Delete directory contents first

```java
Path dir = Path.of("/var/data/cache");

// Delete all files in directory first
try (DirectoryStream<Path> stream = Files.newDirectoryStream(dir)) {
    for (Path file : stream) {
        Files.delete(file);
    }
}
// Now delete the directory
Files.delete(dir);
```

### Fix 2: Use Files.walk() for recursive deletion

```java
import java.nio.file.FileVisitResult;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;

Path dir = Path.of("/var/data/cache");

Files.walkFileTree(dir, new SimpleFileVisitor<Path>() {
    @Override
    public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
            throws IOException {
        Files.delete(file);
        return FileVisitResult.CONTINUE;
    }

    @Override
    public FileVisitResult postVisitDirectory(Path d, IOException exc)
            throws IOException {
        Files.delete(d);
        return FileVisitResult.CONTINUE;
    }
});
```

### Fix 3: Use Files.walk() with Stream API (Java 8+)

```java
Path dir = Path.of("/var/data/cache");

// Sort deepest-first so subdirectories are deleted before parents
Files.walk(dir)
    .sorted((a, b) -> b.compareTo(a))
    .forEach(path -> {
        try {
            Files.delete(path);
        } catch (IOException e) {
            System.err.println("Cannot delete: " + path + " — " + e.getMessage());
        }
    });
```

### Fix 4: Use FileUtils from Apache Commons or Guava

```java
// Apache Commons IO
import org.apache.commons.io.FileUtils;
FileUtils.deleteDirectory(dir.toFile());

// Guava
import com.google.common.io.Files;
Files.deleteRecursively(dir.toFile());

// Or use standard library (Java 12+)
import java.nio.file.Files;
// Files.walk() approach shown above
```

### Fix 5: Handle deletion order properly

```java
public static void deleteDirectoryRecursive(Path dir) throws IOException {
    if (!Files.isDirectory(dir)) {
        Files.delete(dir);
        return;
    }

    // List and sort — delete files before directories
    Files.walk(dir)
        .sorted(Comparator.reverseOrder())
        .forEach(path -> {
            try {
                Files.deleteIfExists(path);
            } catch (DirectoryNotEmptyException e) {
                // Directory still has open files — retry after delay
                try { Thread.sleep(100); } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                }
                try { Files.deleteIfExists(path); } catch (IOException ex) {
                    System.err.println("Failed to delete: " + path);
                }
            } catch (IOException e) {
                System.err.println("Failed to delete: " + path + " — " + e.getMessage());
            }
        });
}
```

### Fix 6: Use temporary directory for atomic moves

```java
Path source = Path.of("/tmp/build");
Path tempTarget = Path.of("/opt/temp-deploy");
Path finalTarget = Path.of("/opt/current");

// Move to temp location first
Files.move(source, tempTarget, StandardCopyOption.REPLACE_EXISTING);

// Delete old current
deleteDirectoryRecursive(finalTarget);

// Move from temp to final
Files.move(tempTarget, finalTarget);
```

## Prevention Checklist

- Always delete directory contents before deleting the directory itself.
- Use `Files.walkFileTree()` or `Files.walk()` with `Comparator.reverseOrder()` for recursive deletion.
- Handle `DirectoryNotEmptyException` with retry logic for open file handles.
- Use atomic moves with temp directories for deployment operations.
- Consider using established libraries (Commons IO, Guava) for complex file operations.

## Related Errors

- [NoSuchFileException](../nosuchfileexception) — file or directory does not exist.
- [AccessDeniedException](../accessdeniedexception) — insufficient permissions to delete.
- [FileSystemLoopException](../filesystemloopexception) — symlink cycle during traversal.
- [IOException](../ioexception) — parent class for all I/O failures.
