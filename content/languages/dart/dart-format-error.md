---
title: "[Solution] Dart FormatException - Invalid Format"
description: "Fix Dart 'FormatException: Invalid format' error. Learn about string parsing and validation in Dart."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["format", "parse", "invalid", "string", "conversion"]
weight: 5
---

## What This Error Means

A `FormatException` occurs when attempting to parse a string into a specific type (int, double, DateTime, etc.) and the string does not match the expected format.

## Common Causes

- Parsing non-numeric string as int or double
- Invalid date format string
- Malformed JSON or URI string
- Incorrect number format (commas, currency symbols)
- Null or empty string passed to parser

## How to Fix

Validate input before parsing:

```dart
String input = getUserInput();
int? value = int.tryParse(input);
if (value != null) {
  print('Parsed value: $value');
} else {
  print('Invalid number format');
}
```

Use tryParse for safe conversion:

```dart
double? price = double.tryParse(priceString);
if (price != null) {
  // Use price
} else {
  print('Invalid price format');
}
```

Handle date parsing:

```dart
DateTime? parseDate(String dateString) {
  try {
    return DateTime.parse(dateString);
  } catch (e) {
    print('Invalid date format: $dateString');
    return null;
  }
}
```

Validate before int.parse:

```dart
String count = getCountString();
if (RegExp(r'^\d+$').hasMatch(count)) {
  int number = int.parse(count);
}
```

## Examples

```dart
void main() {
  int number = int.parse('abc'); // FormatException: Invalid radix-10
  double value = double.parse('12.34.56'); // FormatException
}
```

## Related Errors

- [null-check] — null check operator fails on null
- [type-cast] — invalid type cast
