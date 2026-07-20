---
title: "[Solution] Java AtomicMoveNotSupportedException — Atomic Move Not Supported Fix"
description: "Fix Java AtomicMoveNotSupportedException by using non-atomic move, handling partial moves, and implementing fallback strategy."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# AtomicMoveNotSupportedException — Atomic Move Not Supported Fix

An `AtomicMoveNotSupportedException` is thrown when a file cannot be moved atomically. This occurs when `StandardCopyOption.ATOMIC_MOVE` is specified but the file system does not support atomic file moves, or the move cannot be performed atomically.

## Description

`java.nio.file.AtomicMoveNotSupportedException` extends `FileSystemException` and is thrown by `Files.move()` when `ATOMIC_MOVE` is requested but the target file system cannot guarantee atomicity. Atomic moves ensure the file is either fully moved or not moved at all — no intermediate state is visible.

Common message variants:

- `java.nio.file.AtomicMoveNotSupportedException`
- `Atomic move not supported`

## Common Causes

```java
// Cause 1: Cross-device move (atomic move not possible)
Path source = Path.of("/mnt/disk1/temp.dat");
Path target = Path.of("/mnt/disk2/data.dat");
Files.move(source, target, StandardCopyOption.ATOMIC_MOVE);
// AtomicMoveNotSupportedException — different mount points

// Cause 2: File system doesn't support atomic moves
// Network filesystem (NFS, SMB) may not support atomic rename
Path source = Path.of("/mnt/nfs/temp.dat");
Path target = Path.of("/mnt/nfs/data.dat");
Files.move(source, target, StandardCopyOption.ATOMIC_MOVE);

// Cause 3: Target exists and atomic replace not supported
Path source = Path.of("/tmp/new-config.txt");
Path target = Path.of("/etc/app/config.txt");
Files.move(source, target,
    StandardCopyOption.ATOMIC_MOVE,
    StandardCopyOption.REPLACE_EXISTING);

// Cause 4: Same file system but directory boundary
Path source = Path.of("/data/temp.dat");
Path target = Path.of("/data/subdir/data.dat");
// May fail atomically if target directory is on different device

// Cause 5: Temp directory on different filesystem
Path source = Files.createTempFile("output", ".tmp");
Path target = Path.of("/var/data/result.dat");
Files.move(source, target, StandardCopyOption.ATOMIC_MOVE);
```

## Solutions

### Fix 1: Handle AtomicMoveNotSupportedException with fallback

```java
Path source = Path.of("/tmp/data.dat");
Path target = Path.of("/opt/data.dat");

try {
    Files.move(source, target,
        StandardCopyOption.ATOMIC_MOVE,
        StandardCopyOption.REPLACE_EXISTING);
} catch (AtomicMoveNotSupportedException e) {
    // Fallback to non-atomic move
    Files.move(source, target, StandardCopyOption.REPLACE_EXISTING);
}
```

### Fix 2: Try atomic move first, then copy-and-delete

```java
public static void safeMove(Path source, Path target) throws IOException {
    try {
        Files.move(source, target,
            StandardCopyOption.ATOMIC_MOVE,
            StandardCopyOption.REPLACE_EXISTING);
    } catch (AtomicMoveNotSupportedException e) {
        // Atomic move not supported — try non-atomic
        try {
            Files.move(source, target, StandardCopyOption.REPLACE_EXISTING);
        } catch (AtomicMoveNotSupportedException | IOException ex) {
            // Non-atomic move also failed — fall back to copy + delete
            Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
            Files.delete(source);
        }
    }
}
```

### Fix 3: Use same filesystem for atomic operations

```java
// Ensure source and target are on same filesystem
Path tempDir = target.getParent().resolve(".tmp");
Files.createDirectories(tempDir);

Path tempFile = tempDir.resolve(source.getFileName());
Files.move(source, tempFile, StandardCopyOption.ATOMIC_MOVE);

// Atomic move within same filesystem
Files.move(tempFile, target, StandardCopyOption.ATOMIC_MOVE);
```

### Fix 4: Implement full fallback strategy

```java
public enum MoveStrategy {
    ATOMIC, NON_ATOMIC, COPY_DELETE
}

public static void moveWithStrategy(Path source, Path target,
        MoveStrategy preferred) throws IOException {
    switch (preferred) {
        case ATOMIC:
            try {
                Files.move(source, target,
                    StandardCopyOption.ATOMIC_MOVE,
                    StandardCopyOption.REPLACE_EXISTING);
                return;
            } catch (AtomicMoveNotSupportedException e) {
                // Fall through to non-atomic
            }
            // Fall through intentionally

        case NON_ATOMIC:
            try {
                Files.move(source, target,
                    StandardCopyOption.REPLACE_EXISTING);
                return;
            } catch (AtomicMoveNotSupportedException e) {
                // Fall through to copy-delete
            }
            // Fall through intentionally

        case COPY_DELETE:
            Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
            Files.delete(source);
            break;
    }
}
```

### Fix 5: Check filesystem capabilities before move

```java
import java.nio.file.FileStore;
import java.nio.file.Files;

FileStore sourceStore = Files.getFileStore(source.getParent());
FileStore targetStore = Files.getFileStore(target.getParent());

if (!sourceStore.equals(targetStore)) {
    // Different filesystems — atomic move likely won't work
    System.out.println("Cross-device move detected — using copy+delete");
    Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
    Files.delete(source);
} else {
    // Same filesystem — atomic move should work
    Files.move(source, target,
        StandardCopyOption.ATOMIC_MOVE,
        StandardCopyOption.REPLACE_EXISTING);
}
```

## Prevention Checklist

- Always handle `AtomicMoveNotSupportedException` with a fallback strategy.
- Keep source and target on the same filesystem when atomic moves are required.
- Use temp directories on the same filesystem as the target for staged moves.
- Check `FileStore` equality to predict cross-device moves.
- Prefer `ATOMIC_MOVE` for deployment operations to avoid partial states.

## Related Errors

- [DirectoryNotEmptyException](../directorynotemptyexception) — target directory not empty.
- [NoSuchFileException](../nosuchfileexception) — source file does not exist.
- [AccessDeniedException](../accessdeniedexception) — insufficient permissions.
- [IOException](../ioexception) — parent class for all I/O failures.
