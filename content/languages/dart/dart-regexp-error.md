---
title: "[Solution] Dart RegExp Error — Pattern Syntax, Match, group, allMatches"
description: "Fix Dart RegExp errors from invalid pattern syntax, match group access, and allMatches misuse."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 110
---

RegExp errors arise from malformed regex patterns, accessing non-existent match groups, or misunderstanding lazy vs eager matching behavior.

## Common Causes

1. Unescaped special characters in regex patterns (e.g., `.` instead of `\.`).
2. Accessing a match group index that does not exist.
3. `firstMatch` returning `null` when no match is found.
4. Forgetting `allMatches` returns an `Iterable`, not a single match.
5. Greedy vs lazy quantifiers producing unexpected results.

## How to Fix It

**Solution 1: Validate regex patterns**

```dart
void main() {
  try {
    RegExp pattern = RegExp(r'[invalid');
  } on FormatException catch (e) {
    print('Invalid regex: $e');
  }
  
  // Valid pattern
  RegExp email = RegExp(r'^[\w.-]+@[\w.-]+\.\w+$');
  print(email.hasMatch('user@example.com')); // true
}
```

**Solution 2: Check for null before accessing groups**

```dart
void main() {
  RegExp datePattern = RegExp(r'(\d{4})-(\d{2})-(\d{2})');
  Match? match = datePattern.firstMatch('Today is 2024-01-15');
  
  if (match != null) {
    print('Full match: ${match.group(0)}'); // 2024-01-15
    print('Year: ${match.group(1)}');       // 2024
    print('Month: ${match.group(2)}');      // 01
    print('Day: ${match.group(3)}');        // 15
  }
}
```

**Solution 3: Use `allMatches` correctly**

```dart
void main() {
  RegExp wordPattern = RegExp(r'\b\w+\b');
  String text = 'Hello World Dart';
  
  Iterable<Match> matches = wordPattern.allMatches(text);
  
  for (Match match in matches) {
    print('${match.group(0)} at ${match.start}');
  }
}
```

**Solution 4: Use named groups for clarity**

```dart
void main() {
  RegExp urlPattern = RegExp(
    r'(?<protocol>https?)://(?<host>[^/]+)(?<path>/.*)?',
  );
  
  Match? match = urlPattern.firstMatch('https://example.com/page');
  
  if (match != null) {
    print('Protocol: ${match.namedGroup('protocol')}'); // https
    print('Host: ${match.namedGroup('host')}');         // example.com
    print('Path: ${match.namedGroup('path')}');         // /page
  }
}
```

**Solution 5: Escape special characters properly**

```dart
void main() {
  String input = 'Price is \$10.99 (USD)';
  
  // Escape the dollar sign and dot
  RegExp pricePattern = RegExp(r'\$[\d.]+');
  Match? match = pricePattern.firstMatch(input);
  
  if (match != null) {
    print('Price: ${match.group(0)}'); // $10.99
  }
}
```

## Examples

Dart uses PCRE-style regular expressions. The `dotAll` flag (`.` matches newlines) and `multiLine` flag (`^`/`$` match line boundaries) are controlled via constructor parameters.

## Related Errors

- [Dart URI Encode Error](/languages/dart/dart-uri-encode-error/)
- [Dart String Concat Error](/languages/dart/dart-string-concat-error/)
- [Dart Date Time Error](/languages/dart/dart-date-time-error/)
