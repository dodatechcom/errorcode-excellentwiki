---
title: "[Solution] Java ArrayIndexOutOfBoundsException — off-by-one in copyOfRange, arraycopy, or subList with out-of-range indices"
description: "Fix Java ArrayIndexOutOfBoundsException when off-by-one in copyofrange, arraycopy, or sublist with out-of-range indices with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayIndexOutOfBoundsException — off-by-one in copyOfRange, arraycopy, or subList with out-of-range indices

A `ArrayIndexOutOfBoundsException` occurs when int[] arr = {1,2,3,4,5};
int[] sub = Arrays.copyOfRange(arr, 2, 6);  // AIOOBE.

## Common Causes

```java
int[] arr = {1,2,3,4,5};
int[] sub = Arrays.copyOfRange(arr, 2, 6);  // AIOOBE
```

## Solutions

```java
// Fix: validate indices
int start = Math.max(0, Math.min(2, arr.length));
int end = Math.max(start, Math.min(5, arr.length));
int[] sub = Arrays.copyOfRange(arr, start, end);

// Fix: streams
List<String> sub = list.stream().skip(2).limit(3).collect(toList());
```

## Prevention Checklist

- Validate slice indices before operations.
- Use Math.min()/max() to clamp.
- Consider streams for safer slicing.

## Related Errors

IndexOutOfBoundsException, NegativeArraySizeException
