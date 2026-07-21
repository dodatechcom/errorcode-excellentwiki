---
title: "[Solution] Flutter ScaffoldMessenger SnackBar Error"
description: "Fix Flutter ScaffoldMessenger SnackBar errors when snack bars do not appear or are dismissed by navigation."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A ScaffoldMessenger SnackBar error in Flutter occurs when the `SnackBar` does not display because the `ScaffoldMessenger` cannot find a `Scaffold`, or the SnackBar is dismissed when navigating to a new screen.

## Common Causes

- `ScaffoldMessenger.of(context)` called with a context above the `Scaffold`
- `ScaffoldMessenger` does not exist in the widget tree
- SnackBar shown on a screen that is about to be disposed by navigation
- `SnackBar` duration too short and auto-dismisses before user reads it
- Multiple SnackBars queued and previous ones are lost

## How to Fix

1. Show SnackBar with proper context:

```dart
void showMessage(BuildContext context, String message) {
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      content: Text(message),
      duration: const Duration(seconds: 3),
      action: SnackBarAction(
        label: 'DISMISS',
        onPressed: () {
          ScaffoldMessenger.of(context).hideCurrentSnackBar();
        },
      ),
    ),
  );
}
```

2. Persist SnackBar across navigation:

```dart
// Create a global messenger key
final messengerKey = GlobalKey<ScaffoldMessengerState>();

MaterialApp(
  scaffoldMessengerKey: messengerKey,
  // ...
);

// Show SnackBar from anywhere
messengerKey.currentState?.showSnackBar(
  SnackBar(content: Text('Item saved')),
);
```

3. Use SnackBar with clear feedback:

```dart
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: Row(
      children: [
        Icon(Icons.check_circle, color: Colors.green),
        SizedBox(width: 8),
        Text('Changes saved successfully'),
      ],
    ),
    duration: Duration(seconds: 2),
    behavior: SnackBarBehavior.floating,
    margin: EdgeInsets.all(8),
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
  ),
);
```

## Examples

```dart
// Bug: showing SnackBar after navigating away
Navigator.push(context, MaterialPageRoute(builder: (_) => NextScreen()));
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(content: Text('Done')), // Screen disposed -- no SnackBar
);

// Fixed: show before navigation
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(content: Text('Done')),
);
Navigator.push(context, MaterialPageRoute(builder: (_) => NextScreen()));
```

```text
Scaffold.of() called with a context that does not include a Scaffold.
```
