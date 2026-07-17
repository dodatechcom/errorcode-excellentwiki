---
title: "RangeError - index out of range"
description: "Dart throws RangeError when accessing a list or string index that is outside the valid range"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dart", "range", "index", "list", "string", "bounds"]
weight: 5
---

A RangeError occurs when you try to access a list element, string character, or other indexed collection at a position that does not exist. The index must be between 0 and length-1 (for positive indices).

## Common Causes

- Accessing a list element at an index >= list length
- Off-by-one errors in loop conditions
- Empty list access without checking length
- Using -1 as an index (not valid for direct access)
- Dynamically calculated index exceeding bounds

## How to Fix

1. Check index bounds before accessing:

```dart
final items = [1, 2, 3];

if (index >= 0 && index < items.length) {
  final item = items[index];
} else {
  // handle out of bounds
}
```

2. Use safe access methods:

```dart
// Use elementAtOrNull (Dart 3+)
final item = items.elementAtOrNull(index);

// Or use firstWhere with orElse
final item = items.where((e) => e.id == targetId).firstOrNull;
```

3. Use `clamp` to restrict index to valid range:

```dart
final safeIndex = index.clamp(0, items.length - 1);
final item = items[safeIndex];
```

4. Check list empties before accessing:

```dart
if (items.isNotEmpty) {
  final first = items.first;
  final last = items.last;
}
```

5. Handle negative or zero-length lists:

```dart
final first = items.isNotEmpty ? items[0] : null;
```

## Examples

```dart
// Error: RangeError (index): Invalid value: Not in inclusive range 0..2: 3
final list = [10, 20, 30];
print(list[3]); // index 3 doesn't exist

// Fix: check bounds
if (list.length > 3) {
  print(list[3]);
}

// Or use safe access
print(list.elementAtOrNull(3)); // returns null
```

```dart
// Error on empty list
final emptyList = <int>[];
print(emptyList[0]); // RangeError: No element

// Fix: check if empty
if (emptyList.isNotEmpty) {
  print(emptyList[0]);
}
```

## Related Errors

- [Type error]({{< relref "/frameworks/flutter/flutter-dart-type-error" >}})
- [Null error]({{< relref "/frameworks/flutter/flutter-dart-null-error" >}})
