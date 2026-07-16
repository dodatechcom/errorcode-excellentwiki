---
title: "Navigator error"
description: "Flutter throws an error when Navigator operations are called with invalid routes or on a disposed NavigatorState"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["navigator", "navigation", "route", "push", "pop"]
weight: 5
---

This error occurs when Flutter's Navigator cannot complete a navigation operation because the route does not exist, the Navigator is not available, or a `pop` is called when there is no route to pop.

## Common Causes

- `Navigator.of(context)` called with a context not under a Navigator
- Trying to pop the last route (no previous route)
- Pushing a named route that is not defined in the MaterialApp routes
- Using `Navigator.pop` after the route has already been popped

## How to Fix

1. Verify the context belongs to a Navigator:

```dart
// Ensure context has a Navigator ancestor
Navigator.of(context).push(
  MaterialPageRoute(builder: (_) => DetailScreen()),
);
```

2. Check before popping:

```dart
if (Navigator.canPop(context)) {
  Navigator.of(context).pop();
} else {
  Navigator.of(context).pushReplacementNamed('/home');
}
```

3. Define all named routes in `MaterialApp`:

```dart
MaterialApp(
  routes: {
    '/': (context) => HomeScreen(),
    '/settings': (context) => SettingsScreen(),
    '/profile': (context) => ProfileScreen(),
  },
);
```

4. Use a try-catch for navigation operations:

```dart
try {
  Navigator.of(context).pushNamed('/settings');
} catch (e) {
  debugPrint('Navigation error: $e');
}
```

## Examples

```dart
// No routes defined in MaterialApp
MaterialApp(
  home: HomeScreen(),
);

Navigator.of(context).pushNamed('/settings');
// Error: '/settings' is not defined
```

```text
FlutterError: Navigator operation requested with a context that does not include a Navigator.
```

## Related Errors

- [setState after dispose]({{< relref "/frameworks/flutter/widget-error" >}})
