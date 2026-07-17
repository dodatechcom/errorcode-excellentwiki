---
title: "[Solution] Dart StateError No Element in Iterable"
description: "Fix Dart StateError when calling first or single on empty iterables. Handle empty collections safely."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StateError: No element` error occurs when you call `.first`, `.single`, or `.last` on an empty iterable, or use `.singleWhere` when multiple elements match.

## Common Causes

- Calling `.first` on an empty list
- Using `.single` on collection with 0 or 2+ elements
- `.singleWhere` matching multiple elements
- `.firstWhere` without `orElse` on empty collection

## How to Fix

```dart
// WRONG: Calling first on empty list
List<int> numbers = [];
print(numbers.first);  // Error: No element

// CORRECT: Check if empty first
if (numbers.isNotEmpty) {
  print(numbers.first);
} else {
  print('List is empty');
}
```

```dart
// WRONG: firstWhere without orElse
var result = numbers.firstWhere((n) => n > 10);  // Error if none match

// CORRECT: Use orElse for fallback
var result = numbers.firstWhere(
  (n) => n > 10,
  orElse: () => -1,
);
```

```dart
// WRONG: single on multiple elements
List<int> nums = [1, 1, 2];
int single = nums.singleWhere((n) => n == 1);  // Error: 2 matches

// CORRECT: Use where to filter first
int? single = nums.where((n) => n == 1).firstOrNull;
```

## Examples

```dart
void main() {
  // Example 1: Safe single access
  List<int> empty = [];
  List<int> one = [42];
  List<int> many = [1, 2, 3];
  
  int? safeFirst(List<int> list) => list.isNotEmpty ? list.first : null;
  
  print(safeFirst(empty));  // null
  print(safeFirst(one));    // 42
  print(safeFirst(many));   // 1
  
  // Example 2: Using firstOrNull (Dart 3.0+)
  int? result = empty.firstOrNull;
  
  // Example 3: Custom single access
  T? safeSingle<T>(Iterable<T> iter, bool Function(T) test) {
    var matches = iter.where(test).toList();
    if (matches.length == 1) return matches.first;
    return null;
  }
}
```

## Related Errors

- [dart-index-error]({{< relref "/languages/dart/dart-index-error" >}}) — index out of range
- [dart-null-error]({{< relref "/languages/dart/dart-null-error" >}}) — null check error
- [dart-state-error]({{< relref "/languages/dart/dart-state-error" >}}) — state error
