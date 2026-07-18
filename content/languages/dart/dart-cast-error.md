---
title: "[Solution] Dart Type Cast Error - X Is Not a Subtype of Y"
description: "Fix Dart type cast error 'X is not a subtype of type Y'. Learn why downcasting fails at runtime, how to use is-checks, and safe type conversion patterns."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `type 'X' is not a subtype of type 'Y'` error occurs when Dart attempts to cast a value to an incompatible type at runtime. The variable holds an object of one type, but you are trying to use it as a different, incompatible type. This is a `TypeError` that halts execution.

## Why It Happens

Dart is statically typed, but type checking happens both at compile time and runtime. Generics are reified, meaning the actual type parameter is preserved at runtime. When you cast a `List<dynamic>` element to a specific type and the element is not that type, the cast fails.

The most common scenarios are JSON deserialization where the API returns unexpected types, downcasting from a parent class to a child class without an `is` check, and treating a `num` as an `int` when it is actually a `double`.

```dart
dynamic value = 3.14;
int number = value as int; // TypeError: double is not a subtype of int
```

Type inference can also cause unexpected casts. When a variable is inferred as `Object` or `dynamic`, operations on it may require explicit casting that fails at runtime.

## How to Fix It

Use the `is` operator to check types before casting:

```dart
dynamic value = getApiResponse();

if (value is String) {
  print(value.length); // Safe, value is promoted to String
} else {
  print('Expected String but got ${value.runtimeType}');
}
```

Use safe casting with `as` inside a try-catch:

```dart
try {
  int number = value as int;
} on TypeError catch (e) {
  print('Type mismatch: $e');
}
```

Handle JSON deserialization carefully:

```dart
Map<String, dynamic> json = jsonDecode(responseBody);

// Wrong - assumes type
int count = json['count'] as int;

// Correct - check and convert
int count = (json['count'] as num).toInt();
```

Use pattern matching in Dart 3:

```dart
// Dart 3 switch expression
switch (value) {
  case int n => print('Integer: $n'),
  case double d => print('Double: $d'),
  case String s => print('String: $s'),
  default => print('Unknown type'),
}
```

Avoid `dynamic` when possible. Use explicit type annotations to catch mismatches at compile time rather than runtime.

## Common Mistakes

- Casting `dynamic` values without `is` checks, assuming the runtime type matches expectations
- Treating all numbers as `int` when JSON often returns `double`
- Not accounting for null values in typed casts from nullable maps
- Relying on implicit casts between `num`, `int`, and `double`
- Using `as` casts in hot paths where the performance cost of `is` checks is preferable

## Related Pages

- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart JSON Error](/languages/dart/dart-json-error/)
- [Dart Type Error](/languages/dart/dart-type-error/)
- [Dart Index Error](/languages/dart/dart-index-error/)
- [Dart Format Error](/languages/dart/dart-format-error/)
