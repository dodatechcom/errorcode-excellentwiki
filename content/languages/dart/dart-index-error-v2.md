---
title: "[Solution] Dart RangeError Index Out of Range"
description: "Fix Dart RangeError when accessing elements beyond valid indices in lists, strings, and streams."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["range-error", "index", "out-of-range", "list", "runtime", "dart"]
weight: 5
---

## What This Error Means

A `RangeError: Index out of range` error occurs when you access an element at an index that is outside the valid bounds of a list, string, or other indexed collection. Dart uses 0-based indexing.

## Common Causes

- Index exceeds list length
- Off-by-one error in loops
- Accessing empty list
- Substring with invalid range
- Negative index (not allowed)

## How to Fix

```dart
// WRONG: Index exceeds length
List<int> numbers = [1, 2, 3];
print(numbers[3]);  // Error: index 3, length 3

// CORRECT: Check bounds first
if (numbers.length > 3) {
  print(numbers[3]);
}
```

```dart
// WRONG: Off-by-one in loop
List<String> items = ['a', 'b', 'c'];
for (int i = 0; i <= items.length; i++) {
  print(items[i]);  // Error on i = 3
}

// CORRECT: Use < not <=
for (int i = 0; i < items.length; i++) {
  print(items[i]);
}
```

```dart
// WRONG: Accessing empty list
List<int> empty = [];
print(empty[0]);  // Error: index 0, length 0

// CORRECT: Check if empty
if (empty.isNotEmpty) {
  print(empty[0]);
} else {
  print('List is empty');
}
```

```dart
// WRONG: Invalid substring
String text = 'hello';
print(text.substring(10));  // Error: range end out of bounds

// CORRECT: Clamp or check bounds
String safe = text.substring(0, text.length.clamp(0, text.length));
print(safe);
```

## Examples

```dart
void main() {
  // Example 1: Safe list access
  T? safeGet<T>(List<T> list, int index) {
    if (index >= 0 && index < list.length) return list[index];
    return null;
  }
  
  List<int> nums = [10, 20, 30];
  print(safeGet(nums, 1));   // 20
  print(safeGet(nums, 10));  // null
  
  // Example 2: Using firstWhere safely
  List<int> data = [1, 2, 3, 4, 5];
  int? first = data.isNotEmpty ? data.first : null;
  
  // Example 3: Substring with range check
  String safeSubstring(String s, int start, int end) {
    start = start.clamp(0, s.length);
    end = end.clamp(0, s.length);
    if (start >= end) return '';
    return s.substring(start, end);
  }
}
```

## Related Errors

- [dart-null-error]({{< relref "/languages/dart/dart-null-error" >}}) — null check error
- [dart-state-error]({{< relref "/languages/dart/dart-state-error" >}}) — no element in iterable
- [dart-type-error]({{< relref "/languages/dart/dart-type-error" >}}) — type mismatch
