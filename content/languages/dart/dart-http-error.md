---
title: "[Solution] Dart ClientException - HTTP Client Error"
description: "Fix Dart 'ClientException' in HTTP requests. Learn about network errors, timeouts, and client configuration in Dart."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["http", "client", "network", "timeout", "request"]
weight: 5
---

## What This Error Means

A `ClientException` occurs when the Dart HTTP client encounters a network error during a request. This includes connection failures, timeouts, SSL errors, and incomplete responses.

## Common Causes

- Server unreachable or DNS resolution failure
- Connection timeout
- SSL certificate verification failure
- Server closed connection prematurely
- Invalid URL format

## How to Fix

Handle client exceptions:

```dart
import 'package:http/http.dart' as http;

Future<String?> fetchData(String url) async {
  try {
    final response = await http.get(Uri.parse(url));
    return response.body;
  } on http.ClientException catch (e) {
    print('Client error: ${e.message}');
    return null;
  }
}
```

Set custom timeouts:

```dart
import 'package:http/http.dart' as http;

final client = http.Client();
try {
  final response = await client.get(
    Uri.parse('https://api.example.com/data'),
  ).timeout(
    Duration(seconds: 15),
    onTimeout: () => throw http.ClientException('Request timed out'),
  );
  print(response.body);
} finally {
  client.close();
}
```

Handle SSL errors:

```dart
import 'package:http/http.dart' as http;

// For development only - not recommended for production
final client = http.Client();
try {
  final response = await client.get(Uri.parse('https://self-signed.example.com'));
} on http.ClientException catch (e) {
  print('SSL or connection error: ${e.message}');
} finally {
  client.close();
}
```

## Examples

```dart
import 'package:http/http.dart' as http;

void main() async {
  final response = await http.get(Uri.parse('https://nonexistent.example.com'));
  // ClientException: Failed host lookup
}
```

## Related Errors

- [io-error] — HTTP connection closed errors
- [async-error] — stream errors in Dart
