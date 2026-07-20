---
title: "[Solution] Java BufferUnderflowException — NIO Buffer Underflow Fix"
description: "Fix Java BufferUnderflowException by checking hasRemaining(), filling the buffer before reading, and using absolute get operations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# BufferUnderflowException — NIO Buffer Underflow Fix

A `BufferUnderflowException` is thrown when a relative get operation is attempted on a buffer when no bytes are available — that is, when the buffer's position is at or beyond its limit.

## Description

`java.nio.BufferUnderflowException` is an unchecked exception extending `java.lang.IllegalStateException`. It occurs during read operations when the buffer is empty (position >= limit) and a relative get is called.

Common message variants:

- `java.nio.BufferUnderflowException`
- `Buffer underflow (attempted to read X bytes from a Y-byte buffer with Z bytes remaining)`

This affects all NIO buffer types: `ByteBuffer`, `CharBuffer`, `IntBuffer`, `LongBuffer`, `ShortBuffer`, `DoubleBuffer`, and `FloatBuffer`.

## Common Causes

```java
// Cause 1: Reading from an empty buffer
ByteBuffer buffer = ByteBuffer.allocate(10);
buffer.get();  // BufferUnderflowException — position == limit == 0

// Cause 2: Not flipping before reading
ByteBuffer buffer = ByteBuffer.allocate(1024);
buffer.put(data);  // position is at end of data
buffer.get();      // BufferUnderflowException — need to flip first

// Cause 3: Reading more bytes than available
ByteBuffer buffer = ByteBuffer.allocate(5);
buffer.put(new byte[]{1, 2, 3});
buffer.flip();
byte[] dest = new byte[10];
buffer.get(dest);  // BufferUnderflowException — only 3 bytes available

// Cause 4: Reusing buffer without resetting position
ByteBuffer buffer = ByteBuffer.wrap(new byte[]{1, 2, 3, 4, 5});
buffer.get(new byte[5]);  // Reads all 5 bytes
buffer.get();             // BufferUnderflowException — already consumed
```

## Solutions

### Fix 1: Check hasRemaining() before reading

```java
ByteBuffer buffer = getBuffer();

while (buffer.hasRemaining()) {
    byte b = buffer.get();
    processByte(b);
}
```

### Fix 2: Flip the buffer after writing and before reading

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
channel.read(buffer);    // Write data into buffer

buffer.flip();           // Switch from write to read mode
channel.write(buffer);   // Read data from buffer

buffer.clear();          // Reset for next cycle
```

### Fix 3: Use absolute get with bounds checking

```java
ByteBuffer buffer = getBuffer();
int bytesToRead = 10;

if (buffer.remaining() >= bytesToRead) {
    byte[] dest = new byte[bytesToRead];
    buffer.get(dest);
} else {
    // Handle partial read
    byte[] dest = new byte[buffer.remaining()];
    buffer.get(dest);
}
```

### Fix 4: Fill buffer before consuming data

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
int bytesRead = channel.read(buffer);

if (bytesRead == -1) {
    // End of stream
    return;
}

buffer.flip();
// Now safely read from buffer
byte[] data = new byte[buffer.remaining()];
buffer.get(data);
```

## Prevention Checklist

- Always call `flip()` after writing data to a buffer and before reading from it.
- Check `buffer.hasRemaining()` before every relative get operation.
- Reset the buffer with `clear()` or `compact()` after reading to prepare for reuse.
- Use absolute get methods when you know the exact position to read from.
- Verify channel read returns a positive value before processing buffer contents.

## Related Errors

- [BufferOverflowException](../bufferoverflowexception) — write operation exceeds buffer capacity.
- [ClosedChannelException](../closedchannelexception) — I/O operation on a closed channel.
- [ReadOnlyBufferException](../unsupportedoperationexception) — attempt to modify a read-only buffer.
