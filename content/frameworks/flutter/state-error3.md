---
title: "State management error"
description: "Flutter throws an error when state is inconsistent or not properly managed across the widget tree"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["state", "bloc", "provider", "change-notifier", "riverpod"]
weight: 5
---

This error occurs when state becomes inconsistent across the widget tree, typically when using state management solutions like Provider, Bloc, or Riverpod and the state is accessed after disposal or not properly initialized.

## Common Causes

- Accessing Provider/Bloc after it has been disposed
- State not initialized before the first build
- Listener registered multiple times without cleanup
- Circular dependency between state objects

## How to Fix

1. Handle loading and error states explicitly:

```dart
class _MyPageState extends State<MyPage> {
  @override
  Widget build(BuildContext context) {
    return Consumer<UserProvider>(
      builder: (context, provider, child) {
        if (provider.isLoading) return CircularProgressIndicator();
        if (provider.error != null) return Text('Error: ${provider.error}');
        return Text('User: ${provider.user?.name}');
      },
    );
  }
}
```

2. Dispose state properly with ChangeNotifier:

```dart
class MyModel extends ChangeNotifier {
  Timer? _timer;

  void startPolling() {
    _timer = Timer.periodic(Duration(seconds: 5), (_) {
      _fetchData();
    });
  }

  void _fetchData() async {
    final data = await fetchData();
    notifyListeners();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
}
```

3. Use `select` to limit rebuilds and avoid stale state:

```dart
// Only rebuild when userName changes
final name = context.select<UserProvider, String>((p) => p.user?.name ?? '');
```

4. Provide state at the correct level in the widget tree:

```dart
// Provide at the top level, not inside a StatefulWidget
MaterialApp(
  home: ChangeNotifierProvider(
    create: (_) => MyModel(),
    child: MyHomePage(),
  ),
);
```

## Examples

```dart
// Provider disposed but still accessed
final provider = Provider.of<UserProvider>(context, listen: false);
provider.user.name; // Error if provider was disposed
```

```text
FlutterError: looking up a deactivated widget's ancestor is unsafe.
At this point the state of the widget's tree is invalid.
```

## Related Errors

- [setState after dispose]({{< relref "/frameworks/flutter/widget-error" >}})
