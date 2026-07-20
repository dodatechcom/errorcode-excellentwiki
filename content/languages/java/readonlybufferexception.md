---
title: "[Solution] Java ReadOnlyBufferException — Read-Only Buffer Mutation Fix"
description: "Fix Java ReadOnlyBufferException by creating writable buffers, checking isReadOnly(), and using proper buffer views."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ReadOnlyBufferException — Read-Only Buffer Mutation Fix

A `ReadOnlyBufferException` is thrown when an attempt is made to mutate (write to, put, or compact) a read-only NIO buffer. Read-only buffers do not permit any modification of their content.

## Description

`java.nio.ReadOnlyBufferException` extends `IllegalStateException` and is thrown when calling `put()`, `compact()`, `flip()`, `clear()`, or `limit()` on a buffer created as read-only. Common message variants:

- `java.nio.ReadOnlyBufferException`

Read-only buffers are created via `Buffer.asReadOnlyBuffer()` or when wrapping read-only `ByteBuffer` arrays/files.

## Common Causes

```java
// Cause 1: Modifying a buffer obtained from asReadOnlyBuffer()
ByteBuffer readOnly = ByteBuffer.allocate(1024).asReadOnlyBuffer();
readOnly.put((byte) 42);  // ReadOnlyBufferException

// Cause 2: Writing to a read-only file channel mapped buffer
try (FileChannel channel = FileChannel.open(path, StandardOpenOption.READ)) {
    MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0, channel.size());
    buffer.put(0, (byte) 42);  // ReadOnlyBufferException
}

// Cause 3: Wrapping a read-only byte array
byte[] data = new byte[1024];
ByteBuffer buffer = ByteBuffer.wrap(data).asReadOnlyBuffer();
buffer.put((byte) 1);  // ReadOnlyBufferException

// Cause 4: Passing read-only buffer to code that writes
ByteBuffer buffer = receiveFromNetwork();  // Returns read-only buffer
processBuffer(buffer);  // ReadOnlyBufferException if processBuffer calls put()

// Cause 5: Compact or flip on read-only buffer
ByteBuffer readOnly = ByteBuffer.allocate(1024).asReadOnlyBuffer();
readOnly.compact();  // ReadOnlyBufferException
readOnly.flip();     // ReadOnlyBufferException — flip() modifies position
```

## Solutions

### Fix 1: Create a writable copy of the read-only buffer

```java
// Wrong — modifying read-only buffer directly
ByteBuffer readOnly = sourceBuffer.asReadOnlyBuffer();
readOnly.put((byte) 42);  // ReadOnlyBufferException

// Correct — copy to writable buffer
ByteBuffer readOnly = sourceBuffer.asReadOnlyBuffer();
ByteBuffer writable = ByteBuffer.allocate(readOnly.capacity());
writable.put(readOnly);
writable.flip();
writable.put((byte) 42);  // Works
```

### Fix 2: Check isReadOnly() before mutating

```java
public static void safePut(ByteBuffer buffer, byte value) {
    if (buffer.isReadOnly()) {
        throw new IllegalStateException("Cannot write to read-only buffer");
    }
    buffer.put(value);
}

// Usage
if (!buffer.isReadOnly()) {
    buffer.put(data);
} else {
    // Create writable copy first
    ByteBuffer writable = ByteBuffer.allocate(buffer.capacity());
    writable.put(buffer.duplicate());
    writable.put(data);
}
```

### Fix 3: Use duplicate() to create independent position writable copy

```java
ByteBuffer original = ByteBuffer.allocate(1024);
original.put(data);
original.flip();

// Read-only view
ByteBuffer readOnlyView = original.asReadOnlyBuffer();

// Writable copy with independent position
ByteBuffer writableCopy = original.duplicate();
writableCopy.position(0);
writableCopy.put(newData);
```

### Fix 4: Create writable buffer from file instead of read-only mapping

```java
// Wrong — READ_ONLY mapping
try (FileChannel channel = FileChannel.open(path, StandardOpenOption.READ)) {
    MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0, size);
    buffer.put(data);  // ReadOnlyBufferException
}

// Correct — READ_WRITE mapping
try (FileChannel channel = FileChannel.open(path,
        StandardOpenOption.READ, StandardOpenOption.WRITE)) {
    MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_WRITE, 0, size);
    buffer.put(data);  // Works
}
```

### Fix 5: Clone buffer before passing to write-capable methods

```java
public ByteBuffer ensureWritable(ByteBuffer buffer) {
    if (buffer.isReadOnly()) {
        ByteBuffer writable = ByteBuffer.allocate(buffer.capacity());
        writable.put(buffer.duplicate());
        writable.flip();
        return writable;
    }
    return buffer;
}

// Usage
ByteBuffer input = receiveData();  // May be read-only
ByteBuffer safeBuffer = ensureWritable(input);
safeBuffer.put(updateBytes);
```

## Prevention Checklist

- Always check `buffer.isReadOnly()` before calling `put()`, `compact()`, or `flip()`.
- Create writable copies when working with buffers from external sources.
- Use `duplicate()` for independent-position copies and `asReadOnlyBuffer()` for read-only views.
- Use `FileChannel.MapMode.READ_WRITE` when you need to modify file-mapped buffers.
- Document buffer mutability in method contracts.

## Related Errors

- [BufferOverflowException](../bufferoverflowexception) — writing beyond buffer capacity.
- [BufferUnderflowException](../bufferunderflowexception) — reading beyond buffer limit.
- [NonWritableChannelException](../nonwritablechannelexception) — writing to read-only channel.
