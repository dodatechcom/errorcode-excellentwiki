---
title: "[Solution] Dart Boolean Error — Bool Conversion, Truthiness, == vs identical"
description: "Fix Dart boolean errors from incorrect truthiness checks, == vs identical usage, and non-bool conditions."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 108
---

Boolean errors occur when Dart's strict type system rejects non-boolean values in conditions, or when `==` and `identical()` produce different results.

## Common Causes

1. Using `if (value)` where `value` is not a `bool` — Dart is not JavaScript.
2. Comparing with `==` instead of `identical()` when checking for `null`.
3. `null` is not truthy or falsy in Dart — it must be handled explicitly.
4. Using `&&`/`||` with non-boolean operands.
5. Overriding `==` incorrectly without considering bool semantics.

## How to Fix It

**Solution 1: Explicit boolean conditions**

```dart
void main() {
  String? name = 'Alice';
  
  // Wrong: Dart requires explicit bool in conditions
  // if (name) { } // Error: Conditions must have a bool type
  
  // Correct
  if (name != null) {
    print('Name: $name');
  }
  
  // For collections
  List<int> items = [1, 2, 3];
  if (items.isNotEmpty) {
    print('Has items');
  }
}
```

**Solution 2: Use `identical()` for identity checks**

```dart
void main() {
  dynamic a = null;
  dynamic b = null;
  
  print(a == b);        // true (null == null is true)
  print(identical(a, b)); // true
  
  String s1 = 'hello';
  String s2 = 'hello';
  print(s1 == s2);        // true (value equality)
  print(identical(s1, s2)); // true (Dart interns small strings)
  
  List<int> l1 = [1, 2];
  List<int> l2 = [1, 2];
  print(l1 == l2);        // false (reference equality for lists)
  print(identical(l1, l2)); // false
}
```

**Solution 3: Use nullable bools carefully**

```dart
void main() {
  bool? nullableBool;
  
  // Wrong
  // if (nullableBool) { }
  
  // Correct
  if (nullableBool == true) {
    print('True');
  } else if (nullableBool == false) {
    print('False');
  } else {
    print('Null');
  }
}
```

**Solution 4: Override `==` correctly**

```dart
class Money {
  final int amount;
  final String currency;

  Money(this.amount, this.currency);

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Money &&
          amount == other.amount &&
          currency == other.currency;

  @override
  int get hashCode => amount.hashCode ^ currency.hashCode;
}

void main() {
  print(Money(100, 'USD') == Money(100, 'USD')); // true
}
```

**Solution 5: Avoid converting non-bool to bool**

```dart
void main() {
  int? count;
  
  // Wrong pattern from other languages
  // if (count) { }
  
  // Dart idiomatic
  if (count != null && count > 0) {
    print('Count: $count');
  }
}
```

## Examples

Dart is strongly typed — `if (1)` is a compile error, unlike JavaScript. The `??` operator works well with booleans: `bool flag = nullableBool ?? false;`

## Related Errors

- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart Type Error](/languages/dart/dart-type-error/)
- [Dart Assert Error](/languages/dart/dart-assert-error/)
