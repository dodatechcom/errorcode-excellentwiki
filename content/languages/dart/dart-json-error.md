---
title: "[Solution] Dart jsonDecode Error"
description: "Fix Dart 'jsonDecode' errors when parsing JSON strings. Learn about JSON decoding and validation in Dart."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `jsonDecode` error in Dart occurs when attempting to parse an invalid JSON string. This happens when the JSON is malformed, contains invalid characters, or does not conform to JSON syntax rules.

## Common Causes

- Malformed JSON string (missing quotes, trailing commas)
- Single quotes instead of double quotes
- Null bytes or invalid characters
- JSON string is actually HTML or plain text
- Encoding issues (BOM, wrong charset)

## How to Fix

Decode JSON with error handling:

```dart
import 'dart:convert';

Map<String, dynamic>? parseJson(String jsonString) {
  try {
    return jsonDecode(jsonString) as Map<String, dynamic>;
  } on FormatException catch (e) {
    print('Invalid JSON: ${e.message}');
    return null;
  }
}
```

Handle nested JSON safely:

```dart
import 'dart:convert';

void processApiResponse(String responseBody) {
  try {
    final data = jsonDecode(responseBody);
    final users = (data['users'] as List?)?.map((u) => u as Map<String, dynamic>).toList();
    print('Users: ${users?.length ?? 0}');
  } on FormatException {
    print('Invalid JSON response');
  } on TypeError catch (e) {
    print('Unexpected data structure: $e');
  }
}
```

Validate JSON before decoding:

```dart
import 'dart:convert';

bool isValidJson(String jsonString) {
  try {
    jsonDecode(jsonString);
    return true;
  } catch (e) {
    return false;
  }
}
```

Encode objects to JSON:

```dart
import 'dart:convert';

Map<String, dynamic> user = {'name': 'John', 'age': 30};
String jsonString = jsonEncode(user);
print(jsonString); // {"name":"John","age":30}
```

## Examples

```dart
import 'dart:convert';

void main() {
  String invalidJson = "{'name': 'John'}"; // Single quotes
  Map<String, dynamic> data = jsonDecode(invalidJson);
  // FormatException: Unexpected character
}
```

## Related Errors

- [format-error] — invalid format exceptions
- [type-cast] — type cast errors
