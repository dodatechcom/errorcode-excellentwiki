---
title: "[Solution] Java ArrayIndexOutOfBoundsException — Array Bounds Fix"
description: "Fix Java ArrayIndexOutOfBoundsException by validating array indices, checking bounds before access, and using enhanced for-loops for safe iteration."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
tags: ["arrayindexoutofboundsexception", "array", "index", "bounds"]
weight: 5
---

# ArrayIndexOutOfBoundsException — Array Bounds Fix

An `ArrayIndexOutOfBoundsException` is thrown when your code attempts to access an array element using an invalid index — either negative or greater than or equal to the array's length.

## Description

The exception fires the moment you read or write an array element outside its valid range. Common message variants include:

- `ArrayIndexOutOfBoundsException: Index X out of bounds for length Y`
- `ArrayIndexOutOfBoundsException: -1`
- `ArrayIndexOutOfBoundsException: 10`

This is a subclass of `IndexOutOfBoundsException` and always indicates a logic bug.

## Common Causes

```java
// Cause 1: Off-by-one error in a loop
int[] nums = {1, 2, 3};
for (int i = 0; i <= nums.length; i++) {  // <= should be <
    System.out.println(nums[i]);  // AIOOBE when i == 3
}

// Cause 2: Using hardcoded index beyond array length
String[] colors = {"red", "green", "blue"};
String third = colors[3];  // Valid indices are 0, 1, 2

// Cause 3: Negative index
int[] data = {10, 20, 30};
int value = data[-1];  // Negative index

// Cause 4: Index from user input or external data without validation
int index = Integer.parseInt(userInput);
String item = array[index];  // No bounds check
```

## Solutions

### Fix 1: Use `<` instead of `<=` in loops

```java
// Wrong
for (int i = 0; i <= array.length; i++) {
    process(array[i]);
}

// Correct
for (int i = 0; i < array.length; i++) {
    process(array[i]);
}
```

### Fix 2: Use enhanced for-loop to avoid index management

```java
// Wrong
for (int i = 0; i < array.length; i++) {
    System.out.println(array[i]);
}

// Correct — no index to get wrong
for (int item : array) {
    System.out.println(item);
}
```

### Fix 3: Validate index before access

```java
public static <T> T safeGet(T[] array, int index) {
    if (array == null) throw new IllegalArgumentException("array is null");
    if (index < 0 || index >= array.length) {
        throw new IndexOutOfBoundsException(
            "Index " + index + " out of bounds for length " + array.length);
    }
    return array[index];
}
```

### Fix 4: Use `Arrays.asList()` or `List` for dynamic sizing

```java
// Wrong — fixed-size array, easy to overshoot
String[] items = new String[5];
items[5] = "oops";  // AIOOBE

// Correct — List grows automatically
List<String> items = new ArrayList<>();
items.add("a");
items.add("b");  // No bounds issues
```

## Prevention Checklist

- Always use `< array.length` (not `<=`) in loop conditions.
- Prefer enhanced for-loops (`for (T item : array)`) when index is not needed.
- Validate external or user-supplied indices before array access.
- Consider using `List` instead of raw arrays when size is unpredictable.

## Related Errors

- [StringIndexOutOfBoundsException](../stringindexoutofboundsexception) — same bounds violation on String characters.
- [IndexOutOfBoundsException](../indexoutofboundsexception) — parent class for all index-related errors.
- [NullPointerException](../nullpointerexception) — dereferencing a null array reference.
