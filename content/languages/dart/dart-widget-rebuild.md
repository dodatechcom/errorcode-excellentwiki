---
title: "[Solution] Dart setState Called After Dispose - Widget Rebuild Fix"
description: "Fix Dart setState called after dispose error in Flutter. Learn why setState crashes on disposed widgets and how to guard async callbacks safely."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `setState() called after dispose()` error occurs when you invoke `setState` on a `State` object that has already been disposed. Flutter removes the widget from the tree and calls `dispose()` on its state. After that point, the state object is no longer valid and calling `setState` throws a `FlutterError`.

## Why It Happens

The most common cause is an async callback that completes after the widget has been removed from the tree. A network request, timer, or stream listener finishes and tries to update the UI, but the widget is gone. The callback still holds a reference to the state object and calls `setState` on it.

Stream subscriptions that are not cancelled in `dispose()` are another frequent cause. If the stream emits a new value after disposal, the listener fires and calls `setState`.

```dart
class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  String data = '';

  void fetchData() async {
    final result = await api.getData();
    // If the user navigated away, this crashes
    setState(() {
      data = result;
    });
  }

  @override
  Widget build(BuildContext context) => Text(data);
}
```

## How to Fix It

Check `mounted` before calling `setState`:

```dart
void fetchData() async {
  final result = await api.getData();
  if (!mounted) return;
  setState(() {
    data = result;
  });
}
```

Cancel stream subscriptions and timers in `dispose()`:

```dart
class _MyWidgetState extends State<MyWidget> {
  StreamSubscription? _subscription;
  Timer? _timer;

  @override
  void initState() {
    super.initState();
    _subscription = eventStream.listen((_) {
      if (mounted) setState(() {});
    });
    _timer = Timer.periodic(Duration(seconds: 5), (_) {
      if (mounted) setState(() {});
    });
  }

  @override
  void dispose() {
    _subscription?.cancel();
    _timer?.cancel();
    super.dispose();
  }
}
```

Use `Completer` or `CancelableOperation` for cancellable async work:

```dart
import 'package:async/async.dart';

class _MyWidgetState extends State<MyWidget> {
  CancelableOperation? _operation;

  void fetchData() {
    _operation?.cancel();
    _operation = CancelableOperation.fromFuture(
      api.getData().then((result) {
        if (mounted) setState(() => data = result);
      }),
    );
  }

  @override
  void dispose() {
    _operation?.cancel();
    super.dispose();
  }
}
```

## Common Mistakes

- Not checking `mounted` before `setState` in async callbacks
- Forgetting to cancel stream subscriptions in `dispose()`
- Holding references to state objects in long-lived singletons or services
- Using `Timer.periodic` without cancelling it in `dispose()`
- Calling `setState` inside `dispose()` itself which is always invalid

## Related Pages

- [Dart Navigation Error](/languages/dart/dart-navigation-error/)
- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart Async Error](/languages/dart/dart-async-error-v2/)
- [Dart Plugin Error](/languages/dart/dart-plugin-error/)
- [Dart Missing Override](/languages/dart/dart-missing-override/)
