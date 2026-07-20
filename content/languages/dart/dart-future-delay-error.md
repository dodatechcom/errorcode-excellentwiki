---
title: "[Solution] Dart Future.delayed Error — Timer Cancellation, Periodic Timer"
description: "Fix Dart Future.delayed misuse, timer cancellation issues, and periodic timer problems."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 120
---

Future.delayed errors involve canceling delayed operations, managing periodic timers, and handling async code that depends on timing.

## Common Causes

1. `Future.delayed` cannot be canceled — code runs even if no longer needed.
2. Multiple `Future.delayed` calls creating race conditions.
3. `Timer.periodic` not being canceled, causing memory leaks.
4. Using `Future.delayed` for polling instead of proper event mechanisms.
5. Assuming `Future.delayed` runs on a background thread.

## How to Fix It

**Solution 1: Use `Timer` for cancellable delays**

```dart
import 'dart:async';

void main() {
  Timer? timer;
  
  // Cancellable delayed execution
  timer = Timer(Duration(seconds: 2), () {
    print('This runs after 2 seconds');
  });
  
  // Cancel before it fires
  timer.cancel();
  print('Timer canceled');
}
```

**Solution 2: Cancel periodic timers properly**

```dart
import 'dart:async';

void main() {
  int count = 0;
  
  Timer periodic = Timer.periodic(Duration(seconds: 1), (timer) {
    count++;
    print('Tick $count');
    
    if (count >= 5) {
      timer.cancel();
      print('Periodic timer stopped');
    }
  });
}
```

**Solution 3: Use completer for cancellable futures**

```dart
import 'dart:async';

Future<void> delayedOperation() async {
  Completer<void> completer = Completer();
  bool canceled = false;
  
  Timer(Duration(seconds: 5), () {
    if (!canceled) {
      completer.complete();
    }
  });
  
  return completer.future;
}

void main() async {
  // Start the operation
  Future<void> operation = delayedOperation();
  
  // Cancel by setting flag
  await Future.delayed(Duration(seconds: 1), () {
    print('Operation canceled');
  });
}
```

**Solution 4: Avoid multiple overlapping delayed operations**

```dart
import 'dart:async';

Timer? debounceTimer;

void handleInput(String input) {
  debounceTimer?.cancel();
  
  debounceTimer = Timer(Duration(milliseconds: 300), () {
    print('Processing: $input');
  });
}

void main() {
  handleInput('a');
  handleInput('ab');
  handleInput('abc'); // Only this one fires
}
```

**Solution 5: Use `Future.delayed` for simple timeouts**

```dart
import 'dart:async';

Future<T> withTimeout<T>(Future<T> future, Duration timeout) async {
  return future.timeout(timeout, onTimeout: () {
    throw TimeoutException('Operation timed out');
  });
}

void main() async {
  try {
    String result = await withTimeout(
      Future.delayed(Duration(seconds: 2), () => 'done'),
      Duration(seconds: 1),
    );
    print(result);
  } on TimeoutException catch (e) {
    print('Timeout: $e');
  }
}
```

## Examples

`Future.delayed` does not block the event loop — it schedules work to run later. Dart is single-threaded, so `Future.delayed` runs its callback on the same isolate after the specified duration.

## Related Errors

- [Dart Timer Error](/languages/dart/dart-timer-error/)
- [Dart Completer Error](/languages/dart/dart-completer-error/)
- [Dart Stream Subscription Error](/languages/dart/dart-stream-subscription-error/)
