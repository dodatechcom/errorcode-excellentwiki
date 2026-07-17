---
title: "[Solution] Dart RangeError - Index Out of Range"
description: "Fix Dart 'RangeError: Index out of range' error. Learn about valid index ranges and safe collection access in Dart."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["range", "index", "array", "list", "collection"]
weight: 5
---

## What This Error Means

A `RangeError` occurs when you try to access an element at an index that is outside the valid range of a list, string, or other indexable collection. Dart collections are zero-indexed.

## Common Causes

- Accessing index equal to or greater than collection length
- Accessing negative index
- Off-by-one error in loops
- Empty collection access
- Incorrect index calculation

## How to Fix

Check index bounds before access:

```dart
List<String> items = ['a', 'b', 'c'];

if (index >= 0 && index < items.length) {
  print(items[index]);
} else {
  print('Index out of bounds');
}
```

Use safe access with `elementAtOrNull`:

```dart
import 'package:collection/collection.dart';

List<String> items = ['a', 'b', 'c'];
String? item = items.elementAtOrNull(5); // Returns null instead of throwing
```

Use proper loop bounds:

```dart
List<int> numbers = [1, 2, 3, 4, 5];

for (int i = 0; i < numbers.length; i++) {
  print(numbers[i]);
}
```

Handle empty collections:

```dart
List<int> numbers = getNumbers();
if (numbers.isNotEmpty) {
  print(numbers.first);
} else {
  print('List is empty');
}
```

## Examples

```dart
void main() {
  List<int> numbers = [10, 20, 30];
  print(numbers[5]); // RangeError: Index out of range
}
```

## Related Errors

- [null-check] — null check operator fails on null
- [type-cast] — invalid type cast
