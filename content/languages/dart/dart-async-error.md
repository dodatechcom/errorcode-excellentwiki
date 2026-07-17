---
title: "[Solution] Dart AsyncError - Stream Error"
description: "Fix Dart 'AsyncError' and stream errors. Learn about asynchronous error handling in Dart streams and futures."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `AsyncError` or stream error occurs when an asynchronous operation fails within a Dart `Stream` or `Future`. These errors propagate through the stream and must be handled with `onError`, `catchError`, or `try-catch` in async contexts.

## Common Causes

- Unhandled exception in async function
- Stream controller adding error without subscription
- Future chain missing error handling
- Network request failure in async context
- Timer or periodic task throwing exception

## How to Fix

Handle stream errors:

```dart
Stream<int> numbers = Stream.fromIterable([1, 2, 3, 4, 5]);

numbers.listen(
  (number) => print(number),
  onError: (error) => print('Stream error: $error'),
  onDone: () => print('Stream completed'),
);
```

Handle future errors:

```dart
Future<String> fetchData() async {
  try {
    final response = await http.get(Uri.parse('https://api.example.com'));
    return response.body;
  } catch (e) {
    print('Error fetching data: $e');
    return 'Default data';
  }
}
```

Use stream transformers for error handling:

```dart
Stream<int> safeStream = numbers.handleError((error) {
  print('Caught: $error');
});
```

Catch errors in async generators:

```dart
Stream<int> countDown(int from) async* {
  for (int i = from; i >= 0; i--) {
    yield i;
  }
}

countDown(5).listen(
  (value) => print(value),
  onError: (e) => print('Error: $e'),
);
```

## Examples

```dart
void main() async {
  Stream<int> stream = Stream.fromFuture(
    Future.error(Exception('Stream failed')),
  );

  stream.listen(
    (data) => print(data),
    onError: (error) => print('Error: $error'),
  );
}
```

## Related Errors

- [http-error] — HTTP client connection errors
- [json-error] — JSON decoding errors
