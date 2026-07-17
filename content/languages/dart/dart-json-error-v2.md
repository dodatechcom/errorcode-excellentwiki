---
title: "[Solution] Dart FormatException Unexpected Character in JSON"
description: "Fix Dart JSON parsing errors including unexpected characters, malformed JSON, and type mismatches."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["json", "parsing", "format", "decode", "serialization", "dart"]
weight: 5
---

## What This Error Means

A `FormatException: Unexpected character` error in JSON parsing occurs when `jsonDecode()` encounters malformed JSON input. This happens with invalid syntax, incorrect quoting, or encoding issues.

## Common Causes

- Malformed JSON string (missing quotes, trailing commas)
- Single quotes instead of double quotes
- Unescaped special characters
- BOM (byte order mark) in file
- Null bytes or control characters
- Server returning HTML instead of JSON

## How to Fix

```dart
// WRONG: Parsing invalid JSON
import 'dart:convert';
var data = jsonDecode("{name: 'Alice'}");  // Error: single quotes

// CORRECT: Use proper JSON syntax
var data = jsonDecode('{"name": "Alice"}');
```

```dart
// WRONG: Not handling server errors
var response = await http.get(url);
var data = jsonDecode(response.body);  // Error if HTML error page

// CORRECT: Validate response first
var response = await http.get(url);
if (response.headers['content-type']?.contains('json') == true) {
  var data = jsonDecode(response.body);
} else {
  throw FormatException('Expected JSON, got ${response.headers['content-type']}');
}
```

```dart
// WRONG: Parsing user input directly
String userInput = getUserInput();
var data = jsonDecode(userInput);  // May fail

// CORRECT: Try-catch with fallback
Map<String, dynamic> safeJsonDecode(String input) {
  try {
    return jsonDecode(input) as Map<String, dynamic>;
  } catch (e) {
    return {};
  }
}
```

## Examples

```dart
import 'dart:convert';

// Example 1: Validate JSON before parsing
bool isValidJson(String source) {
  try {
    jsonDecode(source);
    return true;
  } catch (e) {
    return false;
  }
}

// Example 2: Parse with type safety
T? safeParseJson<T>(String source) {
  try {
    final decoded = jsonDecode(source);
    if (decoded is T) return decoded;
    return null;
  } catch (e) {
    return null;
  }
}

// Example 3: Handle nested JSON safely
Map<String, dynamic> parseApiResponse(String body) {
  try {
    final json = jsonDecode(body);
    return json as Map<String, dynamic>;
  } on FormatException catch (e) {
    print('Invalid JSON: ${e.message}');
    return {'error': 'Invalid response'};
  }
}
```

## Related Errors

- [dart-format-error]({{< relref "/languages/dart/dart-format-error" >}}) — format exception
- [dart-type-error]({{< relref "/languages/dart/dart-type-error" >}}) — type mismatch
- [dart-io-error]({{< relref "/languages/dart/dart-io-error" >}}) — connection closed
