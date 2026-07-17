---
title: "[Solution] Dart Null Check Operator Used on Null Value"
description: "Fix Dart 'Null check operator used on a null value' error. Learn why the ! operator panics on null and how to handle nullable types safely."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `Null check operator used on a null value` error occurs when you use the `!` (null check) operator on a variable that is actually `null`. This is a runtime exception in Dart's null safety system.

## Common Causes

- Using `!` on a nullable variable without null check
- Late variable not initialized before access
- Map returns null for missing key
- Uninitialized optional parameter

## How to Fix

Use null-aware operators instead of `!`:

```dart
String? name = getName();
print(name?.length ?? 0); // Safe access with fallback
```

Check for null before using the value:

```dart
String? name = getOptionalName();
if (name != null) {
  print(name.toUpperCase());
} else {
  print('Name is not available');
}
```

Use default values with `??`:

```dart
String name = getOptionalName() ?? 'Anonymous';
print(name.length);
```

Initialize late variables properly:

```dart
late String username = fetchUsername();
// Or use nullable alternative
String? _username;
String get username => _username ??= fetchUsername();
```

## Examples

```dart
void main() {
  String? nullableName = null;
  print(nullableName!.length); // Error: Null check operator used on a null value
}
```

## Related Errors

- [type-cast] — type cast fails when converting between incompatible types
- [RangeError] — index is out of bounds
