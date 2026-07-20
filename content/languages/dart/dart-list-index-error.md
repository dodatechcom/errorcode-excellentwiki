---
title: "[Solution] Dart List Index Error — RangeError: Index Out of Bounds"
description: "Fix Dart RangeError when accessing a List index out of bounds. Learn about growable vs fixed lists, sublist ranges, and safe index access patterns."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 100
---

A `RangeError` is thrown when you access a `List` index that is negative or greater than or equal to the list's length. This is one of the most common runtime errors in Dart.

## Common Causes

1. Accessing an index that does not exist in the list.
2. Off-by-one errors when iterating with `for` loops.
3. Using `sublist` with out-of-range start or end parameters.
4. Accessing elements of a fixed-length list after removing items without recreating the list.
5. Passing a negative index to `operator []`.

## How to Fix It

**Solution 1: Check the index before accessing**

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];

void printFruit(int index) {
  if (index >= 0 && index < fruits.length) {
    print(fruits[index]);
  } else {
    print('Index $index is out of range');
  }
}

void main() {
  printFruit(1);  // banana
  printFruit(5);  // Index 5 is out of range
}
```

**Solution 2: Use the safe `[]` null-aware pattern**

```dart
List<int> numbers = [10, 20, 30];
int? value = numbers.length > 2 ? numbers[2] : null;
print(value); // 30
```

**Solution 3: Use `sublist` with validated bounds**

```dart
void main() {
  List<int> data = [0, 1, 2, 3, 4];
  
  int start = 1;
  int end = 4;
  
  if (start >= 0 && end <= data.length && start <= end) {
    print(data.sublist(start, end)); // [1, 2, 3]
  } else {
    print('Invalid sublist range');
  }
}
```

**Solution 4: Use growable lists and understand fixed-length behavior**

```dart
void main() {
  // Fixed-length list — cannot add/remove
  List<int> fixed = List<int>.filled(3, 0);
  // fixed.add(1); // UnsupportedError

  // Growable list
  List<int> growable = [1, 2, 3];
  growable.add(4);
  growable.removeAt(0);
  print(growable); // [2, 3, 4]
}
```

**Solution 5: Iterate safely with `for-in` or `forEach`**

```dart
void main() {
  List<String> names = ['Alice', 'Bob', 'Charlie'];
  
  for (String name in names) {
    print(name);
  }
  
  names.forEach((name) => print(name));
}
```

## Examples

Accessing `list[-1]` throws a `RangeError`. Instead, use `list.last` or `list[list.length - 1]`. When using `List.generate`, ensure the `growable` parameter is set to `true` if you plan to modify the list later.

## Related Errors

- [Dart Iterable Error](/languages/dart/dart-iterable-error/)
- [Dart Index Error](/languages/dart/dart-index-error/)
- [Dart Set Error](/languages/dart/dart-set-error/)
