---
title: "[Solution] Java StringIndexOutOfBoundsException — String Bounds Fix"
description: "Fix Java StringIndexOutOfBoundsException by validating char indices, checking string length before substring calls, and using safe string utilities."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StringIndexOutOfBoundsException — String Bounds Fix

A `StringIndexOutOfBoundsException` is thrown when your code attempts to access a character or substring of a `String` using an invalid index — either negative or beyond the string's length.

## Description

The exception fires when you call `charAt()`, `substring()`, or `getChars()` with an index outside the valid range `0` to `length() - 1`. Common message variants include:

- `StringIndexOutOfBoundsException: Range [0, 10) out of bounds for length 5`
- `StringIndexOutOfBoundsException: String index out of range: 10`
- `StringIndexOutOfBoundsException: begin 2, end 5, length 3`

## Common Causes

```java
// Cause 1: Accessing beyond string length
String name = "Java";
char last = name.charAt(4);  // Length is 4, valid indices are 0-3

// Cause 2: Substring with end index exceeding length
String text = "hello";
String sub = text.substring(1, 10);  // end index 10 > length 5

// Cause 3: Hardcoded index without checking length
String code = getUserInput();
char c = code.charAt(5);  // User input may be shorter than expected

// Cause 4: Negative index
String str = "test";
char c = str.charAt(-1);  // Negative index
```

## Solutions

### Fix 1: Check length before accessing by index

```java
// Wrong
char c = str.charAt(index);

// Correct
if (str != null && index >= 0 && index < str.length()) {
    char c = str.charAt(index);
} else {
    // Handle invalid index
}
```

### Fix 2: Use safe substring with bounds clamping

```java
public static String safeSubstring(String str, int begin, int end) {
    if (str == null) return null;
    begin = Math.max(0, begin);
    end = Math.min(str.length(), end);
    if (begin >= end) return "";
    return str.substring(begin, end);
}
```

### Fix 3: Use `Optional` and `Stream` for safe character iteration

```java
// Wrong — may throw if index is bad
for (int i = 0; i <= str.length(); i++) {
    System.out.println(str.charAt(i));
}

// Correct
str.chars()
    .mapToObj(c -> (char) c)
    .forEach(System.out::println);
```

### Fix 4: Validate before `substring` calls

```java
// Wrong
String result = input.substring(start, end);

// Correct
if (input == null || start < 0 || end > input.length() || start > end) {
    throw new IllegalArgumentException("Invalid range: [" + start + ", " + end + ")");
}
String result = input.substring(start, end);
```

## Prevention Checklist

- Always verify `index >= 0 && index < str.length()` before calling `charAt()`.
- Clamp or validate `begin` and `end` indices before calling `substring()`.
- Prefer `str.chars()` or enhanced iteration over index-based character access.
- Use `StringUtils` from Apache Commons for null-safe string operations.

## Related Errors

- [ArrayIndexOutOfBoundsException](../arrayindexoutofboundsexception) — same bounds violation on arrays.
- [IndexOutOfBoundsException](../indexoutofboundsexception) — parent class for all index-related errors.
- [NullPointerException](../nullpointerexception) — calling methods on a null String reference.
