---
title: "[Solution] Flutter ValueNotifier Error — listeners, addListener, removeListener"
description: "Fix Flutter ValueNotifier errors from listener management, disposal, threading, and ValueListenableBuilder usage."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 185
---

ValueNotifier errors occur when listeners are not properly managed, the notifier is not disposed, or `ValueListenableBuilder` is used incorrectly.

## Common Causes

1. Forgetting to call `removeListener` in `dispose()`.
2. Adding the same listener multiple times.
3. Not disposing the `ValueNotifier`, causing memory leaks.
4. Using `ValueListenableBuilder` with a null listenable.
5. Changing value without triggering listener if using `==` comparison.

## How to Fix It

**Solution 1: Use ValueListenableBuilder**

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

**Solution 2: Add and remove listeners properly**

```dart
import 'package:flutter/material.dart';

class ListenerWidget extends StatefulWidget {
  @override
  State<ListenerWidget> createState() => _ListenerWidgetState();
}

class _ListenerWidgetState extends State<ListenerWidget> {
  final ValueNotifier<String> _notifier = ValueNotifier<String>('');
  
  void _onValueChanged() {
    print('Value changed: ${_notifier.value}');
  }
  
  @override
  void initState() {
    super.initState();
    _notifier.addListener(_onValueChanged);
  }
  
  @override
  void dispose() {
    _notifier.removeListener(_onValueChanged);
    _notifier.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () => _notifier.value = 'Updated ${DateTime.now()}',
      child: Text('Update'),
    );
  }
}
```

**Solution 3: Custom ValueNotifier with equality**

```dart
import 'package:flutter/material.dart';

class UserNotifier extends ValueNotifier<User> {
  UserNotifier() : super(User(name: 'Guest', age: 0));
  
  void updateName(String name) {
    value = value.copyWith(name: name);
  }
  
  void updateAge(int age) {
    value = value.copyWith(age: age);
  }
}

class User {
  final String name;
  final int age;
  
  User({required this.name, required this.age});
  
  User copyWith({String? name, int? age}) {
    return User(
      name: name ?? this.name,
      age: age ?? this.age,
    );
  }
}

class UserWidget extends StatelessWidget {
  final notifier = UserNotifier();
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ValueListenableBuilder<User>(
          valueListenable: notifier,
          builder: (context, user, child) {
            return Text('${user.name}, Age: ${user.age}');
          },
        ),
        ElevatedButton(
          onPressed: () => notifier.updateName('Alice'),
          child: Text('Set Alice'),
        ),
      ],
    );
  }
}
```

**Solution 4: Use ListenableBuilder for multiple listenables**

```dart
import 'package:flutter/material.dart';

class MultiListenableWidget extends StatefulWidget {
  @override
  State<MultiListenableWidget> createState() => _MultiListenableWidgetState();
}

class _MultiListenableWidgetState extends State<MultiListenableWidget> {
  final ValueNotifier<int> _counter = ValueNotifier<int>(0);
  final ValueNotifier<String> _text = ValueNotifier<String>('');
  
  @override
  void dispose() {
    _counter.dispose();
    _text.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: Listenable.merge([_counter, _text]),
      builder: (context, child) {
        return Column(
          children: [
            Text('Counter: ${_counter.value}'),
            Text('Text: ${_text.value}'),
            ElevatedButton(
              onPressed: () => _counter.value++,
              child: Text('Inc'),
            ),
          ],
        );
      },
    );
  }
}
```

**Solution 5: ValueNotifier in separate class**

```dart
import 'package:flutter/material.dart';

class ThemeManager extends ChangeNotifier {
  bool _isDark = false;
  bool get isDark => _isDark;
  
  void toggleTheme() {
    _isDark = !_isDark;
    notifyListeners();
  }
}

// Usage with ValueListenableBuilder
class ThemeWidget extends StatelessWidget {
  final ThemeManager _themeManager = ThemeManager();
  
  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: _themeManager,
      builder: (context, child) {
        return MaterialApp(
          theme: _themeManager.isDark ? ThemeData.dark() : ThemeData.light(),
          home: Scaffold(
            body: Center(child: Text('Theme: ${_themeManager.isDark ? "Dark" : "Light"}')),
            floatingActionButton: FloatingActionButton(
              onPressed: _themeManager.toggleTheme,
              child: Icon(Icons.brightness_6),
            ),
          ),
        );
      },
    );
  }
}
```

## Examples

`ValueNotifier<T>` extends `ChangeNotifier` and notifies listeners when `value` changes. Use `ValueListenableBuilder` for efficient widget rebuilds — only the builder's child is rebuilt.

## Related Errors

- [Flutter Change Notifier Error](/languages/dart/flutter-change-notifier-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
- [Flutter Provider Error](/languages/dart/flutter-provider-error/)
