---
title: "[Solution] Dart Map Insert Error — putIfAbsent, update, Concurrent Modification"
description: "Fix Dart Map errors from putIfAbsent, update, updateAll, and concurrent modification during iteration."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 103
---

Map insert errors happen when modifying a map while iterating over it, misusing `putIfAbsent`/`update`, or expecting `[]` to insert values for missing keys.

## Common Causes

1. Adding or removing entries while iterating with `for-in` or `forEach`.
2. `update` called on a key that does not exist without a fallback.
3. `putIfAbsent` callback returning `null` for a non-nullable map.
4. `[]` operator returning `null` for missing keys in non-nullable typed maps.
5. Using `map[key] = value` inside `updateAll` causing inconsistent state.

## How to Fix It

**Solution 1: Avoid concurrent modification — iterate on a copy**

```dart
void main() {
  Map<String, int> scores = {'Alice': 90, 'Bob': 85, 'Charlie': 70};
  
  // Wrong: modifying during iteration
  // for (var key in scores.keys) {
  //   if (scores[key]! < 80) scores.remove(key); // ConcurrentModificationError
  // }
  
  // Correct: iterate on a snapshot
  for (var key in scores.keys.toList()) {
    if (scores[key]! < 80) scores.remove(key);
  }
  print(scores); // {Alice: 90, Bob: 85}
}
```

**Solution 2: Use `putIfAbsent` correctly**

```dart
void main() {
  Map<String, List<String>> groups = {};
  
  groups.putIfAbsent('admin', () => []);
  groups['admin']!.add('Alice');
  groups.putIfAbsent('admin', () => []); // Does not overwrite
  groups['admin']!.add('Bob');
  
  print(groups); // {admin: [Alice, Bob]}
}
```

**Solution 3: Use `update` with a fallback for missing keys**

```dart
void main() {
  Map<String, int> counter = {'a': 1, 'b': 2};
  
  // This throws if key 'c' does not exist
  // counter.update('c', (v) => v + 1);
  
  // Use updateValue to provide a default
  counter.update('c', (v) => v + 1, ifAbsent: () => 1);
  print(counter); // {a: 1, b: 2, c: 1}
}
```

**Solution 4: Use `updateAll` safely**

```dart
void main() {
  Map<String, int> prices = {'apple': 100, 'banana': 50, 'cherry': 200};
  
  prices.updateAll((key, value) => (value * 1.1).toInt());
  print(prices); // {apple: 110, banana: 55, cherry: 220}
}
```

**Solution 5: Use `??` and `[]=` for conditional insertion**

```dart
void main() {
  Map<String, int> cache = {};
  
  String key = 'data';
  
  // Assign only if not present
  cache[key] ??= expensiveComputation();
  print(cache);
}

int expensiveComputation() => 42;
```

## Examples

The `[]` operator on a `Map` returns `null` (or the default value) for missing keys rather than throwing. Use `map[key]!` only after confirming the key exists to avoid null assertion errors.

## Related Errors

- [Dart Set Error](/languages/dart/dart-set-error/)
- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart JSON Error](/languages/dart/dart-json-error/)
