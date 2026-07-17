---
title: "[Solution] Dart TimeoutException Future Timed Out"
description: "Fix Dart TimeoutException when async operations exceed their time limit. Handle future timeouts and stream delays."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `TimeoutException` occurs when a `Future` or `Stream` operation takes longer than the specified timeout duration. Dart's `TimeoutException` is thrown by the `timeout()` method.

## Common Causes

- Network request taking too long
- Database query timeout
- Long-running computation blocking event loop
- Deadlock in async operations
- Too short timeout value

## How to Fix

```dart
// WRONG: No timeout configured
var result = await longRunningOperation();  // May hang forever

// CORRECT: Add timeout
var result = await longRunningOperation()
    .timeout(Duration(seconds: 30), onTimeout: () {
  throw TimeoutException('Operation timed out');
});
```

```dart
// WRONG: Too short timeout
var response = await http.get(url)
    .timeout(Duration(milliseconds: 100));  // Too aggressive

// CORRECT: Reasonable timeout with fallback
var response = await http.get(url)
    .timeout(Duration(seconds: 10), onTimeout: () {
  // Return cached data on timeout
  return cachedResponse;
});
```

```dart
// WRONG: Not handling stream timeout
await for (var data in stream) {
  process(data);  // May never complete
}

// CORRECT: Use timeout on stream
stream.timeout(Duration(seconds: 5), onTimeout: (event) {
  // Handle timeout per event
  event.resume();
});
```

## Examples

```dart
import 'dart:async';

// Example 1: Simple timeout
Future<String> fetchWithTimeout() async {
  try {
    final result = await fetchData()
        .timeout(Duration(seconds: 10));
    return result;
  } on TimeoutException {
    return 'Default value';
  }
}

// Example 2: Retry with increasing timeout
Future<T> retryWithTimeout<T>(
  Future<T> Function() operation, {
  int maxRetries = 3,
  Duration initialTimeout = const Duration(seconds: 5),
}) async {
  for (int i = 0; i < maxRetries; i++) {
    try {
      return await operation().timeout(
        initialTimeout * (i + 1),
      );
    } on TimeoutException {
      if (i == maxRetries - 1) rethrow;
      await Future.delayed(Duration(seconds: 1));
    }
  }
  throw StateError('Unreachable');
}

// Example 3: Stream timeout
Stream<int> countWithTimeout() async* {
  for (int i = 0; i < 10; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}
```

## Related Errors

- [dart-io-error]({{< relref "/languages/dart/dart-io-error" >}}) — connection closed
- [dart-http-error]({{< relref "/languages/dart/dart-http-error" >}}) — connection refused
- [dart-state-error]({{< relref "/languages/dart/dart-state-error" >}}) — no element in iterable
