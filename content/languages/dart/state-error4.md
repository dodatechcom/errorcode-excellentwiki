---
title: "StateError: No element"
description: "A StateError occurs when calling first or last on an empty iterable."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["state", "empty", "no-element", "dart"]
weight: 5
---

## What This Error Means

A `StateError: No element` is thrown when you call `first` or `last` on an empty iterable. These properties require at least one element to exist.

## Common Causes

- Calling first/last on empty list
- Filter returning no results
- Empty collection from database/API
- Missing empty check

## How to Fix

```dart
// WRONG: Calling first on empty list
List<int> empty = [];
int first = empty.first;  // StateError: No element

// CORRECT: Check if empty first
List<int> empty = [];
if (empty.isNotEmpty) {
  int first = empty.first;
}
```

```dart
// WRONG: Using first without checking
var results = list.where((x) => x > 100);
print(results.first);  // StateError if no matches

// CORRECT: Use firstWhere with orElse
var results = list.where((x) => x > 100);
print(results.firstWhere(
  (x) => x > 100,
  orElse: () => -1,
));
```

## Examples

```dart
// Example 1: Empty list
[].first;  // StateError: No element

// Example 2: Empty after filter
[1, 2, 3].where((x) => x > 10).first;  // StateError

// Example 3: Empty set
Set<int> emptySet = {};
emptySet.last;  // StateError: No element
```

## Related Errors

- [RangeError: Index out of range](/languages/dart/range-error)
- [Null check operator used on null](/languages/dart/null-check-error)
