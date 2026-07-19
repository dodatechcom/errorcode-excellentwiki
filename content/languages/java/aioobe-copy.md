---
title: "[Solution] Java ArrayIndexOutOfBoundsException — srcPos+length or destPos+length exceeds array bounds"
description: "Fix Java ArrayIndexOutOfBoundsException when srcpos+length or destpos+length exceeds array bounds with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ArrayIndexOutOfBoundsException — srcPos+length or destPos+length exceeds array bounds

A `ArrayIndexOutOfBoundsException` occurs when int[] src = {1,2,3};
int[] dest = new int[2];
System.arraycopy(src, 0, dest, 0, 3);  // AIOOBE.

## Common Causes

```java
int[] src = {1,2,3};
int[] dest = new int[2];
System.arraycopy(src, 0, dest, 0, 3);  // AIOOBE
```

## Solutions

```java
// Fix: calculate safe length
int safeLen = Math.min(src.length - srcPos, dest.length - destPos);
System.arraycopy(src, srcPos, dest, destPos, safeLen);

// Fix: validate all params
Objects.checkFromToIndex(srcPos, srcPos+length, src.length);
Objects.checkFromToIndex(destPos, destPos+length, dest.length);
System.arraycopy(src, srcPos, dest, destPos, length);
```

## Prevention Checklist

- Validate srcPos+length <= src.length and destPos+length <= dest.length.
- Use Math.min() for safe copy length.
- Use Objects.checkFromToIndex() (Java 9+).

## Related Errors

ArrayIndexOutOfBoundsException, IndexOutOfBoundsException
