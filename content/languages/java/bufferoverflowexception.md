---
title: "[Solution] Java BufferOverflowException — NIO Buffer Overflow Fix"
description: "Fix Java BufferOverflowException by checking remaining capacity, flipping buffers before reading, compacting buffers, and increasing buffer size."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# BufferOverflowException — NIO Buffer Overflow Fix

A `BufferOverflowException` is thrown when a relative put operation attempts to write data beyond the buffer's limit. This occurs when the buffer's remaining capacity (`limit - position`) is insufficient for the data being written.

## Description

`java.nio.BufferOverflowException` is an unchecked exception thrown by buffer's relative put methods when there is insufficient space between the position and limit. It extends `java.lang.IllegalStateException`.

Common message variants:

- `java.nio.BufferOverflowException`
- `Buffer overflow (attempted to write X bytes into a Y-byte buffer)`

This exception is specific to `java.nio` buffer classes such as `ByteBuffer`, `CharBuffer`, `IntBuffer`, and their variants.

## Common Causes

```java
// Cause 1: Writing more data than remaining capacity
ByteBuffer buffer = ByteBuffer.allocate(10);
buffer.put(new byte[20]);  // BufferOverflowException

// Cause 2: Not flipping buffer before writing to a second channel
ByteBuffer buffer = ByteBuffer.allocate(1024);
channel.read(buffer);  // Fills buffer
channel.write(buffer);  // BufferOverflowException — position is at end, not flipped

// Cause 3: Reusing buffer without clearing or compacting
ByteBuffer buffer = ByteBuffer.allocate(100);
buffer.put(data);
// Missing buffer.clear() or buffer.compact()
buffer.put(moreData);  // BufferOverflowException if buffer was full

// Cause 4: Mismatched buffer and data sizes
ByteBuffer buffer = ByteBuffer.allocate(32);
String longString = "This string is definitely longer than 32 bytes";
buffer.put(longString.getBytes(StandardCharsets.UTF_8));  // BufferOverflowException
```

## Solutions

### Fix 1: Check remaining capacity before writing

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
byte[] data = getData();

if (data.length > buffer.remaining()) {
    buffer.flip();
    // Process or flush existing data
    buffer.clear();
}

buffer.put(data);
```

### Fix 2: Flip the buffer before reading from it

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
channel.read(buffer);  // Write into buffer

// Must flip before reading from the buffer
buffer.flip();
channel.write(buffer);  // Now works correctly

buffer.clear();  // Ready for next read
```

### Fix 3: Compact the buffer to retain unread data and free space

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
channel.read(buffer);

// Some data was partially read — compact retains unread bytes
buffer.compact();

// Now position is after unread data, limit is at capacity
channel.read(buffer);  // Continues reading without losing data
```

### Fix 4: Use a dynamically sized buffer or grow as needed

```java
public static ByteBuffer ensureCapacity(ByteBuffer buffer, int additionalBytes) {
    if (buffer.remaining() < additionalBytes) {
        ByteBuffer newBuffer = ByteBuffer.allocate(
            Math.max(buffer.capacity() * 2, buffer.position() + additionalBytes)
        );
        buffer.flip();
        newBuffer.put(buffer);
        return newBuffer;
    }
    return buffer;
}
```

## Prevention Checklist

- Always check `buffer.remaining()` before calling `put()` or `write()`.
- Call `flip()` after writing to a buffer and before reading from it.
- Call `clear()` or `compact()` after reading to prepare for the next write.
- Pre-calculate buffer sizes when the data size is known in advance.
- Use try-with-resources to ensure buffers associated with channels are handled properly.

## Related Errors

- [BufferUnderflowException](../bufferunderflowexception) — read operation when no bytes are available.
- [ClosedChannelException](../closedchannelexception) — I/O operation on a closed channel.
- [IndexOutOfBoundsException](../indexoutofboundsexception) — array index out of bounds.
