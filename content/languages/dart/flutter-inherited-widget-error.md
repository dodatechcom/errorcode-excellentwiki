---
title: "[Solution] Flutter InheritedWidget Error — dependOnInheritedWidgetOfExactType"
description: "Fix Flutter InheritedWidget errors from incorrect dependOnInheritedWidgetOfExactType usage and missing providers."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 153
---

InheritedWidget errors occur when widgets try to access inherited data that is not available above them in the tree, or when using the wrong lookup method.

## Common Causes

1. `dependOnInheritedWidgetOfExactType` returning null when provider is missing.
2. Using `context.read` where `context.watch` is needed (or vice versa).
3. Accessing inherited data from a widget that is not a descendant of the provider.
4. Circular dependencies between InheritedWidgets.
5. Not registering with `dependOn` when needing rebuilds on changes.

## How to Fix It

**Solution 1: Provide data above the consumer**

```dart
import 'package:flutter/material.dart';

class ThemeProvider extends InheritedWidget {
  final bool isDark;
  
  const ThemeProvider({
    super.key,
    required this.isDark,
    required super.child,
  });
  
  static ThemeProvider? of(BuildContext context) {
    return context.dependOnInheritedWidgetOfExactType<ThemeProvider>();
  }
  
  @override
  bool updateShouldNotify(ThemeProvider oldWidget) {
    return isDark != oldWidget.isDark;
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ThemeProvider(
      isDark: true,
      child: MaterialApp(
        home: MyHomePage(),
      ),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final theme = ThemeProvider.of(context);
    
    if (theme == null) {
      return Text('ThemeProvider not found');
    }
    
    return Text(theme.isDark ? 'Dark Mode' : 'Light Mode');
  }
}
```

**Solution 2: Use `getElementForInheritedWidgetOfExactType` for non-reactive lookups**

```dart
import 'package:flutter/material.dart';

class MyData extends InheritedWidget {
  final String value;
  
  const MyData({super.key, required this.value, required super.child});
  
  static MyData? of(BuildContext context) {
    return context.dependOnInheritedWidgetOfExactType<MyData>();
  }
  
  // Non-reactive lookup — won't trigger rebuild
  static MyData? lookup(BuildContext context) {
    return context.getElementForInheritedWidgetOfExactType<MyData>()?.widget as MyData?;
  }
  
  @override
  bool updateShouldNotify(MyData old) => value != old.value;
}
```

**Solution 3: Use MultiProvider for multiple dependencies**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class CounterModel extends ChangeNotifier {
  int _count = 0;
  int get count => _count;
  
  void increment() {
    _count++;
    notifyListeners();
  }
}

class UserModel extends ChangeNotifier {
  String _name = 'Guest';
  String get name => _name;
  
  void setName(String name) {
    _name = name;
    notifyListeners();
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => CounterModel()),
        ChangeNotifierProvider(create: (_) => UserModel()),
      ],
      child: MaterialApp(home: MyHomePage()),
    );
  }
}
```

**Solution 4: Handle missing providers gracefully**

```dart
import 'package:flutter/material.dart';

class Config {
  final String apiUrl;
  const Config(this.apiUrl);
}

class ConfigProvider extends InheritedWidget {
  final Config config;
  
  const ConfigProvider({super.key, required this.config, required super.child});
  
  @override
  bool updateShouldNotify(ConfigProvider old) => config != old.config;
}

extension ConfigExtension on BuildContext {
  Config get config {
    final provider = dependOnInheritedWidgetOfExactType<ConfigProvider>();
    assert(provider != null, 'No ConfigProvider found in context');
    return provider!.config;
  }
}
```

**Solution 5: Create an inherited notifier**

```dart
import 'package:flutter/material.dart';

class CounterNotifier extends InheritedNotifier<ValueNotifier<int>> {
  const CounterNotifier({super.key, required ValueNotifier<int> notifier, required super.child})
      : super(notifier: notifier);
  
  static int of(BuildContext context) {
    return context.dependOnInheritedWidgetOfExactType<CounterNotifier>()!.notifier!.value;
  }
  
  @override
  bool updateShouldNotify(CounterNotifier old) => false;
}
```

## Examples

`dependOnInheritedWidgetOfExactType` registers a dependency so the widget rebuilds when the inherited widget changes. `getElementForInheritedWidgetOfExactType` does not register a dependency — useful for one-time lookups.

## Related Errors

- [Flutter Provider Error](/languages/dart/flutter-provider-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
