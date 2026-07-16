---
title: "RangeError: Index out of range"
description: "A RangeError occurs when accessing a list or string with an index outside its valid bounds."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["range", "index", "out-of-bounds", "dart"]
weight: 5
---

## What This Error Means

A `RangeError` is thrown when you try to access an element of a list, string, or other indexed collection using an index that is outside the valid range (less than 0 or greater than/equal to the length).

## Common Causes

- Off-by-one errors in loops
- Accessing empty collections
- Using computed indices without bounds check
- Wrong index calculation

## How to Fix

```dart
// WRONG: Accessing beyond bounds
List<int> list = [1, 2, 3];
int x = list[3];  // RangeError

// CORRECT: Check bounds first
List<int> list = [1, 2, 3];
if (list.isNotEmpty && list.length > 3) {
  int x = list[3];
}
```

```dart
// WRONG: Using first/last on empty list
List<int> empty = [];
int first = empty.first;  // StateError (similar to RangeError)

// CORRECT: Check if empty
List<int> empty = [];
if (empty.isNotEmpty) {
  int first = empty.first;
}
```

## Examples

```dart
// Example 1: Off by one
var list = [1, 2, 3];
print(list[list.length]);  // RangeError

// Example 2: Negative index
print(list[-1]);  // RangeError

// Example 3: String index
String str = "hello";
print(str[10]);  // RangeError
```

## Related Errors

- [type cast error](/languages/dart/type-cast-error)
- [StateError: No element](/languages/dart/state-error4)
