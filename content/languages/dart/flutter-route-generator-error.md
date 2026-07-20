---
title: "[Solution] Flutter Route Generator Error — onGenerateRoute, initialRoute, unknownRoute"
description: "Fix Flutter route generator errors from onGenerateRoute failures, initialRoute issues, and unknownRoute handling."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 167
---

Route generator errors occur when `onGenerateRoute` returns null, `initialRoute` does not match any route, or `unknownRoute` is not configured.

## Common Causes

1. `onGenerateRoute` returning `null` for unhandled routes.
2. `initialRoute` not being `/` or not defined in routes.
3. Missing `unknownRoute` for invalid route names.
4. Route arguments not being properly extracted.
5. Deep link routes not matching any defined pattern.

## How to Fix It

**Solution 1: Implement onGenerateRoute**

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      onGenerateRoute: (RouteSettings settings) {
        switch (settings.name) {
          case '/':
            return MaterialPageRoute(builder: (_) => HomePage());
          case '/profile':
            final args = settings.arguments as String?;
            return MaterialPageRoute(
              builder: (_) => ProfilePage(userId: args ?? 'guest'),
            );
          case '/settings':
            return MaterialPageRoute(builder: (_) => SettingsPage());
          default:
            return MaterialPageRoute(builder: (_) => UnknownPage());
        }
      },
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(body: Text('Home'));
}

class ProfilePage extends StatelessWidget {
  final String userId;
  const ProfilePage({super.key, required this.userId});
  @override
  Widget build(BuildContext context) => Scaffold(body: Text('Profile: $userId'));
}

class SettingsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(body: Text('Settings'));
}

class UnknownPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(body: Text('404'));
}
```

**Solution 2: Handle unknownRoute**

```dart
import 'package:flutter/material.dart';

MaterialApp(
  onUnknownRoute: (settings) {
    return MaterialPageRoute(
      builder: (_) => Scaffold(
        body: Center(
          child: Text('Route not found: ${settings.name}'),
        ),
      ),
    );
  },
);
```

**Solution 3: Use onGenerateInitialRoutes for deep linking**

```dart
import 'package:flutter/material.dart';

MaterialApp(
  onGenerateInitialRoutes: (initialRoute) {
    // Handle deep links like /profile/123
    List<String> segments = initialRoute.split('/');
    
    List<Route<dynamic>> routes = [];
    
    if (segments.length > 2 && segments[1] == 'profile') {
      routes.add(MaterialPageRoute(builder: (_) => HomePage()));
      routes.add(MaterialPageRoute(
        builder: (_) => ProfilePage(userId: segments[2]),
      ));
    } else {
      routes.add(MaterialPageRoute(builder: (_) => HomePage()));
    }
    
    return routes;
  },
);
```

**Solution 4: Use GoRouter for complex navigation**

```dart
import 'package:flutter/material.dart';
// import 'package:go_router/go_router.dart';

// Example with GoRouter (add go_router to pubspec.yaml)
// final router = GoRouter(
//   routes: [
//     GoRoute(path: '/', builder: (context, state) => HomePage()),
//     GoRoute(
//       path: '/profile/:id',
//       builder: (context, state) => ProfilePage(
//         userId: state.pathParameters['id']!,
//       ),
//     ),
//   ],
// );
```

**Solution 5: Extract arguments from RouteSettings**

```dart
import 'package:flutter/material.dart';

class PageArgs {
  final String title;
  final int id;
  PageArgs({required this.title, required this.id});
}

Route<dynamic> generateRoute(RouteSettings settings) {
  switch (settings.name) {
    case '/detail':
      final args = settings.arguments as PageArgs?;
      return MaterialPageRoute(
        builder: (_) => Scaffold(
          body: Center(child: Text('${args?.title} #${args?.id}')),
        ),
      );
    default:
      return MaterialPageRoute(
        builder: (_) => Scaffold(body: Text('Not found')),
      );
  }
}
```

## Examples

`onGenerateRoute` is called for every `Navigator.pushNamed` call. Return `null` to let the normal route table handle it. `initialRoute` must start with `/`.

## Related Errors

- [Flutter Navigator Push Error](/languages/dart/flutter-navigator-push-error/)
- [Flutter Navigator Pop Error](/languages/dart/flutter-navigator-pop-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
