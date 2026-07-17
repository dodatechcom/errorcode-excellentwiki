---
title: "Navigator - pop with no routes"
description: "Flutter throws Navigator pop error when trying to pop a route from an empty navigation stack"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The "Navigator.pop with no routes" error occurs when `Navigator.of(context).pop()` is called but there are no routes left on the navigation stack. This typically happens when the last route in the stack is popped, or when pop is called from a context that has no navigator.

## Common Causes

- Calling pop on the root route of the app
- Using Navigator.pop after Navigator.pushAndRemoveUntil
- Multiple pop calls in response to a single event
- Back button handling conflicts with manual pop
- Modal route popped twice

## How to Fix

1. Check if the route can be popped before calling pop:

```dart
if (Navigator.of(context).canPop()) {
  Navigator.of(context).pop();
}
```

2. Use `maybePop` instead of `pop`:

```dart
Navigator.of(context).maybePop();
```

3. Handle the root route case explicitly:

```dart
void goBack(BuildContext context) {
  if (Navigator.of(context).canPop()) {
    Navigator.of(context).pop();
  } else {
    // Handle root route - exit app or show home
    SystemNavigator.pop();
  }
}
```

4. Use named routes with proper guards:

```dart
Navigator.of(context).popUntil((route) => route.isFirst);
```

5. Check route count before popping:

```dart
final routes = ModalRoute.of(context);
if (routes != null && Navigator.of(context).canPop()) {
  Navigator.of(context).pop();
}
```

## Examples

```dart
// Error: pop called twice
onPressed: () {
  Navigator.of(context).pop(); // first pop
  Navigator.of(context).pop(); // second pop - error!
},

// Fix: pop once
onPressed: () {
  Navigator.of(context).pop();
},
```

```dart
// Error: pop on root route
Navigator.of(context).pop(); // when at root screen

// Fix: check first
if (Navigator.of(context).canPop()) {
  Navigator.of(context).pop();
} else {
  SystemNavigator.pop();
}
```

## Related Errors

- [Platform error]({{< relref "/frameworks/flutter/flutter-platform-error-v2" >}})
- [State error]({{< relref "/frameworks/flutter/flutter-state-error-v2" >}})
