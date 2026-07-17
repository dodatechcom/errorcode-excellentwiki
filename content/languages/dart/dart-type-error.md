---
title: "[Solution] Dart Type Error - Type X is not a subtype of type Y"
description: "Fix Dart 'type X is not a subtype of type Y' runtime error. Learn about type casting and runtime type checking in Dart."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `type 'X' is not a subtype of type 'Y'` error occurs when Dart attempts an invalid type cast at runtime. This happens when a value of one type is used where a different type is expected.

## Common Causes

- Incorrect type cast with `as` operator
- Dynamic type used where specific type expected
- JSON decoding without type validation
- Generic type mismatch
- Incorrect function return type

## How to Fix

Use safe type casting:

```dart
// Wrong
String value = someDynamicValue as String;

// Correct
if (someDynamicValue is String) {
  String value = someDynamicValue;
}
```

Handle JSON decoding safely:

```dart
Map<String, dynamic> json = jsonDecode(response);
String name = json['name'] as String? ?? 'Unknown';
```

Use type checks before casting:

```dart
void process(dynamic value) {
  if (value is List<String>) {
    for (String item in value) {
      print(item);
    }
  } else {
    print('Expected List<String>');
  }
}
```

Use `tryCast` pattern:

```dart
String? tryCast<T>(dynamic value) {
  if (value is T) return value as T;
  return null;
}
```

## Examples

```dart
void main() {
  dynamic value = 42;
  String text = value as String; // Error: type 'int' is not a subtype of type 'String'
}
```

## Related Errors

- [null-check] — null check operator fails on null value
- [RangeError] — index is out of bounds
