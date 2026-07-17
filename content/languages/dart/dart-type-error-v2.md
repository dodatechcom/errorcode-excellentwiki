---
title: "[Solution] Dart Type Is Not a Subtype Error"
description: "Fix Dart 'type X is not a subtype of type Y' error. Learn about Dart type casting, generics, and runtime type checks."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["type-error", "cast", "subtype", "generics", "runtime", "dart"]
weight: 5
---

## What This Error Means

The error `type 'X' is not a subtype of type 'Y'` occurs when Dart attempts a type cast that fails at runtime. This happens when you try to use a value as a type it doesn't actually implement.

## Common Causes

- Incorrect type casting with `as` operator
- Generic type mismatches
- Dynamic type returned where specific type expected
- JSON decoding returning wrong types
- Incorrect collection type annotations

## How to Fix

```dart
// WRONG: Unsafe type cast
dynamic data = getData();
String name = data as String;  // Error if data is int

// CORRECT: Safe type check first
if (data is String) {
  String name = data;
  print(name);
}
```

```dart
// WRONG: Wrong generic type
List<int> numbers = [1, 2, 3];
List<String> strings = numbers as List<String>;  // Error

// CORRECT: Map to correct type
List<String> strings = numbers.map((n) => n.toString()).toList();
```

```dart
// WRONG: JSON type assumption
Map<String, dynamic> json = {'count': '5'};
int count = json['count'] as int;  // Error: '5' is String

// CORRECT: Handle type conversion
int count = int.parse(json['count'].toString());
```

```dart
// WRONG: Implicit type conversion
Object obj = 42;
String str = obj;  // Error: Object is not String

// CORRECT: Explicit check
if (obj is String) {
  String str = obj;
}
```

## Examples

```dart
void main() {
  // Example 1: Safe casting function
  T? safeCast<T>(dynamic value) {
    if (value is T) return value;
    return null;
  }
  
  int? num = safeCast<int>('hello');  // null
  int? num2 = safeCast<int>(42);      // 42
  
  // Example 2: JSON type handling
  Map<String, dynamic> json = {'value': 42};
  int value = json['value'] as int;  // Works
  // int bad = json['value'] as String;  // Error
  
  // Example 3: Collection type safety
  List<Object> mixed = [1, 'two', 3.0];
  for (var item in mixed) {
    if (item is int) {
      print('Integer: $item');
    } else if (item is String) {
      print('String: $item');
    }
  }
}
```

## Related Errors

- [dart-null-error]({{< relref "/languages/dart/dart-null-error" >}}) — null check operator error
- [dart-json-error]({{< relref "/languages/dart/dart-json-error" >}}) — JSON parsing error
- [dart-index-error]({{< relref "/languages/dart/dart-index-error" >}}) — index out of range
