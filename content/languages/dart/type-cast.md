---
title: "[Solution] Dart Type Cast Error — 'type X is not a subtype of type Y'"
description: "Fix Dart type cast errors. Learn why 'type X is not a subtype of type Y' occurs and how to safely cast between types."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Type Cast Error — 'type X is not a subtype of type Y'

A `type 'X' is not a subtype of type 'Y'` error occurs when you attempt to cast a value to an incompatible type at runtime. Dart's type system cannot perform the conversion.

## Description

Dart is a statically typed language, but some casts are only verified at runtime. When you use `as` to force a type cast, or when Dart implicitly tries to convert a value, a `TypeError` is thrown if the types are not compatible.

Common scenarios:

- **Incorrect `as` cast** — casting a value to a type it doesn't implement.
- **JSON deserialization** — expecting a `String` but receiving an `int` from a parsed JSON map.
- **Wrong generic type** — a `List<dynamic>` contains unexpected types.
- **Interface mismatch** — an object doesn't implement the expected interface.

## Common Causes

```dart
// Cause 1: Incorrect explicit cast
dynamic value = 42;
String text = value as String; // TypeError: type 'int' is not a subtype of type 'String'

// Cause 2: JSON parsing returns wrong type
Map<String, dynamic> json = {'age': 'twenty'}; // might come as int
int age = json['age'] as int; // TypeError if it's actually a String

// Cause 3: Wrong list element type
List<dynamic> items = [1, 2, 3];
String first = items[0] as String; // TypeError

// Cause 4: Function return type mismatch
Object getObject() => 'hello';
int num = getObject() as int; // TypeError
```

## How to Fix

### Fix 1: Use is-check before casting

```dart
// Wrong
String text = value as String;

// Correct
if (value is String) {
  print(value.length);
} else {
  print('Not a string');
}
```

### Fix 2: Parse JSON carefully with type checks

```dart
// Wrong
int age = json['age'] as int;

// Correct
dynamic rawAge = json['age'];
int age;
if (rawAge is int) {
  age = rawAge;
} else if (rawAge is String) {
  age = int.tryParse(rawAge) ?? 0;
} else {
  age = 0;
}
```

### Fix 3: Use typed collections instead of dynamic

```dart
// Wrong
List<dynamic> items = [1, 2, 3];
String first = items[0] as String;

// Correct
List<String> items = ['a', 'b', 'c'];
String first = items[0];
```

### Fix 4: Use try-catch for defensive casting

```dart
// Wrong
int value = riskyCast() as int;

// Correct
try {
  int value = riskyCast() as int;
} on TypeError {
  print('Type cast failed');
}
```

## Examples

```dart
void main() {
  dynamic data = 42;

  // This triggers: type 'int' is not a subtype of type 'String'
  String text = data as String;
  print(text);
}
```

## Related Errors

- [null-check] — null check operator used on a null value.
- [NoSuchMethodError] — calling a method that doesn't exist.
- [RangeError] — index out of range on a list or string.
