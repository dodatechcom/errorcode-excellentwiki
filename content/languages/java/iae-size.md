---
title: "[Solution] Java IllegalArgumentException — negative or zero size/capacity passed to constructors"
description: "Fix Java IllegalArgumentException when negative or zero size/capacity passed to constructors with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# IllegalArgumentException — negative or zero size/capacity passed to constructors

A `IllegalArgumentException` occurs when ArrayList<String> list = new ArrayList<>(-1);  // IAE
ByteBuffer buf = ByteBuffer.allocate(-100);  // IAE.

## Common Causes

```java
ArrayList<String> list = new ArrayList<>(-1);  // IAE
ByteBuffer buf = ByteBuffer.allocate(-100);  // IAE
```

## Solutions

```java
// Fix: validate before allocation
int size = calculateSize();
if (size < 0) throw new IAE("Size must be non-negative: "+size);

// Fix: clamp to non-negative
int size = Math.max(0, calculateSize());
ArrayList<String> list = new ArrayList<>(size);
```

## Prevention Checklist

- Validate all size parameters are non-negative.
- Use Math.max(0, size) to clamp.
- Document size constraints in Javadoc.

## Related Errors

NegativeArraySizeException, ArrayIndexOutOfBoundsException
