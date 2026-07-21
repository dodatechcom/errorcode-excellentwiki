---
title: "[Solution] Flutter Navigator Route Not Found Error"
description: "Fix Flutter Navigator route not found errors when pushing a named route that is not registered in the route table."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Navigator route not found error in Flutter occurs when `Navigator.pushNamed` is called with a route name that does not exist in the `MaterialApp.routes` map, causing a runtime error.

## Common Causes

- Route name typo in `Navigator.pushNamed`
- Route not registered in `MaterialApp.routes`
- Using `pushNamed` when `routes` map is defined but route does not exist
- Dynamic routes not handled by `onGenerateRoute`
- Route name includes leading `/` inconsistently

## How to Fix

1. Define all routes in the routes map:

```dart
MaterialApp(
  routes: {
    '/': (context) => HomeScreen(),
    '/login': (context) => LoginScreen(),
    '/profile': (context) => ProfileScreen(),
    '/settings': (context) => SettingsScreen(),
  },
);
```

2. Use `onGenerateRoute` for dynamic routes:

```dart
MaterialApp(
  onGenerateRoute: (RouteSettings settings) {
    final routes = {
      '/': (context) => HomeScreen(),
      '/login': (context) => LoginScreen(),
    };

    final builder = routes[settings.name];
    if (builder != null) {
      return MaterialPageRoute(builder: builder, settings: settings);
    }

    // Fallback for unknown routes
    return MaterialPageRoute(
      builder: (_) => NotFoundScreen(route: settings.name),
    );
  },
);
```

3. Use route constants to avoid typos:

```dart
class Routes {
  static const home = '/';
  static const login = '/login';
  static const profile = '/profile';
  static const settings = '/settings';
}

// Usage
Navigator.pushNamed(context, Routes.profile);
```

## Examples

```dart
// Bug: typo in route name
Navigator.pushNamed(context, '/profil'); // Missing 'e'

// Fixed: use route constant
Navigator.pushNamed(context, Routes.profile);
```

```text
Navigator operation requested with a context that does not include a Navigator.
Could not find a generator for route RouteSettings("/profil")
```
