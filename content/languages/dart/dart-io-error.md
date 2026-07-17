---
title: "[Solution] Dart HttpException - Connection Closed"
description: "Fix Dart 'HttpException: Connection closed' error. Learn about HTTP client errors and connection handling in Dart."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `HttpException` occurs when an HTTP request fails due to connection issues, invalid responses, or server errors. This commonly happens when the server closes the connection unexpectedly or the request times out.

## Common Causes

- Server closed connection before response received
- Network timeout
- Invalid URL or host unreachable
- SSL/TLS certificate issues
- Request body too large

## How to Fix

Handle HTTP errors with try-catch:

```dart
import 'package:http/http.dart' as http;

Future<Map<String, dynamic>?> fetchData(String url) async {
  try {
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }
    return null;
  } on http.ClientException catch (e) {
    print('Client error: ${e.message}');
    return null;
  } on TimeoutException {
    print('Request timed out');
    return null;
  }
}
```

Set timeouts:

```dart
import 'package:http/http.dart' as http;

final response = await http.get(
  Uri.parse('https://api.example.com/data'),
).timeout(
  Duration(seconds: 10),
  onTimeout: () => throw TimeoutException('Request timed out'),
);
```

Use retry logic:

```dart
Future<T> retry<T>(Future<T> Function() fn, {int maxRetries = 3}) async {
  for (int i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i == maxRetries - 1) rethrow;
      await Future.delayed(Duration(seconds: 1 << i));
    }
  }
  throw StateError('Should not reach here');
}
```

## Examples

```dart
import 'package:http/http.dart' as http;

void main() async {
  final response = await http.get(Uri.parse('https://example.com/api'));
  // HttpException: Connection closed before full header was received
}
```

## Related Errors

- [async-error] — stream errors in Dart
- [json-error] — JSON decoding errors
