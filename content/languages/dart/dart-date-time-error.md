---
title: "[Solution] Dart DateTime Error — Parse, Format, Timezone, Difference"
description: "Fix Dart DateTime errors from parsing failures, timezone offsets, date difference calculations, and isUtc confusion."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 112
---

DateTime errors happen when parsing non-standard date strings, misusing UTC vs local time, or calculating differences incorrectly.

## Common Causes

1. `DateTime.parse` failing on non-ISO 8601 formats.
2. Confusing `DateTime.now()` (local) with `DateTime.now().toUtc()`.
3. Calculating duration differences across daylight saving time transitions.
4. `DateTime.utc` vs `DateTime` constructor confusion.
5. `isAfter`/`isBefore` comparing UTC and local dates unexpectedly.

## How to Fix It

**Solution 1: Handle parse failures gracefully**

```dart
void main() {
  List<String> dates = [
    '2024-01-15',
    '2024-01-15T10:30:00',
    '15/01/2024', // not ISO 8601
    'not a date',
  ];
  
  for (String dateStr in dates) {
    DateTime? date = DateTime.tryParse(dateStr);
    if (date != null) {
      print('Parsed: $date');
    } else {
      print('Failed to parse: $dateStr');
    }
  }
}
```

**Solution 2: Be explicit about UTC vs local time**

```dart
void main() {
  DateTime local = DateTime.now();
  DateTime utc = DateTime.now().toUtc();
  
  print('Local: $local');
  print('UTC: $utc');
  print('Are they equal? ${local == utc}'); // false (different time values)
  
  // Convert explicitly
  DateTime localFromUtc = utc.toLocal();
  print('Local from UTC: $localFromUtc');
}
```

**Solution 3: Calculate differences safely**

```dart
void main() {
  DateTime start = DateTime(2024, 1, 1);
  DateTime end = DateTime(2024, 3, 15);
  
  Duration diff = end.difference(start);
  print('Days: ${diff.inDays}');           // 74
  print('Hours: ${diff.inHours}');         // 1776
  print('Minutes: ${diff.inMinutes}');     // 106560
}
```

**Solution 4: Use `isAfter`/`isBefore` consistently**

```dart
void main() {
  DateTime date1 = DateTime.utc(2024, 6, 15);
  DateTime date2 = DateTime(2024, 6, 15); // local, may differ by timezone offset
  
  // Both are compared as millisecondsSinceEpoch
  // UTC 2024-06-15 00:00:00 vs local 2024-06-15 00:00:00 (offset applied)
  print(date1.isAfter(date2)); // depends on local timezone offset
}
```

**Solution 5: Format dates manually or use `intl` package**

```dart
// import 'package:intl/intl.dart';

void main() {
  DateTime now = DateTime.now();
  
  // Manual formatting
  String formatted = '${now.year}-${now.month.toString().padLeft(2, '0')}-${now.day.toString().padLeft(2, '0')}';
  print(formatted); // 2024-01-15
  
  // Using intl package (add dependency)
  // DateFormat formatter = DateFormat('yyyy-MM-dd HH:mm');
  // print(formatter.format(now));
}
```

## Examples

`DateTime(2024, 2, 29)` is valid (leap year), but `DateTime(2023, 2, 29)` wraps to March 1. Always validate dates after construction if using user input.

## Related Errors

- [Dart Duration Error](/languages/dart/dart-duration-error/)
- [Dart URI Encode Error](/languages/dart/dart-uri-encode-error/)
- [Dart String Concat Error](/languages/dart/dart-string-concat-error/)
