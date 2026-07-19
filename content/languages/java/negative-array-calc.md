---
title: "[Solution] Java NegativeArraySizeException — calculated array size is negative due to overflow or wrong formula"
description: "Fix Java NegativeArraySizeException when calculated array size is negative due to overflow or wrong formula with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NegativeArraySizeException — calculated array size is negative due to overflow or wrong formula

A `NegativeArraySizeException` occurs when int size = calculateSize();  // returns -1
int[] arr = new int[size];  // NegativeArraySizeException.

## Common Causes

```java
int size = calculateSize();  // returns -1
int[] arr = new int[size];  // NegativeArraySizeException
```

## Solutions

```java
// Fix: validate before creation
int size = calculateSize();
if (size < 0) throw new IAE("Size must be non-negative: "+size);
int[] arr = new int[size];

// Fix: clamp
int size = Math.max(0, calculateSize());
int[] arr = new int[size];

// Fix: use long for intermediate
long sizeL = (long) width * height;
if (sizeL > Integer.MAX_VALUE) throw new IAE("Array too large");
int[] arr = new int[(int) sizeL];
```

## Prevention Checklist

- Validate calculated sizes are non-negative.
- Use Math.max(0, size) to clamp.
- Use long for intermediate calculations.
- Test with boundary values.

## Related Errors

ArrayIndexOutOfBoundsException, IllegalArgumentException
