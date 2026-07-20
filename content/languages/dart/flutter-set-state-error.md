---
title: "[Solution] Flutter setState Error — disposed widget, mounted check, lifecycle"
description: "Fix Flutter setState errors from calling setState on disposed widgets, missing mounted checks, and lifecycle issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 180
---

setState errors occur when `setState` is called after the widget is disposed, or when async operations complete after the widget lifecycle ends.

## Common Causes

1. Calling `setState` after `dispose()` has been called.
2. Async callbacks completing after the widget is removed from the tree.
3. Not checking `mounted` before calling `setState`.
4. Using `setState` in `initState` before the first build.
5. `setState` called from a `StreamSubscription` after disposal.

## How to Fix It

**Solution 1: Check mounted before setState**

```dart
import 'package:flutter/material.dart';

class DataWidget extends StatefulWidget {
  @override
  State<DataWidget> createState() => _DataWidgetState();
}

class _DataWidgetState extends State<DataWidget> {
  String _data = 'Loading...';
  
  @override
  void initState() {
    super.initState();
    _loadData();
  }
  
  Future<void> _loadData() async {
    final result = await fetchData();
    
    if (!mounted) return;
    
    setState(() {
      _data = result;
    });
  }
  
  Future<String> fetchData() async {
    await Future.delayed(Duration(seconds: 2));
    return 'Loaded data';
  }
  
  @override
  Widget build(BuildContext context) {
    return Text(_data);
  }
}
```

**Solution 2: Cancel subscriptions in dispose**

```dart
import 'dart:async';
import 'package:flutter/material.dart';

class StreamWidget extends StatefulWidget {
  @override
  State<StreamWidget> createState() => _StreamWidgetState();
}

class _StreamWidgetState extends State<StreamWidget> {
  StreamSubscription? _subscription;
  final List<int> _numbers = [];
  
  @override
  void initState() {
    super.initState();
    _subscription = Stream.periodic(
      Duration(seconds: 1),
      (i) => i,
    ).listen((number) {
      if (!mounted) return;
      
      setState(() {
        _numbers.add(number);
      });
    });
  }
  
  @override
  void dispose() {
    _subscription?.cancel();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Text('Numbers: ${_numbers.length}');
  }
}
```

**Solution 3: Safe timer pattern**

```dart
import 'dart:async';
import 'package:flutter/material.dart';

class TimerWidget extends StatefulWidget {
  @override
  State<TimerWidget> createState() => _TimerWidgetState();
}

class _TimerWidgetState extends State<TimerWidget> {
  Timer? _timer;
  int _seconds = 0;
  
  @override
  void initState() {
    super.initState();
    _timer = Timer.periodic(Duration(seconds: 1), (timer) {
      if (!mounted) {
        timer.cancel();
        return;
      }
      setState(() => _seconds++);
    });
  }
  
  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Text('Seconds: $_seconds');
  }
}
```

**Solution 4: Avoid setState in initState for async work**

```dart
import 'package:flutter/material.dart';

class EarlyStateWidget extends StatefulWidget {
  @override
  State<EarlyStateWidget> createState() => _EarlyStateWidgetState();
}

class _EarlyStateWidgetState extends State<EarlyStateWidget> {
  bool _loaded = false;
  
  @override
  void initState() {
    super.initState();
    // Don't call setState here — use postFrameCallback
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (mounted) {
        setState(() => _loaded = true);
      }
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Text(_loaded ? 'Loaded' : 'Not loaded');
  }
}
```

**Solution 5: Use ValueNotifier for simple state**

```dart
import 'package:flutter/material.dart';

class CounterWidget extends StatefulWidget {
  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  final ValueNotifier<int> _counter = ValueNotifier<int>(0);
  
  @override
  void dispose() {
    _counter.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ValueListenableBuilder<int>(
          valueListenable: _counter,
          builder: (context, value, child) {
            return Text('Count: $value');
          },
        ),
        ElevatedButton(
          onPressed: () => _counter.value++,
          child: Text('Increment'),
        ),
      ],
    );
  }
}
```

## Examples

The `mounted` property is `true` between `initState` and `dispose`. After `dispose` is called, `mounted` becomes `false` and calling `setState` throws a framework error.

## Related Errors

- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
- [Flutter Animation Controller Error](/languages/dart/flutter-animation-controller-error/)
- [Flutter Change Notifier Error](/languages/dart/flutter-change-notifier-error/)
