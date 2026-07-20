---
title: "[Solution] Dart Timer Error — Periodic, OneShot, Cancel, Negative Period"
description: "Fix Dart Timer errors from canceling timers, negative periods, periodic timer management, and timer callbacks."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 128
---

Timer errors occur when timers are not canceled, negative duration values are used, or timer callbacks throw exceptions.

## Common Causes

1. `Timer.periodic` not being canceled, causing memory leaks.
2. Using `Duration.zero` or negative durations.
3. Timer callback throwing an exception that crashes the zone.
4. Creating timers in widgets without canceling in dispose.
5. `isActive` check not being sufficient for cancel-then-recreate patterns.

## How to Fix It

**Solution 1: Cancel timers properly**

```dart
import 'dart:async';

void main() {
  Timer timer = Timer.periodic(Duration(seconds: 1), (t) {
    print('Tick');
    t.cancel(); // Stop after first tick
  });
}
```

**Solution 2: Use `Timer` for one-shot delayed execution**

```dart
import 'dart:async';

void main() {
  Timer(Duration(seconds: 2), () {
    print('Fires once after 2 seconds');
  });
  
  // Duration.zero schedules for next microtask
  Timer(Duration.zero, () {
    print('Fires in next microtask');
  });
}
```

**Solution 3: Handle timer cancellation gracefully**

```dart
import 'dart:async';

class Poller {
  Timer? _timer;
  
  void start() {
    _timer = Timer.periodic(Duration(seconds: 5), (_) => _poll());
  }
  
  void _poll() {
    print('Polling...');
  }
  
  void stop() {
    _timer?.cancel();
    _timer = null;
  }
  
  bool get isRunning => _timer?.isActive ?? false;
}

void main() {
  Poller poller = Poller();
  poller.start();
  
  Future.delayed(Duration(seconds: 12), () {
    poller.stop();
    print('Poller stopped');
  });
}
```

**Solution 4: Avoid negative or zero periodic intervals**

```dart
import 'dart:async';

void main() {
  // Negative period is not allowed — throws RangeError
  // Timer.periodic(Duration(seconds: -1), (t) {}); // RangeError
  
  // Zero period is valid but not recommended for periodic timers
  // It fires as fast as possible
  Timer.periodic(Duration.zero, (t) {
    t.cancel(); // Cancel immediately to avoid infinite loop
  });
}
```

**Solution 5: Use timer in async patterns safely**

```dart
import 'dart:async';

Future<T> withTimeout<T>(Future<T> task, Duration timeout) async {
  Timer? timer;
  
  Completer<T> completer = Completer<T>();
  
  timer = Timer(timeout, () {
    if (!completer.isCompleted) {
      completer.completeError(TimeoutException('Timed out'));
    }
  });
  
  try {
    T result = await task;
    if (!completer.isCompleted) {
      completer.complete(result);
    }
  } catch (e) {
    if (!completer.isCompleted) {
      completer.completeError(e);
    }
  } finally {
    timer?.cancel();
  }
  
  return completer.future;
}
```

## Examples

`Timer` is a class from `dart:async`. It does not block the event loop. Periodic timers continue firing until canceled, even if the callback takes longer than the interval.

## Related Errors

- [Dart Future Delay Error](/languages/dart/dart-future-delay-error/)
- [Dart Stream Subscription Error](/languages/dart/dart-stream-subscription-error/)
- [Dart Zone Error](/languages/dart/dart-zone-error/)
