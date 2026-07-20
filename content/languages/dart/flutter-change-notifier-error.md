---
title: "[Solution] Flutter ChangeNotifier Error — notifyListeners, dispose, ListenableBuilder"
description: "Fix Flutter ChangeNotifier errors from notification ordering, disposal, listener management, and ListenableBuilder usage."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 186
---

ChangeNotifier errors occur when `notifyListeners` is called during disposal, listeners are not properly managed, or notification triggers recursive rebuilds.

## Common Causes

1. Calling `notifyListeners()` in `dispose()`.
2. Adding/removing listeners during notification iteration.
3. Not disposing the ChangeNotifier, causing memory leaks.
4. Recursive `notifyListeners` calls.
5. Not checking `hasListeners` before calling `notifyListeners`.

## How to Fix It

**Solution 1: Create a proper ChangeNotifier**

```dart
import 'package:flutter/material.dart';

class TodoModel extends ChangeNotifier {
  final List<String> _todos = [];
  
  List<String> get todos => List.unmodifiable(_todos);
  
  void add(String todo) {
    _todos.add(todo);
    notifyListeners();
  }
  
  void remove(String todo) {
    _todos.remove(todo);
    notifyListeners();
  }
  
  void toggle(int index) {
    // Example mutation
    notifyListeners();
  }
}

class TodoListWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: TodoModel()..add('Item 1')..add('Item 2'),
      builder: (context, child) {
        return Text('Todos loaded');
      },
    );
  }
}
```

**Solution 2: Use with ChangeNotifierProvider**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class CartModel extends ChangeNotifier {
  final List<String> _items = [];
  
  int get count => _items.length;
  
  void add(String item) {
    _items.add(item);
    notifyListeners();
  }
  
  void remove(String item) {
    _items.remove(item);
    notifyListeners();
  }
  
  @override
  void dispose() {
    // Clean up resources but don't call notifyListeners
    super.dispose();
  }
}

class CartWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => CartModel(),
      child: Builder(
        builder: (context) {
          return Column(
            children: [
              Consumer<CartModel>(
                builder: (context, cart, child) {
                  return Text('Items: ${cart.count}');
                },
              ),
              ElevatedButton(
                onPressed: () {
                  context.read<CartModel>().add('New Item');
                },
                child: Text('Add Item'),
              ),
            ],
          );
        },
      ),
    );
  }
}
```

**Solution 3: Avoid notifyListeners during dispose**

```dart
import 'package:flutter/material.dart';

class SafeNotifier extends ChangeNotifier {
  bool _isDisposed = false;
  
  void updateData(String data) {
    if (_isDisposed) return;
    // Update data
    notifyListeners();
  }
  
  @override
  void dispose() {
    _isDisposed = true;
    super.dispose(); // Never call notifyListeners here
  }
}
```

**Solution 4: Use ListenableBuilder for efficient rebuilds**

```dart
import 'package:flutter/material.dart';

class AnimationModel extends ChangeNotifier {
  double _progress = 0;
  double get progress => _progress;
  
  void setProgress(double value) {
    _progress = value.clamp(0.0, 1.0);
    notifyListeners();
  }
}

class ProgressBarWidget extends StatelessWidget {
  final AnimationModel model = AnimationModel();
  
  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: model,
      builder: (context, child) {
        return LinearProgressIndicator(value: model.progress);
      },
    );
  }
}
```

**Solution 5: Compose multiple ChangeNotifiers**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class SettingsModel extends ChangeNotifier {
  bool _darkMode = false;
  String _language = 'en';
  
  bool get darkMode => _darkMode;
  String get language => _language;
  
  void toggleDarkMode() {
    _darkMode = !_darkMode;
    notifyListeners();
  }
  
  void setLanguage(String lang) {
    _language = lang;
    notifyListeners();
  }
}

class SettingsWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => SettingsModel(),
      child: Consumer<SettingsModel>(
        builder: (context, settings, _) {
          return Column(
            children: [
              Switch(
                value: settings.darkMode,
                onChanged: (_) => settings.toggleDarkMode(),
              ),
              DropdownButton<String>(
                value: settings.language,
                items: [
                  DropdownMenuItem(value: 'en', child: Text('English')),
                  DropdownMenuItem(value: 'es', child: Text('Spanish')),
                ],
                onChanged: (v) {
                  if (v != null) settings.setLanguage(v);
                },
              ),
            ],
          );
        },
      ),
    );
  }
}
```

## Examples

`ChangeNotifier` is a simple class that can be extended to provide change notification using the `Listenable` interface. It's the foundation for Provider's `ChangeNotifierProvider`.

## Related Errors

- [Flutter Value Notifier Error](/languages/dart/flutter-value-notifier-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
- [Flutter Provider Error](/languages/dart/flutter-provider-error/)
