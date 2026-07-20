---
title: "[Solution] Flutter Navigator.push Error — push, pushNamed, pushReplacement, routes"
description: "Fix Flutter Navigator push errors from pushNamed failures, pushReplacement misuse, and route configuration issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 165
---

Navigator push errors occur when routes are not defined, `pushNamed` is used with an unregistered route, or `pushReplacement` causes unexpected navigation stack changes.

## Common Causes

1. `pushNamed` used with a route not defined in `routes` or `onGenerateRoute`.
2. `pushReplacement` removing needed routes from the stack.
3. Passing invalid arguments to named routes.
4. Using `Navigator.push` with a context that has no `Navigator`.
5. Route name typos causing silent failures.

## How to Fix It

**Solution 1: Push with MaterialPageRoute**

```dart
import 'package:flutter/material.dart';

void navigateToDetails(BuildContext context, int id) {
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => DetailPage(id: id),
    ),
  );
}

class DetailPage extends StatelessWidget {
  final int id;
  const DetailPage({super.key, required this.id});
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Detail $id')),
      body: Center(child: Text('Item $id')),
    );
  }
}
```

**Solution 2: Use pushNamed with route table**

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    initialRoute: '/',
    routes: {
      '/': (context) => HomePage(),
      '/settings': (context) => SettingsPage(),
    },
    onGenerateRoute: (settings) {
      if (settings.name == '/detail') {
        final args = settings.arguments as int?;
        return MaterialPageRoute(
          builder: (context) => DetailPage(id: args ?? 0),
        );
      }
      return null;
    },
  ));
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ElevatedButton(
          onPressed: () => Navigator.pushNamed(context, '/detail', arguments: 42),
          child: Text('Go to Detail'),
        ),
      ),
    );
  }
}

class SettingsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(appBar: AppBar(title: Text('Settings')));
}

class DetailPage extends StatelessWidget {
  final int id;
  const DetailPage({super.key, required this.id});
  @override
  Widget build(BuildContext context) => Scaffold(body: Center(child: Text('Detail $id')));
}
```

**Solution 3: Use pushReplacement correctly**

```dart
import 'package:flutter/material.dart';

void login(BuildContext context) {
  // Replace login page so back button doesn't return to it
  Navigator.pushReplacement(
    context,
    MaterialPageRoute(builder: (context) => HomePage()),
  );
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Home')),
      body: Center(child: Text('Welcome')),
    );
  }
}
```

**Solution 4: Pass arguments safely**

```dart
import 'package:flutter/material.dart';

class UserArguments {
  final String name;
  final int age;
  UserArguments({required this.name, required this.age});
}

void navigateToProfile(BuildContext context) {
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => ProfilePage(),
      settings: RouteSettings(
        arguments: UserArguments(name: 'Alice', age: 30),
      ),
    ),
  );
}

class ProfilePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final args = ModalRoute.of(context)!.settings.arguments as UserArguments;
    return Scaffold(
      body: Center(child: Text('${args.name}, ${args.age}')),
    );
  }
}
```

**Solution 5: Handle pushAndRemoveUntil**

```dart
import 'package:flutter/material.dart';

void navigateToHomeAndClearStack(BuildContext context) {
  Navigator.pushAndRemoveUntil(
    context,
    MaterialPageRoute(builder: (context) => HomePage()),
    (route) => false, // Remove all routes
  );
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(body: Center(child: Text('Home')));
  }
}
```

## Examples

`Navigator.push` adds a route to the stack. `pushReplacement` replaces the current route. `pushNamed` uses the route table for navigation. Always ensure routes are properly registered.

## Related Errors

- [Flutter Navigator Pop Error](/languages/dart/flutter-navigator-pop-error/)
- [Flutter Route Generator Error](/languages/dart/flutter-route-generator-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
