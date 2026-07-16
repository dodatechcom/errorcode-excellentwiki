---
title: "type cast error"
description: "A type cast error occurs when attempting to cast a value to an incompatible type at runtime."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["type-cast", "type-error", "casting", "dart"]
weight: 5
---

## What This Error Means

A type cast error occurs when you attempt to cast a value to an incompatible type using the `as` keyword. Dart's type system cannot perform the conversion, resulting in a `TypeError`.

## Common Causes

- Incorrect `as` cast to incompatible type
- JSON deserialization returning wrong type
- Wrong generic type assumptions
- Interface mismatch

## How to Fix

```dart
// WRONG: Incorrect explicit cast
dynamic value = 42;
String text = value as String; // TypeError

// CORRECT: Use type check before casting
if (value is String) {
  print(value.length);
} else {
  print('Not a string');
}
```

```dart
// WRONG: JSON parsing returns wrong type
Map<String, dynamic> json = {'age': 'twenty'};
int age = json['age'] as int; // TypeError if it's a String

// CORRECT: Parse carefully with type checks
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

## Examples

```dart
// Example 1: Wrong type cast
dynamic data = 42;
String text = data as String;
// TypeError: type 'int' is not a subtype of type 'String'

// Example 2: List element cast
List<dynamic> items = [1, 2, 3];
String first = items[0] as String;
// TypeError

// Example 3: Function return type
Object getObject() => 'hello';
int num = getObject() as int;
// TypeError
```

## Related Errors

- [Null check operator used on null](/languages/dart/null-check-error)
- [RangeError: Index out of range](/languages/dart/range-error)
