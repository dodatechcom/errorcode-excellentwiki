---
title: "[Solution] Java NonWritableChannelException — NIO Write Permission Fix"
description: "Fix Java NonWritableChannelException by opening channels with WRITE permission, checking channel mode, and using correct open options."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NonWritableChannelException — NIO Write Permission Fix

A `NonWritableChannelException` is thrown when attempting to write to a channel that was not opened for writing. This occurs when a channel is opened without the appropriate write option or mode.

## Description

`java.nio.channels.NonWritableChannelException` is an unchecked exception extending `java.lang.IllegalStateException`. It is thrown by write operations on channels that do not support writing.

This typically happens with:

- `FileChannel` opened with only `StandardOpenOption.READ`
- `SocketChannel` not connected or in read-only mode
- `DatagramChannel` opened without write support

Common message variants:

- `java.nio.channels.NonWritableChannelException`
- `Channel not open for writing`

## Common Causes

```java
// Cause 1: FileChannel opened for reading only
Path path = Paths.get("data.txt");
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ);
ByteBuffer buffer = ByteBuffer.wrap("hello".getBytes());
channel.write(buffer);  // NonWritableChannelException

// Cause 2: Attempting to write to a read-only FileChannel from Files
Path path = Paths.get("input.txt");
try (SeekableByteChannel ch = Files.newByteChannel(path, StandardOpenOption.READ)) {
    ch.write(buffer);  // NonWritableChannelException
}

// Cause 3: Writing to a channel obtained from read-only stream
InputStream is = new FileInputStream("data.txt");
if (is instanceof ReadableByteChannel) {
    ReadableByteChannel rc = (ReadableByteChannel) is;
    // rc is not a WritableByteChannel
    ((WritableByteChannel) rc).write(buffer);  // NonWritableChannelException
}

// Cause 4: Channel opened with CREATE (not CREATE_NEW or TRUNCATE) for existing file
Path path = Paths.get("existing.txt");
FileChannel channel = FileChannel.open(path, StandardOpenOption.CREATE);
channel.write(buffer);  // NonWritableChannelException if CREATE alone doesn't grant write
```

## Solutions

### Fix 1: Open the channel with WRITE permission

```java
// Wrong — only READ permission
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ);

// Correct — include WRITE permission
FileChannel channel = FileChannel.open(path, StandardOpenOption.WRITE);
ByteBuffer buffer = ByteBuffer.wrap("data".getBytes());
channel.write(buffer);
```

### Fix 2: Open for both read and write when needed

```java
FileChannel channel = FileChannel.open(path,
    StandardOpenOption.READ,
    StandardOpenOption.WRITE
);

// Write data
ByteBuffer writeBuffer = ByteBuffer.wrap("hello".getBytes());
channel.write(writeBuffer);

// Read data back
ByteBuffer readBuffer = ByteBuffer.allocate(1024);
channel.read(readBuffer);
```

### Fix 3: Use CREATE with WRITE for new or existing files

```java
Path path = Paths.get("output.txt");
FileChannel channel = FileChannel.open(path,
    StandardOpenOption.CREATE,
    StandardOpenOption.WRITE,
    StandardOpenOption.TRUNCATE_EXISTING
);

ByteBuffer buffer = ByteBuffer.wrap("new content".getBytes());
channel.write(buffer);
```

### Fix 4: Check channel writability before writing

```java
public static int safeWrite(WritableByteChannel channel, ByteBuffer buffer)
        throws IOException {
    if (!channel.isOpen()) {
        throw new IOException("Channel is closed");
    }
    if (channel instanceof FileChannel) {
        // FileChannel doesn't expose writability directly, but we can catch the exception
    }
    return channel.write(buffer);
}
```

## Prevention Checklist

- Always include `StandardOpenOption.WRITE` when opening a `FileChannel` for writing.
- Use `StandardOpenOption.CREATE` or `StandardOpenOption.CREATE_NEW` for new files.
- Verify the channel's open options before performing write operations.
- Document the expected read/write mode of channels passed between methods.

## Related Errors

- [NonReadableChannelException](../nonreadablechannelexception) — read from a non-readable channel.
- [ClosedChannelException](../closedchannelexception) — I/O on a closed channel.
- [AccessDeniedException](../ioexception) — file system permission denied.
