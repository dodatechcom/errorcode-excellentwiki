---
title: "Navigator.pop called with no routes"
description: "Flutter throws an error when Navigator.pop is called but there are no routes in the navigation stack to pop"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["navigator", "navigation", "pop", "route", "stack"]
weight: 5
---

This error occurs when `Navigator.pop(context)` is called but the current Navigator has no routes on its stack. This typically happens when a dialog or route is dismissed programmatically but the Navigator stack is empty.

## Common Causes

- Dialog dismissed after the parent route was already popped
- Multiple calls to `Navigator.pop` for the same route
- Using the wrong `BuildContext` to get the Navigator
- Back button handling on the root route
- Using `Navigator.pushReplacement` and then calling `pop`

## How to Fix

1. Check if the route can be popped before popping:

```dart
if (Navigator.of(context).canPop()) {
  Navigator.of(context).pop();
}
```

2. Use `Navigator.of(context, rootNavigator: true)` for dialogs:

```dart
// When showing a dialog over nested Navigators
Navigator.of(context, rootNavigator: true).pop();
```

3. Use `MaybePopScope` to handle back navigation:

```dart
class MyScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (didPop) return;
        // Custom back handling
        Navigator.of(context).maybePop();
      },
      child: Scaffold(...),
    );
  }
}
```

4. Use named routes with proper routing:

```dart
MaterialApp(
  routes: {
    '/': (context) => HomeScreen(),
    '/details': (context) => DetailsScreen(),
  },
  initialRoute: '/',
);
```

## Examples

```dart
// Dismissing a dialog after the route was already popped
Navigator.of(context).pop(); // First pop — closes dialog
Navigator.of(context).pop(); // Second pop — NavigatorError
```

## Related Errors

- [Platform error]({{< relref "/frameworks/flutter/platform-error" >}})
- [State error]({{< relref "/frameworks/flutter/state-error3" >}})
