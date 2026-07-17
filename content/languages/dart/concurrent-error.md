---
title: "Concurrent modification error"
description: "A concurrent modification error occurs when modifying a collection while iterating over it."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `ConcurrentModificationError` is thrown when you modify a collection (add, remove, or clear elements) while iterating over it using a for-in loop or other iterator. This invalidates the iterator.

## Common Causes

- Adding elements during iteration
- Removing elements during for-in loop
- Clearing collection while iterating
- Calling methods that modify the collection

## How to Fix

```dart
// WRONG: Removing during iteration
var list = [1, 2, 3, 4, 5];
for (var item in list) {
  if (item > 3) {
    list.remove(item);  // ConcurrentModificationError
  }
}

// CORRECT: Create new list or use removeWhere
var list = [1, 2, 3, 4, 5];
list.removeWhere((item) => item > 3);
```

```dart
// WRONG: Adding during iteration
var map = {'a': 1, 'b': 2};
for (var key in map.keys) {
  map['c'] = 3;  // ConcurrentModificationError
}

// CORRECT: Modify after iteration
var map = {'a': 1, 'b': 2};
var newEntries = {'c': 3};
map.addAll(newEntries);
```

## Examples

```dart
// Example 1: Remove during for-in
var list = [1, 2, 3];
for (var i in list) {
  if (i == 2) list.remove(i);  // Error
}

// Example 2: Add during iteration
var set = {1, 2, 3};
for (var s in set) {
  set.add(s + 10);  // Error
}

// Example 3: Clear during iteration
var list = [1, 2, 3];
for (var i in list) {
  list.clear();  // Error
}
```

## Related Errors

- [RangeError: Index out of range](/languages/dart/range-error)
- [StateError: No element](/languages/dart/state-error4)
