---
title: "[Solution] Dart Set Error — Lookup, Union, Intersection, Hash Contract"
description: "Fix Dart Set errors from lookup failures, union/intersection/difference, and hashCode/equality contract violations."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 102
---

Set errors arise when objects used as set members violate the `hashCode` and `equals` contract, or when set operations produce unexpected results due to custom equality.

## Common Causes

1. Objects overriding `==` without overriding `hashCode` (or vice versa).
2. Expecting `contains()` to work on objects with incorrect equality.
3. Using mutable objects as set members — mutation changes hashCode after insertion.
4. Confusing `Set.difference` semantics with custom equality.
5. Using `LinkedHashSet` vs `SHashSet` expectations incorrectly.

## How to Fix It

**Solution 1: Always override both `==` and `hashCode`**

```dart
class Point {
  final int x;
  final int y;

  Point(this.x, this.y);

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Point && runtimeType == other.runtimeType &&
          x == other.x && y == other.y;

  @override
  int get hashCode => x.hashCode ^ y.hashCode;
}

void main() {
  Set<Point> points = {Point(1, 2), Point(3, 4)};
  print(points.contains(Point(1, 2))); // true
}
```

**Solution 2: Do not mutate set members**

```dart
void main() {
  Set<String> names = {'Alice', 'Bob', 'Charlie'};
  
  // If you need to change a value, remove and re-add
  names.remove('Bob');
  names.add('Bobby');
  print(names); // {Alice, Bobby, Charlie}
}
```

**Solution 3: Use `Set` operations correctly**

```dart
void main() {
  Set<int> a = {1, 2, 3, 4};
  Set<int> b = {3, 4, 5, 6};

  print(a.union(b));        // {1, 2, 3, 4, 5, 6}
  print(a.intersection(b)); // {3, 4}
  print(a.difference(b));   // {1, 2}
}
```

**Solution 4: Use `Set` lookup for O(1) contains checks**

```dart
void main() {
  Set<String> validCodes = {'OK', 'ERROR', 'PENDING'};
  
  String status = 'ERROR';
  
  if (validCodes.contains(status)) {
    print('Valid status: $status');
  }
}
```

**Solution 5: Convert lists to sets to deduplicate**

```dart
void main() {
  List<int> duplicates = [1, 2, 2, 3, 3, 3];
  Set<int> unique = duplicates.toSet();
  print(unique); // {1, 2, 3}
  print(unique.toList()); // [1, 2, 3]
}
```

## Examples

When you store objects in both a `List` and a `Set`, the `Set` uses `hashCode` for bucketing and `==` for collision resolution. If these are inconsistent, lookups silently fail.

## Related Errors

- [Dart List Index Error](/languages/dart/dart-list-index-error/)
- [Dart Iterable Error](/languages/dart/dart-iterable-error/)
- [Dart Map Insert Error](/languages/dart/dart-map-insert-error/)
