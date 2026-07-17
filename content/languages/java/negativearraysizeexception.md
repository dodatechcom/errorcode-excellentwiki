---
title: "[Solution] Java NegativeArraySizeException — Array Size Fix"
description: "Fix Java NegativeArraySizeException by validating array size before allocation, handling negative computed sizes, and using proper bounds checking."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# NegativeArraySizeException — Array Size Fix

A `NegativeArraySizeException` is thrown when an attempt is made to create an array with a negative size. This is a subclass of `RuntimeException` and indicates a logic error in computing the array size.

## Description

Java arrays cannot have negative lengths. When you use the `new` keyword to create an array with a negative size expression, the JVM throws this exception at runtime.

## Common Causes

```java
// Cause 1: Negative size from computation
int size = 10 - 20;
int[] arr = new int[size];  // NegativeArraySizeException: -10

// Cause 2: Negative size from user input
int count = Integer.parseInt(userInput);
String[] items = new String[count];  // if count is negative

// Cause 3: Signed integer overflow
int size = Integer.MAX_VALUE + 1;  // wraps to Integer.MIN_VALUE
int[] arr = new int[size];  // NegativeArraySizeException

// Cause 4: Negative result from collection size
List<String> list = new ArrayList<>();
list.add("a");
int[] arr = new int[list.size() - 5];  // size is -4
```

## Solutions

```java
// Fix 1: Validate size before allocation
int size = computeSize();
if (size < 0) {
    throw new IllegalArgumentException("Array size cannot be negative: " + size);
}
int[] arr = new int[size];

// Fix 2: Use Math.max to enforce minimum size
int size = computeSize();
int[] arr = new int[Math.max(0, size)];

// Fix 3: Check for integer overflow in size computation
int size = a - b;
if (size < 0) {
    size = 0;  // or throw exception
}
int[] arr = new int[size];

// Fix 4: Safe array allocation helper
public static <T> T[] safeArray(Class<T> clazz, int size) {
    if (size < 0) {
        throw new IllegalArgumentException("Cannot create array with negative size: " + size);
    }
    return java.lang.reflect.Array.newInstance(clazz, size);
}
```

## Examples

```java
// This triggers NegativeArraySizeException
public class DataProcessor {
    public byte[] processData(int expectedSize, int headerSize) {
        int dataSize = expectedSize - headerSize;
        return new byte[dataSize];  // NegativeArraySizeException if header > expected
    }
}

// Usage
DataProcessor processor = new DataProcessor();
byte[] data = processor.processData(100, 200);  // size = -100
```

## Related Exceptions

- [ArrayIndexOutOfBoundsException](../arrayindexoutofboundsexception) — index outside array bounds
- [OutOfMemoryError]({{< relref "/languages/java/outofmemoryerror" >}}) — array too large for available memory
- [IllegalArgumentException](../illegalargumentexception) — invalid method argument
