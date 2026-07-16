---
title: "FormatException: Invalid format"
description: "A FormatException occurs when attempting to parse a string that doesn't match the expected format."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["format", "parse", "invalid", "dart"]
weight: 5
---

## What This Error Means

A `FormatException` is thrown when you try to parse a string into a number (int, double) or other format, but the string doesn't contain a valid representation of the target type.

## Common Causes

- Parsing non-numeric string as number
- Wrong date/time format
- Invalid URL or email format
- Missing required format elements

## How to Fix

```dart
// WRONG: Parsing invalid string
int n = int.parse("hello");  // FormatException

// CORRECT: Use tryParse for safe parsing
int? n = int.tryParse("hello");
if (n != null) {
  print(n);
} else {
  print("Invalid number");
}
```

```dart
// WRONG: Not handling parse errors
double d = double.parse("abc.def");  // FormatException

// CORRECT: Use tryParse with default
double d = double.tryParse("abc.def") ?? 0.0;
```

## Examples

```dart
// Example 1: Integer parse
int.parse("12.34");  // FormatException

// Example 2: Double parse
double.parse("not a number");  // FormatException

// Example 3: DateTime parse
DateTime.parse("2024-13-45");  // FormatException
```

## Related Errors

- [type cast error](/languages/dart/type-cast-error)
- [RangeError: Index out of range](/languages/dart/range-error)
