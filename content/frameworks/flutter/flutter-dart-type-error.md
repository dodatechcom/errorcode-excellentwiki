---
title: "type X is not a subtype of type Y"
description: "Dart throws a type casting error when attempting to use a value as a type it does not match"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The "type X is not a subtype of type Y" error occurs in Dart when you try to assign or cast a value to an incompatible type. This is most common when parsing JSON data or working with `dynamic` types in Dart's type system.

## Common Causes

- JSON values parsed as wrong types (e.g., int parsed as String)
- Unsafe type casting with `as` operator
- Deserializing API responses without type validation
- List or Map types not matching expected generic types
- Null values cast to non-nullable types

## How to Fix

1. Use safe type casting:

```dart
// Bad: unsafe cast
final count = data['count'] as int;

// Good: safe cast with null check
final count = (data['count'] as num?)?.toInt() ?? 0;
```

2. Create a typed model with factory constructor:

```dart
class User {
  final String name;
  final int age;

  User({required this.name, required this.age});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      name: json['name'] as String? ?? '',
      age: (json['age'] as num?)?.toInt() ?? 0,
    );
  }
}

final user = User.fromJson(responseData);
```

3. Use pattern matching for type checking (Dart 3+):

```dart
final result = switch (data) {
  {'name': String name, 'age': int age} => User(name: name, age: age),
  _ => User(name: 'Unknown', age: 0),
};
```

4. Handle dynamic JSON safely:

```dart
Map<String, dynamic> parseJson(String jsonString) {
  final decoded = jsonDecode(jsonString);
  if (decoded is Map<String, dynamic>) {
    return decoded;
  }
  throw FormatException('Invalid JSON format');
}
```

5. Use generic type constraints:

```dart
T safeCast<T>(dynamic value, T defaultValue) {
  if (value is T) return value;
  return defaultValue;
}

final name = safeCast<String>(json['name'], 'Unknown');
```

## Examples

```dart
// Error: type 'String' is not a subtype of type 'int'
final data = {'count': '5'};
final count = data['count'] as int; // String cannot be cast to int

// Fix: parse correctly
final count = int.parse(data['count'] as String);

// Or handle both types
final count = (data['count'] as num?)?.toInt() ?? 0;
```

## Related Errors

- [Null error]({{< relref "/frameworks/flutter/flutter-dart-null-error" >}})
- [Index error]({{< relref "/frameworks/flutter/flutter-dart-index-error" >}})
