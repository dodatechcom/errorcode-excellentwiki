---
title: "[Solution] Java NegativeArraySizeException — multiplication overflow causes negative size"
description: "Fix Java NegativeArraySizeException when multiplication overflow causes negative size with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NegativeArraySizeException — multiplication overflow causes negative size

A `NegativeArraySizeException` occurs when int rows = 100000;
int cols = 100000;
int[] arr = new int[rows * cols];  // overflow → negative → NegativeArraySizeException.

## Common Causes

```java
int rows = 100000;
int cols = 100000;
int[] arr = new int[rows * cols];  // overflow → negative → NegativeArraySizeException
```

## Solutions

```java
// Fix: check overflow before creation
long size = (long) rows * cols;
if (size > Integer.MAX_VALUE) throw new IAE("Array too large: "+size);
int[] arr = new int[(int) size];

// Fix: use Math.multiplyExact
int[] arr = new int[Math.multiplyExact(rows, cols)];  // throws ArithmeticException on overflow

// Fix: use long throughout
long[] arr = new long[(long) rows * cols];
```

## Prevention Checklist

- Use Math.multiplyExact() for size calculations.
- Check multiplication overflow before array creation.
- Use long for size intermediates.
- Test with large dimension values.

## Related Errors

ArrayIndexOutOfBoundsException, ArithmeticException
