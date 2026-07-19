---
title: "[Solution] Java IllegalStateException — calling flip, compact, or rewind in wrong state"
description: "Fix Java IllegalStateException when calling flip, compact, or rewind in wrong state with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalStateException — calling flip, compact, or rewind in wrong state

A `IllegalStateException` occurs when ByteBuffer buf = ByteBuffer.allocate(100);
buf.put("hello".getBytes());
buf.flip();
buf.flip();  // ISE or unexpected.

## Common Causes

```java
ByteBuffer buf = ByteBuffer.allocate(100);
buf.put("hello".getBytes());
buf.flip();
buf.flip();  // ISE or unexpected
```

## Solutions

```java
// Fix: track state
if (buf.position() > 0 && !buf.isReadOnly()) { buf.flip(); }
String result = UTF_8.decode(buf).toString();

// Fix: hasRemaining checks
buf.flip();
while (buf.hasRemaining()) { process(buf.get()); }

// Fix: ByteBuffer.wrap for one-time reads
ByteBuffer buf = ByteBuffer.wrap("hello".getBytes());
```

## Prevention Checklist

- Track buffer state carefully.
- Always flip() after writing, before reading.
- Use hasRemaining() checks.

## Related Errors

BufferUnderflowException, ReadOnlyBufferException
