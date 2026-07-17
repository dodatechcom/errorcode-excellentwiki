---
title: "[Solution] Dart Null Check Operator Used on Null Value — Runtime Error Fix"
description: "Fix Dart 'Null check operator used on a null value' error. Learn why the ! operator panics on null and how to handle nullable types safely."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Null Check Operator Used on Null Value — Runtime Error Fix

A `Null check operator used on a null value` error occurs when you use the `!` (null check) operator on a variable that is actually `null`. This is a runtime exception in Dart's null safety system.

## Description

In Dart's null-safe mode, the `!` operator asserts that a value is non-null and forces it into a non-nullable type. If the value is `null` at runtime, Dart throws a `LateInitializationError` or a `TypeError` with the message "Null check operator used on a null value".

Common scenarios:

- **Forced unwrapping of nullable fields** — using `!` on an optional parameter or field.
- **Late variable not initialized** — accessing a `late` variable before assignment.
- **Nullable map/list access** — indexing a map that doesn't contain the expected key.
- **API response fields** — accessing a field that may be absent from JSON.

## Common Causes

```dart
// Cause 1: Using ! on a nullable variable
String? name = null;
print(name!.length); // Error: Null check operator used on a null value

// Cause 2: Late variable not initialized
late String username;
print(username); // Error: LateInitializationError

// Cause 3: Map returns null for missing key
Map<String, String?> config = {};
String value = config['missing']!; // Error

// Cause 4: Uninitialized optional parameter
void greet({String? name}) {
  print('Hello, ${name!}'); // Error if name is null
}
```

## How to Fix

### Fix 1: Use null-aware operators instead of !

```dart
// Wrong
String? name = getName();
print(name!.length);

// Correct
print(name?.length ?? 0);
```

### Fix 2: Check for null before using the value

```dart
// Wrong
String? name = getOptionalName();
print(name!.toUpperCase());

// Correct
String? name = getOptionalName();
if (name != null) {
  print(name.toUpperCase());
} else {
  print('Name is not available');
}
```

### Fix 3: Use default values with ?? or ??=

```dart
// Wrong
String? name = getOptionalName();
print(name!.length);

// Correct
String name = getOptionalName() ?? 'Anonymous';
print(name.length);
```

### Fix 4: Initialize late variables properly

```dart
// Wrong
late String username;

// Correct
late String username = fetchUsername();

// Or check initialization
String? _username;
String get username => _username ??= fetchUsername();
```

## Examples

```dart
void main() {
  String? nullableName = null;

  // This triggers: Null check operator used on a null value
  print(nullableName!.length);
}
```

## Related Errors

- [type-cast] — type cast fails when converting between incompatible types.
- [NoSuchMethodError] — calling a method that doesn't exist on an object.
- [RangeError] — index is out of bounds.
