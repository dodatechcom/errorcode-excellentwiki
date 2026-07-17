---
title: "Null Check Operator Used on a Null Value"
description: "Flutter throws this error when the ! operator is used on a variable that is null"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The "Null check operator used on a null value" error occurs when you use the `!` (null check) operator on a variable that is actually null. This is a common issue in Dart's null safety system when assumptions about non-null values are wrong.

## Common Causes

- Using `!` operator on a nullable variable without checking first
- Uninitialized variables accessed before assignment
- Incorrect null handling in async operations
- Missing null checks after data fetching

## How to Fix

**Use null-aware operators:**

```dart
// Instead of:
final value = nullableVariable!;

// Use:
final value = nullableVariable ?? 'default';
```

**Add null checks before accessing:**

```dart
if (nullableVariable != null) {
  final value = nullableVariable!;
}
```

**Use optional chaining:**

```dart
final value = nullableVariable?.someProperty ?? 'default';
```

## Examples

```dart
// This triggers the error:
String? nullableString;
print(nullableString!.length); // Error: Null check operator

// Fixed versions:
print(nullableString?.length ?? 0); // Uses null-aware access
print(nullableString ?? 'empty'); // Uses default value
```

## Related Errors

- [RenderFlex Overflow]({{< relref "/frameworks/flutter/renderflex-overflow" >}})
