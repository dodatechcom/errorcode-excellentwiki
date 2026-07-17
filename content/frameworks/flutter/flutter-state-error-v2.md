---
title: "setState() called after dispose"
description: "Flutter throws setState() called after dispose error when attempting to update state of a widget that has been removed from the tree"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["flutter", "setstate", "dispose", "lifecycle", "widget", "state"]
weight: 5
---

The "setState() called after dispose" error occurs when an asynchronous operation completes and tries to update the state of a widget that has already been disposed. This commonly happens with network callbacks, timers, or stream listeners that outlive the widget.

## Common Causes

- Async callback (API call) completes after widget is disposed
- Timer or interval not cancelled in dispose()
- Stream subscription not cancelled in dispose()
- Navigator.pop called before async operation completes
- TextEditingController used after widget disposal

## How to Fix

1. Check `mounted` before calling setState in async callbacks:

```dart
class _MyWidgetState extends State<MyWidget> {
  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    final data = await api.getData();
    if (mounted) {
      setState(() {
        _data = data;
      });
    }
  }

  @override
  Widget build(BuildContext context) => Text(_data ?? 'Loading...');
}
```

2. Cancel timers and subscriptions in dispose():

```dart
class _TimerWidgetState extends State<TimerWidget> {
  late Timer _timer;

  @override
  void initState() {
    super.initState();
    _timer = Timer.periodic(Duration(seconds: 1), (_) {
      if (mounted) setState(() {});
    });
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }
}
```

3. Use a flag to prevent state updates after disposal:

```dart
class _MyWidgetState extends State<MyWidget> {
  bool _disposed = false;

  @override
  void dispose() {
    _disposed = true;
    super.dispose();
  }

  void _updateState() {
    if (!_disposed) {
      setState(() {});
    }
  }
}
```

4. Cancel stream subscriptions in dispose():

```dart
class _StreamWidgetState extends State<StreamWidget> {
  late StreamSubscription _subscription;

  @override
  void initState() {
    super.initState();
    _subscription = eventStream.listen((event) {
      if (mounted) setState(() {});
    });
  }

  @override
  void dispose() {
    _subscription.cancel();
    super.dispose();
  }
}
```

## Examples

```dart
class ProfileScreen extends StatefulWidget {
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  String? name;

  @override
  void initState() {
    super.initState();
    loadProfile();
  }

  Future<void> loadProfile() async {
    final profile = await api.getProfile();
    setState(() => name = profile.name); // Error if disposed
  }

  @override
  Widget build(BuildContext context) => Text(name ?? 'Loading...');
}
```

## Related Errors

- [Navigation error]({{< relref "/frameworks/flutter/flutter-navigation-error-v2" >}})
- [Async error]({{< relref "/frameworks/flutter/flutter-dart-async-error" >}})
