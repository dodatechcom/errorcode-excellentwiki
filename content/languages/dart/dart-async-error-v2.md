---
title: "[Solution] Dart Future Already Completed Error - Async State Fix"
description: "Fix Dart 'Future already completed' error. Learn why completer panics on double completion, how to manage async state, and prevent race conditions."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `Future already completed` error is thrown when you call `complete`, `completeError`, or `completeWith` on a `Completer` that has already been completed. This is a state violation. A `Completer` can only transition from pending to completed once. Attempting to complete it a second time throws an `IllegalStateError`.

## Why It Happens

This error occurs in asynchronous code where a `Completer` is shared across multiple code paths. If two async operations both try to complete the same `Completer`, the second one crashes. Common triggers include network requests with retry logic where the first response completes the future, but the retry also tries to complete it, and event handlers that fire multiple times for the same async result.

The error also appears when a `Completer` is completed inside a `try-catch` block that does not guard against double completion:

```dart
final completer = Completer<String>();

// First call succeeds
completer.complete('done');

// Second call throws: Future already completed
completer.complete('done again');
```

## How to Fix It

Check `isCompleted` before completing a `Completer`:

```dart
final completer = Completer<String>();

if (!completer.isCompleted) {
  completer.complete('result');
}
```

Use `complete` only once with proper control flow:

```dart
Future<String> fetchData() async {
  final completer = Completer<String>();

  try {
    final result = await api.getData();
    if (!completer.isCompleted) {
      completer.complete(result);
    }
  } catch (e) {
    if (!completer.isCompleted) {
      completer.completeError(e);
    }
  }

  return completer.future;
}
```

Use `Future.sync` or `Future.microtask` to avoid manual Completer management:

```dart
// Simpler than Completer
Future<String> fetchData() async {
  return await api.getData();
}
```

Avoid sharing Completers across isolate boundaries. Each isolate has its own event loop and sharing mutable state like Completers causes race conditions.

Guard against timeouts that may complete after the main result:

```dart
final result = await fetchData().timeout(
  Duration(seconds: 10),
  onTimeout: () => 'fallback',
);

// Do not also complete a Completer for the same operation
```

## Common Mistakes

- Sharing a single Completer across multiple async operations
- Not checking `isCompleted` in retry or timeout logic
- Completing a Completer inside a loop that may iterate more than once
- Using Completers when plain async/await would be simpler
- Completing inside both a success and error handler without mutual exclusion

## Related Pages

- [Dart Isolate Error](/languages/dart/dart-isolate-error/)
- [Dart HTTP Error](/languages/dart/dart-http-error/)
- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart Widget Rebuild](/languages/dart/dart-widget-rebuild/)
- [Dart Navigation Error](/languages/dart/dart-navigation-error/)
