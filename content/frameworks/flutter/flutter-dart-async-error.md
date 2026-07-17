---
title: "TimeoutException - future timed out"
description: "Dart throws TimeoutException when an asynchronous operation does not complete within the specified time limit"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A TimeoutException in Dart occurs when a Future does not complete within the expected time. This is common with network requests, database operations, or any long-running asynchronous task that exceeds its allowed duration.

## Common Causes

- Network request taking longer than the timeout duration
- Server not responding or experiencing high latency
- Database query taking too long to execute
- Default timeout too short for the operation
- Recursive async calls causing infinite loops

## How to Fix

1. Add a timeout to async operations:

```dart
import 'dart:async';

Future<Map<String, dynamic>?> fetchData() async {
  try {
    final response = await http.get(
      Uri.parse('https://api.example.com/data'),
    ).timeout(Duration(seconds: 10));
    return jsonDecode(response.body);
  } on TimeoutException {
    print('Request timed out');
    return null;
  }
}
```

2. Use Dio with configurable timeout:

```dart
import 'package:dio/dio.dart';

final dio = Dio(BaseOptions(
  connectTimeout: Duration(seconds: 15),
  receiveTimeout: Duration(seconds: 15),
  sendTimeout: Duration(seconds: 15),
));

try {
  final response = await dio.get('/api/data');
} on DioException catch (e) {
  if (e.type == DioExceptionType.connectionTimeout) {
    print('Connection timed out');
  }
}
```

3. Implement retry logic with exponential backoff:

```dart
Future<T> retryWithTimeout<T>(
  Future<T> Function() operation, {
  int maxRetries = 3,
  Duration timeout = const Duration(seconds: 10),
}) async {
  for (var i = 0; i < maxRetries; i++) {
    try {
      return await operation().timeout(timeout);
    } on TimeoutException {
      if (i == maxRetries - 1) rethrow;
      await Future.delayed(Duration(seconds: (i + 1) * 2));
    }
  }
  throw TimeoutException('Max retries exceeded');
}
```

4. Increase timeout for slow operations:

```dart
final response = await http.post(
  Uri.parse('https://api.example.com/upload'),
  body: largePayload,
).timeout(Duration(seconds: 60));
```

## Examples

```dart
// Error: TimeoutException after 30000 milliseconds
final response = await http.get(
  Uri.parse('https://slow-api.example.com/data'),
).timeout(Duration(seconds: 30));
// TimeoutException: TimeoutException after 0:00:30.000000

// Fix: increase timeout or add retry
final response = await http.get(
  Uri.parse('https://slow-api.example.com/data'),
).timeout(Duration(seconds: 60));
```

## Related Errors

- [Network error]({{< relref "/frameworks/flutter/flutter-network-error-v2" >}})
- [Async error]({{< relref "/frameworks/flutter/flutter-dart-async-error" >}})
