---
title: "[Solution] Java ArrayIndexOutOfBoundsException — using negative computed values as array indices"
description: "Fix Java ArrayIndexOutOfBoundsException when using negative computed values as array indices with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayIndexOutOfBoundsException — using negative computed values as array indices

A `ArrayIndexOutOfBoundsException` occurs when int idx = calculateIndex();  // returns -1
String s = arr[idx];  // AIOOBE.

## Common Causes

```java
int idx = calculateIndex();  // returns -1
String s = arr[idx];  // AIOOBE
```

## Solutions

```java
// Fix: validate index
int idx = calculateIndex();
if (idx >= 0 && idx < arr.length) { String s = arr[idx]; }

// Fix: safe get
public static <T> T safeGet(T[] arr, int idx, T def) {
    return (idx >= 0 && idx < arr.length) ? arr[idx] : def;
}
```

## Prevention Checklist

- Validate computed indices are non-negative.
- Use Math.max(0, idx) to clamp.
- Test edge cases with negative values.

## Related Errors

ArrayIndexOutOfBoundsException, NegativeArraySizeException
