---
title: "[Solution] Dart Completer Error — Complete, Already Completed, .future"
description: "Fix Dart Completer errors from double completion, not completing, and misuse of the .future getter."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 121
---

Completer errors occur when a `Completer` is completed more than once, never completed, or its `.future` is accessed incorrectly.

## Common Causes

1. Calling `complete()` or `completeError()` twice on the same `Completer`.
2. Never calling `complete()`, leaving listeners waiting forever.
3. Accessing `.future` before or after the completer is completed.
4. Completing with the wrong type.
5. Not handling errors from `completeError()`.

## How to Fix It

**Solution 1: Check `isCompleted` before completing**

```dart
import 'dart:async';

void main() {
  Completer<String> completer = Completer<String>();
  
  if (!completer.isCompleted) {
    completer.complete('Hello');
  }
  
  completer.future.then((value) => print(value)); // Hello
}
```

**Solution 2: Always complete in error cases too**

```dart
import 'dart:async';

Future<String> fetchData() async {
  Completer<String> completer = Completer<String>();
  
  try {
    String result = await someAsyncWork();
    completer.complete(result);
  } catch (e) {
    completer.completeError(e);
  }
  
  return completer.future;
}

Future<String> someAsyncWork() => Future.value('data');
```

**Solution 3: Use `complete` with a Future**

```dart
import 'dart:async';

void main() async {
  Completer<void> completer = Completer<void>();
  
  // Complete with a future — waits for it to resolve
  completer.complete(Future.delayed(Duration(seconds: 1), () {}));
  
  await completer.future;
  print('Done');
}
```

**Solution 4: Handle timeout scenarios**

```dart
import 'dart:async';

Future<T> withCompleterTimeout<T>(
  Future<T> Function(Completer<T> completer) task,
  Duration timeout,
) async {
  Completer<T> completer = Completer<T>();
  
  // Start the task
  task(completer);
  
  // Set a timeout
  Timer(timeout, () {
    if (!completer.isCompleted) {
      completer.completeError(TimeoutException('Timed out'));
    }
  });
  
  return completer.future;
}
```

**Solution 5: Single-use completer pattern**

```dart
import 'dart:async';

class AsyncInit {
  Completer<void>? _completer;
  
  Future<void> ensureInitialized() {
    if (_completer != null && !_completer!.isCompleted) {
      return _completer!.future;
    }
    
    _completer = Completer<void>();
    
    // Do initialization work
    _completer!.complete();
    return _completer!.future;
  }
}
```

## Examples

A `Completer` creates a `Future` that you control manually. The `.future` getter returns the associated `Future`. Completing a `Completer` that is already completed throws an `StateError`.

## Related Errors

- [Dart Future Delay Error](/languages/dart/dart-future-delay-error/)
- [Dart Stream Controller Error](/languages/dart/dart-stream-controller-error/)
- [Dart Zone Error](/languages/dart/dart-zone-error/)
