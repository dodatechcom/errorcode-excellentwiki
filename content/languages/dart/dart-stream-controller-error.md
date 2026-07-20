---
title: "[Solution] Dart StreamController Error — add, addError, close, Broadcast"
description: "Fix Dart StreamController errors from add/addClose on closed controllers, broadcast stream misuse, and listener management."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 124
---

StreamController errors occur when adding events to a closed controller, using a single-subscription controller for multiple listeners, or forgetting to close the controller.

## Common Causes

1. Calling `add()` or `addError()` after `close()`.
2. Using a single-subscription controller with multiple `.listen()` calls.
3. Not closing the controller, causing memory leaks.
4. `onListen`/`onCancel` callbacks causing unexpected behavior.
5. Broadcast controller losing events when no listeners are attached.

## How to Fix It

**Solution 1: Check if controller is closed before adding events**

```dart
import 'dart:async';

class EventManager {
  final StreamController<String> _controller = StreamController<String>();
  bool _isClosed = false;
  
  Stream<String> get stream => _controller.stream;
  
  void emit(String event) {
    if (!_isClosed) {
      _controller.add(event);
    }
  }
  
  void dispose() {
    _isClosed = true;
    _controller.close();
  }
}
```

**Solution 2: Use broadcast controllers for multiple listeners**

```dart
import 'dart:async';

void main() async {
  // Single-subscription — only one listener allowed
  // StreamController<String> single = StreamController<String>();
  // single.stream.listen((e) {});
  // single.stream.listen((e) {}); // Error!
  
  // Broadcast — multiple listeners allowed
  StreamController<String> broadcast = StreamController<String>.broadcast();
  
  broadcast.stream.listen((e) => print('Listener 1: $e'));
  broadcast.stream.listen((e) => print('Listener 2: $e'));
  
  broadcast.add('Hello');
  
  await Future.delayed(Duration.zero);
  await broadcast.close();
}
```

**Solution 3: Use `onListen` and `onCancel` for lazy streams**

```dart
import 'dart:async';

void main() {
  int counter = 0;
  
  StreamController<int> controller = StreamController<int>.broadcast(
    onListen: () => print('Listener attached'),
    onCancel: () => print('Listener removed'),
  );
  
  StreamSubscription<int> sub1 = controller.stream.listen((e) => print('Sub1: $e'));
  
  controller.add(1);
  
  sub1.cancel();
  
  controller.close();
}
```

**Solution 4: Forward events from one controller to another**

```dart
import 'dart:async';

void main() async {
  StreamController<int> source = StreamController<int>();
  StreamController<int> destination = StreamController<int>();
  
  // Forward all events
  source.stream.pipe(destination);
  
  destination.stream.listen((e) => print('Received: $e'));
  
  source.add(1);
  source.add(2);
  
  await source.close();
}
```

**Solution 5: Use `StreamController` with `sync: true` for predictable ordering**

```dart
import 'dart:async';

void main() async {
  // Async (default) — events delivered in next microtask
  StreamController<String> asyncCtrl = StreamController<String>();
  
  // Sync — events delivered immediately
  StreamController<String> syncCtrl = StreamController<String>.broadcast(sync: true);
  
  syncCtrl.stream.listen((e) => print('Sync: $e'));
  syncCtrl.add('immediate'); // Printed immediately
  
  await asyncCtrl.close();
  await syncCtrl.close();
}
```

## Examples

A `StreamController` that has been closed throws a `StateError` if you try to add events. Use the `done` future on a controller to know when it closes.

## Related Errors

- [Dart Stream Subscription Error](/languages/dart/dart-stream-subscription-error/)
- [Dart Stream Transform Error](/languages/dart/dart-stream-transform-error/)
- [Dart Completer Error](/languages/dart/dart-completer-error/)
