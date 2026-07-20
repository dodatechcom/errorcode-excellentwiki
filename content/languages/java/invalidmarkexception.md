---
title: "[Solution] Java InvalidMarkException — NIO Buffer Mark Fix"
description: "Fix Java InvalidMarkException by checking mark is set before reset(), avoiding overwriting marks, and using position tracking instead."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# InvalidMarkException — NIO Buffer Mark Fix

An `InvalidMarkException` is thrown when the `reset()` method is called on a buffer whose mark has not been set or has been invalidated. The mark is invalidated when the buffer's position is set to a value less than the mark's position.

## Description

`java.nio.InvalidMarkException` is an unchecked exception extending `java.lang.IllegalStateException`. Every NIO buffer (`ByteBuffer`, `CharBuffer`, etc.) maintains a mark that records a specific position. The mark becomes invalid when:

- `reset()` is called before `mark()` has been invoked
- The buffer's position is moved to a value less than the mark (e.g., via `rewind()`, `clear()`, `flip()`, or `position(n)` where `n < mark`)
- `mark()` is never called after the buffer is created

Common message variants:

- `java.nio.InvalidMarkException`

## Common Causes

```java
// Cause 1: Calling reset() without calling mark() first
ByteBuffer buffer = ByteBuffer.allocate(100);
buffer.get(new byte[50]);
buffer.reset();  // InvalidMarkException — mark was never set

// Cause 2: Clearing the buffer after marking
ByteBuffer buffer = ByteBuffer.allocate(100);
buffer.position(10);
buffer.mark();
buffer.clear();       // Invalidates mark (position set to 0 < mark position)
buffer.position(10);
buffer.reset();       // InvalidMarkException

// Cause 3: Flipping invalidates mark
ByteBuffer buffer = ByteBuffer.allocate(100);
buffer.position(20);
buffer.mark();
buffer.flip();        // Invalidates mark
buffer.reset();       // InvalidMarkException

// Cause 4: Rewinding invalidates mark
ByteBuffer buffer = ByteBuffer.allocate(100);
buffer.position(30);
buffer.mark();
buffer.rewind();      // Invalidates mark (position set to 0)
buffer.reset();       // InvalidMarkException
```

## Solutions

### Fix 1: Always call mark() before reset()

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
buffer.position(10);
buffer.mark();       // Set mark at position 10
buffer.position(50);
buffer.reset();      // Returns to position 10 — no exception
```

### Fix 2: Track position manually instead of relying on mark

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
int savedPosition = buffer.position();  // Manual position tracking

buffer.position(100);
// Do work...

buffer.position(savedPosition);  // Restore position without using mark/reset
```

### Fix 3: Use duplicate() to preserve mark across operations

```java
ByteBuffer buffer = ByteBuffer.allocate(1024);
buffer.position(20);
buffer.mark();

// Duplicate shares content but has independent position/mark
ByteBuffer duplicate = buffer.duplicate();
duplicate.position(50);
duplicate.reset();   // Works — duplicate's mark is at position 20
```

### Fix 4: Guard reset() with a validity check pattern

```java
public static void safeReset(ByteBuffer buffer) {
    try {
        buffer.reset();
    } catch (InvalidMarkException e) {
        // Mark was not set or was invalidated
        // Fall back to position(0) or handle accordingly
        buffer.position(0);
    }
}
```

## Prevention Checklist

- Always call `mark()` before `reset()` on any buffer.
- Be aware that `clear()`, `flip()`, `rewind()`, and `position(n)` with `n < mark` invalidate the mark.
- Prefer manual position tracking for complex buffer operations.
- Use `duplicate()` when you need independent position/mark state per thread.
- Review buffer lifecycle when using mark/reset across multiple operations.

## Related Errors

- [BufferOverflowException](../bufferoverflowexception) — write exceeds buffer capacity.
- [BufferUnderflowException](../bufferunderflowexception) — read when no bytes available.
- [IndexOutOfBoundsException](../indexoutofboundsexception) — invalid position, limit, or capacity.
