---
title: "[Solution] Flutter SnackBar Error — ScaffoldMessenger, dismiss, Scaffold.of"
description: "Fix Flutter SnackBar errors from ScaffoldMessenger usage, dismiss behavior, and Scaffold.of context issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 164
---

SnackBar errors occur when using deprecated `Scaffold.of`, failing to use `ScaffoldMessenger`, or incorrect dismiss behavior.

## Common Causes

1. Using `Scaffold.of(context)` which is deprecated in favor of `ScaffoldMessenger`.
2. Calling `showSnackBar` after the Scaffold is disposed.
3. Not handling `SnackBar` dismissal properly.
4. Multiple `SnackBar` calls overwriting each other.
5. `SnackBar` shown during build phase.

## How to Fix It

**Solution 1: Use ScaffoldMessenger correctly**

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Hello!')),
        );
      },
      child: Text('Show SnackBar'),
    );
  }
}
```

**Solution 2: Dismiss SnackBar before showing a new one**

```dart
import 'package:flutter/material.dart';

void showMessage(BuildContext context, String message) {
  ScaffoldMessenger.of(context).clearSnackBars();
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      content: Text(message),
      duration: Duration(seconds: 2),
    ),
  );
}
```

**Solution 3: Add action to SnackBar**

```dart
import 'package:flutter/material.dart';

void showUndoSnackBar(BuildContext context) {
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      content: Text('Item deleted'),
      action: SnackBarAction(
        label: 'UNDO',
        onPressed: () {
          print('Undo clicked');
        },
      ),
      duration: Duration(seconds: 4),
    ),
  );
}
```

**Solution 4: Safe SnackBar after async operation**

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  void _showAfterDelay() {
    Future.delayed(Duration(seconds: 2), () {
      if (!mounted) return;
      
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Completed!')),
      );
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _showAfterDelay,
      child: Text('Start Task'),
    );
  }
}
```

**Solution 5: Custom SnackBar with close icon**

```dart
import 'package:flutter/material.dart';

void showDismissibleSnackBar(BuildContext context) {
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      content: Row(
        children: [
          Icon(Icons.info, color: Colors.white),
          SizedBox(width: 8),
          Expanded(child: Text('This is an info message')),
        ],
      ),
      behavior: SnackBarBehavior.floating,
      margin: EdgeInsets.all(8),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      duration: Duration(seconds: 3),
    ),
  );
}
```

## Examples

`ScaffoldMessenger.of(context)` finds the nearest `ScaffoldMessenger` ancestor, which manages snack bars for the current `Scaffold`. Always use it instead of the deprecated `Scaffold.of`.

## Related Errors

- [Flutter Dialog Error](/languages/dart/flutter-dialog-error/)
- [Flutter Bottom Sheet Error](/languages/dart/flutter-bottom-sheet-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
