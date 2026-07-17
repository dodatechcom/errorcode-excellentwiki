---
title: "[Solution] Dart HttpException Connection Closed"
description: "Fix Dart HttpException when connections are closed unexpectedly. Handle network errors, timeouts, and server issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `HttpException: Connection closed` error occurs when an HTTP connection is terminated before the response is fully received. This can happen due to server issues, network problems, or client timeout settings.

## Common Causes

- Server closes connection prematurely
- Network timeout
- Server overload or crash
- Keep-alive timeout exceeded
- TLS/SSL handshake failure

## How to Fix

```dart
// WRONG: No error handling
var response = await http.get(Uri.parse('https://api.example.com/data'));
// Error if connection drops

// CORRECT: Wrap in try-catch
try {
  var response = await http.get(Uri.parse('https://api.example.com/data'));
  print(response.body);
} on http.ClientException catch (e) {
  print('Client error: ${e.message}');
} on SocketException catch (e) {
  print('Socket error: ${e.message}');
}
```

```dart
// WRONG: No timeout configured
var response = await http.get(Uri.parse(url));  // May hang forever

// CORRECT: Set timeout
var response = await http.get(Uri.parse(url))
    .timeout(Duration(seconds: 30), onTimeout: () {
  throw TimeoutException('Request timed out');
});
```

```dart
// WRONG: Not retrying failed requests
await fetchData();  // Fails once, never retries

// CORRECT: Implement retry logic
Future<Response> fetchWithRetry(Uri url, {int maxRetries = 3}) async {
  for (int i = 0; i < maxRetries; i++) {
    try {
      return await http.get(url).timeout(Duration(seconds: 10));
    } on ClientException {
      if (i == maxRetries - 1) rethrow;
      await Future.delayed(Duration(seconds: 2 * (i + 1)));
    }
  }
  throw StateError('Unreachable');
}
```

## Examples

```dart
import 'dart:async';
import 'package:http/http.dart' as http;

// Example 1: Basic error handling
Future<String?> fetchData(String url) async {
  try {
    final response = await http.get(Uri.parse(url))
        .timeout(Duration(seconds: 10));
    if (response.statusCode == 200) {
      return response.body;
    }
    return null;
  } catch (e) {
    print('Failed to fetch: $e');
    return null;
  }
}

// Example 2: Dio with interceptors
// import 'package:dio/dio.dart';
// final dio = Dio(BaseOptions(
//   connectTimeout: Duration(seconds: 5),
//   receiveTimeout: Duration(seconds: 10),
// ));
```

## Related Errors

- [dart-http-error]({{< relref "/languages/dart/dart-http-error" >}}) — socket connection refused
- [dart-async-error]({{< relref "/languages/dart/dart-async-error" >}}) — timeout exception
- [dart-json-error]({{< relref "/languages/dart/dart-json-error" >}}) — JSON parsing error
