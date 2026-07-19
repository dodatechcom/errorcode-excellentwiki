---
title: "[Solution] Java OutOfMemoryError — NIO direct buffers exhaust native memory"
description: "Fix Java OutOfMemoryError when nio direct buffers exhaust native memory with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError — NIO direct buffers exhaust native memory

A `OutOfMemoryError` occurs when ByteBuffer buf = ByteBuffer.allocateDirect(1024*1024);
// if not freed, native memory leaks.

## Common Causes

```java
ByteBuffer buf = ByteBuffer.allocateDirect(1024*1024);
// if not freed, native memory leaks
```

## Solutions

```java
// Fix: set limit
// -XX:MaxDirectMemorySize=256m

// Fix: release
((DirectBuffer) buf).cleaner().clean();

// Fix: pooled buffers (Netty)
ByteBuf buf = PooledByteBufAllocator.DEFAULT.buffer(1024);
try { /* use */ } finally { buf.release(); }

// Fix: heap buffers
byte[] heapBuf = new byte[1024];
```

## Prevention Checklist

- Set -XX:MaxDirectMemorySize.
- Release direct buffers explicitly.
- Use pooled allocators for NIO.
- Monitor with BufferPoolMXBean.

## Related Errors

OutOfMemoryError, IOException
