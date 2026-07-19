---
title: "[Solution] Java ArrayIndexOutOfBoundsException — using <= instead of < with zero-based indices"
description: "Fix Java ArrayIndexOutOfBoundsException when using <= instead of < with zero-based indices with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayIndexOutOfBoundsException — using <= instead of < with zero-based indices

A `ArrayIndexOutOfBoundsException` occurs when for (int i = 0; i <= arr.length; i++) {
    System.out.println(arr[i]);  // AIOOBE when i==length
}.

## Common Causes

```java
for (int i = 0; i <= arr.length; i++) {
    System.out.println(arr[i]);  // AIOOBE when i==length
}
```

## Solutions

```java
// Fix: always use <
for (int i = 0; i < arr.length; i++) { arr[i] = 0; }

// Fix: enhanced for-loop
for (int v : arr) { process(v); }

// Fix: IntStream
IntStream.range(0, arr.length).forEach(i -> process(arr[i]));
```

## Prevention Checklist

- Always use i < array.length.
- Use enhanced for-loops.
- Enable IDE array bounds inspections.

## Related Errors

ArrayIndexOutOfBoundsException, NegativeArraySizeException
