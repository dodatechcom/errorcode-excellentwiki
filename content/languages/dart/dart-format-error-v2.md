---
title: "[Solution] Dart FormatException Invalid Format"
description: "Fix Dart FormatException when parsing strings to numbers, dates, or other types. Handle malformed input safely."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `FormatException: Invalid format` error occurs when `parse()` methods fail to convert a string to the expected type, such as parsing a non-numeric string to an integer.

## Common Causes

- Parsing non-numeric string to int/double
- Incorrect date format string
- Malformed input from user or external source
- Wrong locale for number parsing
- Trailing or leading whitespace

## How to Fix

```dart
// WRONG: Parsing without validation
int number = int.parse('abc');  // FormatException

// CORRECT: Use tryParse for safe parsing
int? number = int.tryParse('abc');
print(number);  // null
```

```dart
// WRONG: Parsing user input directly
String input = getUserInput();
double value = double.parse(input);  // May fail

// CORRECT: Validate before parsing
double parseDouble(String input) {
  return double.tryParse(input.trim()) ?? 0.0;
}
```

```dart
// WRONG: Date parsing without format
DateTime date = DateTime.parse('not-a-date');  // FormatException

// CORRECT: Use intl package for flexible parsing
import 'package:intl/intl.dart';
var formatter = DateFormat('yyyy-MM-dd');
DateTime? date;
try {
  date = formatter.parseStrict('2024-01-15');
} catch (e) {
  print('Invalid date format');
}
```

## Examples

```dart
void main() {
  // Example 1: Safe number parsing
  List<String> inputs = ['42', '3.14', 'abc', '', '  100  '];
  
  for (var input in inputs) {
    int? value = int.tryParse(input.trim());
    print('$input -> $value');
  }
  // 42 -> 42, 3.14 -> null, abc -> null, '' -> null, 100 -> 100
  
  // Example 2: Parsing with fallback
  double safeParse(String s, {double fallback = 0.0}) {
    return double.tryParse(s.trim()) ?? fallback;
  }
  
  // Example 3: NumberFormat for locale-aware parsing
  // import 'package:intl/intl.dart';
  // var nf = NumberFormat('#,###.##', 'en_US');
  // double val = nf.parse('1,234.56');
}
```

## Related Errors

- [dart-json-error]({{< relref "/languages/dart/dart-json-error" >}}) — JSON parsing error
- [dart-type-error]({{< relref "/languages/dart/dart-type-error" >}}) — type mismatch
- [dart-null-error]({{< relref "/languages/dart/dart-null-error" >}}) — null check error
