---
title: "[Solution] Java SyncFailedException — FileDescriptor Sync Fix"
description: "Fix Java SyncFailedException by handling sync failures, checking disk health, and using fsync alternatives."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# SyncFailedException — FileDescriptor Sync Fix

A `SyncFailedException` is thrown when `FileDescriptor.sync()` or `FileChannel.force()` fails to flush file metadata to stable storage. This indicates the OS could not guarantee that data has been physically written to disk.

## Description

`java.io.SyncFailedException` extends `IOException` and is specific to file descriptor synchronization. Common message variants:

- `java.io.SyncFailedException`
- `sync failed`
- `Structure needs cleaning` (ext4 filesystem error)

This typically occurs when the underlying filesystem or storage device cannot complete the sync operation due to disk errors, full disk, or hardware failures.

## Common Causes

```java
// Cause 1: Calling sync on a closed or invalid file descriptor
FileOutputStream fos = new FileOutputStream("data.txt");
fos.close();
fos.getFD().sync();  // SyncFailedException

// Cause 2: Disk is full or quota exceeded
FileOutputStream fos = new FileOutputStream("large_output.bin");
fos.write(hugeData);
fos.getFD().sync();  // SyncFailedException if disk full

// Cause 3: Filesystem remounted read-only due to errors
// (filesystem entered read-only mode after disk errors)
FileOutputStream fos = new FileOutputStream("/mnt/data/file.txt");
fos.write(data);
fos.getFD().sync();  // SyncFailedException

// Cause 4: Network filesystem timeout
FileOutputStream fos = new FileOutputStream("/mnt/nfs/data.txt");
fos.write(data);
fos.getFD().sync();  // SyncFailedException if NFS server unreachable

// Cause 5: USB drive removed during sync
FileOutputStream fos = new FileOutputStream("/media/usb/log.txt");
fos.write(data);
fos.getFD().sync();  // SyncFailedException if device disconnected
```

## Solutions

### Fix 1: Catch and handle SyncFailedException gracefully

```java
try (FileOutputStream fos = new FileOutputStream("data.txt")) {
    fos.write(data);
    fos.getFD().sync();
} catch (SyncFailedException e) {
    logger.warn("Could not sync to disk: " + e.getMessage());
    // Data may not be durable — log warning or retry
} catch (IOException e) {
    logger.error("I/O error during write/sync", e);
}
```

### Fix 2: Use FileChannel.force() with metadata control

```java
try (FileChannel channel = FileChannel.open(path,
        StandardOpenOption.WRITE, StandardOpenOption.CREATE)) {
    channel.write(ByteBuffer.wrap(data));
    // force(true) = sync data + metadata; force(false) = sync data only
    channel.force(true);
} catch (SyncFailedException e) {
    logger.warn("Sync failed, data may not be durable: " + e.getMessage());
} catch (IOException e) {
    logger.error("Write or force failed", e);
}
```

### Fix 3: Check disk space before writing and syncing

```java
import java.nio.file.FileStore;

FileStore store = Files.getFileStore(path);
long available = store.getUsableSpace();
long free = store.getUnallocatedSpace();

if (available < data.length) {
    throw new IOException("Insufficient disk space: " + available + " bytes available");
}

try (FileChannel channel = FileChannel.open(path,
        StandardOpenOption.WRITE, StandardOpenOption.CREATE)) {
    channel.write(ByteBuffer.wrap(data));
    channel.force(true);
}
```

### Fix 4: Retry sync with exponential backoff

```java
public static void syncWithRetry(FileDescriptor fd, int maxRetries) throws IOException {
    int delay = 100;
    for (int i = 0; i < maxRetries; i++) {
        try {
            fd.sync();
            return;
        } catch (SyncFailedException e) {
            if (i == maxRetries - 1) throw e;
            try {
                Thread.sleep(delay);
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
                throw new IOException("Sync interrupted", ie);
            }
            delay *= 2;
        }
    }
}
```

### Fix 5: Use FileChannel as alternative to FileDescriptor.sync()

```java
// FileChannel.force() provides more control than FileDescriptor.sync()
try (RandomAccessFile raf = new RandomAccessFile("data.txt", "rw");
     FileChannel channel = raf.getChannel()) {
    channel.write(ByteBuffer.wrap(data));
    channel.force(false);  // sync data only, skip metadata
}
```

## Prevention Checklist

- Always handle `SyncFailedException` when calling `sync()` or `force()`.
- Check disk space before performing sync-critical writes.
- Use `FileChannel.force()` instead of `FileDescriptor.sync()` for more control.
- Implement retry logic for transient sync failures on network filesystems.
- Verify storage device health before critical write operations.

## Related Errors

- [IOException](../ioexception) — parent class for all I/O failures.
- [FileNotFoundException](../filenotfoundexception) — file not accessible before sync.
- [AccessDeniedException](../accessdeniedexception) — insufficient permissions for file operations.
