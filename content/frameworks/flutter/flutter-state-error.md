---
title: "setState() called after dispose"
description: "Flutter throws a FlutterError when setState is called on a State object after it has been disposed"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["setstate", "dispose", "state", "lifecycle", "widget"]
weight: 5
---

This error occurs when `setState()` is called on a State object after it has been removed from the widget tree and disposed. This typically happens when async operations complete after the widget is unmounted.

## Common Causes

- Async operation (API call, timer) completes after widget is disposed
- Stream subscription not cancelled in `dispose()`
- Animation controller not stopped in `dispose()`
- Navigating away from a screen while async work is in progress
- Using `BuildContext` after the widget is unmounted

## How to Fix

1. Check `mounted` before calling `setState`:

```dart
class _MyWidgetState extends State<MyWidget> {
  String data = '';

  void loadData() async {
    final result = await fetchData();
    if (!mounted) return;
    setState(() {
      data = result;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text(data);
  }
}
```

2. Cancel subscriptions in `dispose()`:

```dart
class _MyWidgetState extends State<MyWidget> {
  StreamSubscription? _subscription;

  void startListening() {
    _subscription = eventStream.listen((event) {
      if (!mounted) return;
      setState(() { /* update */ });
    });
  }

  @override
  void dispose() {
    _subscription?.cancel();
    super.dispose();
  }
}
```

3. Use a state management library to avoid the pattern entirely:

```dart
// Using Provider
class MyViewModel extends ChangeNotifier {
  Future<void> loadData() async {
    final result = await fetchData();
    notifyListeners(); // safe, handled by Provider
  }
}
```

## Examples

```dart
class _ProfileState extends State<Profile> {
  @override
  void initState() {
    super.initState();
    _loadProfile();
  }

  void _loadProfile() async {
    final profile = await api.getProfile();
    setState(() { // Error if user navigated away
      _profile = profile;
    });
  }

  @override
  Widget build(BuildContext context) => Text(_profile?.name ?? 'Loading');
}
// FlutterError: setState() called after dispose(): _ProfileState#f1a2b
```

## Related Errors

- [Navigation error]({{< relref "/frameworks/flutter/navigation-error2" >}})
- [Platform error]({{< relref "/frameworks/flutter/platform-error" >}})
