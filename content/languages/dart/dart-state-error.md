---
title: "[Solution] Dart StateError - No Element"
description: "Fix Dart 'StateError: No element' error. Learn when first/last/single are called on empty collections."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `StateError: No element` error occurs when you call `first`, `last`, or `single` on an empty iterable. These getters throw a `StateError` when the collection has no elements.

## Common Causes

- Calling `.first` on an empty list
- Calling `.last` on an empty iterable
- Calling `.single` on collection with != 1 element
- Query returns empty result set
- Stream emits no values before completion

## How to Fix

Check if collection is empty first:

```dart
List<int> numbers = getNumbers();
if (numbers.isNotEmpty) {
  print(numbers.first);
}
```

Use `firstOrNull` from `collection` package:

```dart
import 'package:collection/collection.dart';

List<int> numbers = [];
int? first = numbers.firstOrNull; // Returns null instead of throwing
```

Handle empty results gracefully:

```dart
User? findUser(String email) {
  List<User> users = database.query(email);
  return users.isNotEmpty ? users.first : null;
}
```

Use `elementAtOrNull` for indexed access:

```dart
String? item = list.elementAtOrNull(0); // Safe alternative to .first
```

## Examples

```dart
void main() {
  List<int> emptyList = [];
  print(emptyList.first); // StateError: No element
}
```

## Related Errors

- [null-check] — null check operator fails on null
- [RangeError] — index out of bounds
