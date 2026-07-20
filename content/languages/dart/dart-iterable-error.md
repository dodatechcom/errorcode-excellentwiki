---
title: "[Solution] Dart Iterable Error — single/whereType/cast/reduce Misuse"
description: "Fix Dart Iterable errors from single(), whereType, cast, expand, and reduce. Understand lazy evaluation and Iterable contract violations."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 101
---

`Iterable` errors occur when calling methods that have strict preconditions on the iterable's contents, such as `single()`, `reduce()`, or `first` on an empty iterable.

## Common Causes

1. Calling `single()` on an iterable with zero or multiple elements.
2. Calling `reduce()` on an empty iterable without an initial value.
3. `whereType` returns no results but code assumes at least one match.
4. `cast()` fails because the iterable contains an element of the wrong type.
5. `expand` callback returns null or a non-iterable value.

## How to Fix It

**Solution 1: Check length before calling `single()`**

```dart
void main() {
  List<int> nums = [42];
  
  // Unsafe
  // int value = nums.single; // throws if length != 1
  
  // Safe
  if (nums.length == 1) {
    print(nums.single); // 42
  } else {
    print('Expected exactly one element, got ${nums.length}');
  }
}
```

**Solution 2: Provide an initial value to `reduce()`**

```dart
void main() {
  List<int> numbers = [1, 2, 3, 4];
  
  // Safe reduce with initial value using fold
  int sum = numbers.fold(0, (prev, element) => prev + element);
  print(sum); // 10
  
  // Empty list is safe with fold
  List<int> empty = [];
  int emptySum = empty.fold(0, (prev, element) => prev + element);
  print(emptySum); // 0
}
```

**Solution 3: Validate `whereType` results**

```dart
void main() {
  List<dynamic> mixed = [1, 'hello', 3.14, true];
  
  List<String> strings = mixed.whereType<String>().toList();
  
  if (strings.isNotEmpty) {
    print('Found strings: $strings');
  } else {
    print('No strings found');
  }
}
```

**Solution 4: Use safe `cast` with `try-catch`**

```dart
void main() {
  Iterable<dynamic> items = [1, 2, 3];
  
  try {
    Iterable<int> ints = items.cast<int>();
    print(ints.toList());
  } on TypeError catch (e) {
    print('Cast failed: $e');
  }
}
```

**Solution 5: Handle `expand` edge cases**

```dart
void main() {
  List<String> words = ['hello', 'world'];
  
  List<String> expanded = words.expand((word) => word.split('')).toList();
  print(expanded); // [h, e, l, l, o, w, o, r, l, d]
  
  // Returning empty iterable from expand is valid
  List<int> nums = [1, 2, 3];
  List<int> evens = nums.expand((n) => n.isEven ? [n] : []).toList();
  print(evens); // [2]
}
```

## Examples

`Iterable` is lazy — calling `where()` or `map()` does not evaluate until you call `toList()` or iterate. This means errors in chained transforms may surface far from the original call.

## Related Errors

- [Dart List Index Error](/languages/dart/dart-list-index-error/)
- [Dart Set Error](/languages/dart/dart-set-error/)
- [Dart Generic Error](/languages/dart/dart-generics-error/)
