---
title: "[Solution] Flutter Provider Error — context.read/watch/select, MultiProvider"
description: "Fix Flutter Provider errors from incorrect context.read/watch/select usage, MultiProvider configuration, and provider disposal."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 181
---

Provider errors occur when providers are not found in the tree, `read` vs `watch` is misused, or `MultiProvider` order causes issues.

## Common Causes

1. `context.read` used in `build()` instead of `context.watch`.
2. `context.watch` used in callbacks instead of `context.read`.
3. Provider not being above the consumer in the widget tree.
4. `MultiProvider` with wrong provider order.
5. `ChangeNotifierProvider` not disposing the notifier.

## How to Fix It

**Solution 1: Use read and watch correctly**

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

class CounterWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // watch — rebuilds when value changes
    int count = context.watch<CounterModel>().count;
    
    return Column(
      children: [
        Text('Count: $count'),
        ElevatedButton(
          onPressed: () {
            // read — one-time access, does not rebuild
            context.read<CounterModel>().increment();
          },
          child: Text('Increment'),
        ),
      ],
    );
  }
}

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => CounterModel(),
      child: MaterialApp(home: CounterWidget()),
    ),
  );
}
```

**Solution 2: Use select for targeted rebuilds**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class UserModel extends ChangeNotifier {
  String _name = 'Guest';
  int _age = 0;
  
  String get name => _name;
  int get age => _age;
  
  void setName(String name) {
    _name = name;
    notifyListeners();
  }
  
  void setAge(int age) {
    _age = age;
    notifyListeners();
  }
}

class NameWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Only rebuilds when 'name' changes
    String name = context.select<UserModel, String>((m) => m.name);
    return Text('Name: $name');
  }
}

class AgeWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Only rebuilds when 'age' changes
    int age = context.select<UserModel, int>((m) => m.age);
    return Text('Age: $age');
  }
}
```

**Solution 3: Configure MultiProvider**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => UserModel()),
        ChangeNotifierProvider(create: (_) => CounterModel()),
        Provider.value(value: 'API_KEY'),
      ],
      child: MaterialApp(home: MyApp()),
    ),
  );
}
```

**Solution 4: Use context.read in callbacks**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class CallbackWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        // read in callbacks — safe and does not rebuild
        final model = context.read<UserModel>();
        model.setName('Alice');
      },
      child: Text('Set Name'),
    );
  }
}
```

**Solution 5: ProxyProvider for dependent providers**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class ApiClient {
  final String baseUrl;
  ApiClient(this.baseUrl);
}

class UserService {
  final ApiClient client;
  UserService(this.client);
}

void main() {
  runApp(
    MultiProvider(
      providers: [
        Provider(create: (_) => ApiClient('https://api.example.com')),
        ProxyProvider<ApiClient, UserService>(
          update: (_, client, __) => UserService(client),
        ),
      ],
      child: MyApp(),
    ),
  );
}
```

## Examples

`context.watch<T>()` registers a dependency and rebuilds the widget when T changes. `context.read<T>()` returns T without registering a dependency — use it in event handlers.

## Related Errors

- [Flutter Inherited Widget Error](/languages/dart/flutter-inherited-widget-error/)
- [Flutter Riverpod Error](/languages/dart/flutter-riverpod-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
