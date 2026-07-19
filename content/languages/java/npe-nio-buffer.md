---
title: "[Solution] Java NullPointerException"
description: "NIO Buffer Operations"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# wrapping null arrays in ByteBuffer or wrong buffer state

A `wrapping` is thrown when byte[] data = getdata();.

## Common Causes

```java
byte[] data = getData();
ByteBuffer buffer = ByteBuffer.wrap(data);  // NPE if null
```

## Solutions

```java
// Fix: validate array
byte[] data = getData();
if (data == null || data.length == 0) throw new IAE("null data");
ByteBuffer buffer = ByteBuffer.wrap(data);

// Fix: flip before reading
ByteBuffer buf = ByteBuffer.allocate(1024);
buf.put("hello".getBytes());
buf.flip();
String result = UTF_8.decode(buf).toString();
```

## Prevention Checklist

- Always flip() after writing, before reading.
- Validate byte arrays before wrapping.
- Check hasRemaining() before reading.

## Related Errors

[NullPointerException](nullpointerexception), [BufferUnderflowException](indexoutofboundsexception)
