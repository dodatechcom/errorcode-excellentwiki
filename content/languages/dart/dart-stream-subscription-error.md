---
title: "[Solution] Dart StreamSubscription Error — Cancel, Pause, Resume, onData"
description: "Fix Dart StreamSubscription errors from cancel/pause/resume misuse, missing onData handlers, and subscription leaks."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 122
---

StreamSubscription errors occur when subscriptions are not properly managed, canceled too early, or paused without resuming.

## Common Causes

1. Forgetting to cancel subscriptions, causing memory leaks.
2. Pausing a subscription without ever resuming it.
3. Calling `cancel()` and then trying to listen again.
4. Not handling the `onError` callback.
5. Adding data to a controller after the subscription is canceled.

## How to Fix It

**Solution 1: Cancel subscriptions in dispose**

```dart
import 'dart:async';

class Counter {
  StreamController<int> _controller = StreamController<int>.broadcast();
  StreamSubscription? _subscription;
  
  void startListening() {
    _subscription = _controller.stream.listen(
      (data) => print('Data: $data'),
      onError: (error) => print('Error: $error'),
      onDone: () => print('Stream done'),
    );
  }
  
  void dispose() {
    _subscription?.cancel();
    _controller.close();
  }
}
```

**Solution 2: Pause and resume correctly**

```dart
import 'dart:async';

void main() async {
  Stream<int> stream = Stream.periodic(Duration(milliseconds: 100), (i) => i);
  
  StreamSubscription<int> subscription = stream.listen((data) {
    print('Received: $data');
  });
  
  // Pause after receiving some data
  await Future.delayed(Duration(milliseconds: 500));
  subscription.pause();
  print('Paused');
  
  // Resume later
  await Future.delayed(Duration(seconds: 1));
  subscription.resume();
  print('Resumed');
  
  // Clean up
  await Future.delayed(Duration(milliseconds: 500));
  await subscription.cancel();
}
```

**Solution 3: Handle multiple listen calls**

```dart
import 'dart:async';

void main() async {
  StreamController<String> controller = StreamController<String>.broadcast();
  
  // Broadcast streams support multiple listeners
  StreamSubscription<String> sub1 = controller.stream.listen(
    (data) => print('Listener 1: $data'),
  );
  
  StreamSubscription<String> sub2 = controller.stream.listen(
    (data) => print('Listener 2: $data'),
  );
  
  controller.add('Hello');
  
  await Future.delayed(Duration.zero);
  await sub1.cancel();
  await sub2.cancel();
  await controller.close();
}
```

**Solution 4: Transform subscription data safely**

```dart
import 'dart:async';

void main() async {
  Stream<int> numbers = Stream.fromIterable([1, 2, 3, 4, 5]);
  
  StreamSubscription<String> subscription = numbers
      .where((n) => n.isEven)
      .map((n) => 'Even: $n')
      .listen(
        (data) => print(data),
        onDone: () => print('Done'),
      );
  
  await subscription.asFuture<void>();
}
```

**Solution 5: Use `asFuture` to await subscription completion**

```dart
import 'dart:async';

void main() async {
  Stream<int> stream = Stream.fromIterable([1, 2, 3]);
  
  StreamSubscription<int> sub = stream.listen((data) {
    print(data);
  });
  
  // Wait for the stream to complete
  await sub.asFuture<void>();
  print('Stream completed');
}
```

## Examples

A `StreamSubscription` represents the link between a stream and its listener. Calling `cancel()` releases resources. After `cancel()`, the subscription cannot be resumed — you must create a new subscription.

## Related Errors

- [Dart Stream Controller Error](/languages/dart/dart-stream-controller-error/)
- [Dart Stream Transform Error](/languages/dart/dart-stream-transform-error/)
- [Dart Future Delay Error](/languages/dart/dart-future-delay-error/)
