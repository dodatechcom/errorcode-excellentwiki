---
title: "Null check operator used on null"
description: "A null check error occurs when using the ! operator on a null value."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "check", "operator", "dart"]
weight: 5
---

## What This Error Means

A `Null check operator used on null value` error occurs when you use the `!` (null check) operator on a value that is null. This operator asserts that the value is non-null, but if it is null, a `TypeError` is thrown.

## Common Causes

- Using `!` on nullable variables without null check
- Assuming Future result is non-null
- Database or API returning null
- Missing null-aware operators

## How to Fix

```dart
// WRONG: Using ! on nullable value
String? name = null;
print(name!.length);  // Null check error

// CORRECT: Use null check or default
String? name = null;
print(name?.length ?? 0);
// or
if (name != null) {
  print(name.length);
}
```

```dart
// WRONG: Assuming Future result is non-null
Future<String?> future = fetchData();
String result = future.then((v) => v!) as String;  // Null check error

// CORRECT: Handle null in Future
Future<String?> future = fetchData();
String result = await future ?? 'default';
```

## Examples

```dart
// Example 1: Null variable
String? s = null;
int len = s!.length;  // Null check operator used on null

// Example 2: Map access
Map<String, String?> map = {};
String value = map['key']!;  // Null check error

// Example 3: Function return
String? findUser(int id) => null;
String name = findUser(99)!.toUpperCase();  // Null check error
```

## Related Errors

- [type cast error](/languages/dart/type-cast-error)
- [StateError: No element](/languages/dart/state-error4)
