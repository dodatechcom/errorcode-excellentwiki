---
title: "[Solution] Flutter Dialog Error — showDialog, AlertDialog, barrier dismiss, context"
description: "Fix Flutter showDialog errors from context issues, AlertDialog misuse, barrier dismiss, and dialog lifecycle."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 162
---

Dialog errors occur when `showDialog` is called with an invalid context, dialogs are not properly dismissed, or barrier behavior is incorrect.

## Common Causes

1. Calling `showDialog` with a context that has no `Navigator`.
2. Dialog callback executing after the widget is disposed.
3. `barrierDismissible: false` but no way to close the dialog.
4. Using `Navigator.pop` incorrectly to dismiss dialogs.
5. Multiple dialogs stacked without proper management.

## How to Fix It

**Solution 1: Show a basic dialog**

```dart
import 'package:flutter/material.dart';

void showConfirmDialog(BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext dialogContext) {
      return AlertDialog(
        title: Text('Confirm'),
        content: Text('Are you sure?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(dialogContext).pop(false),
            child: Text('Cancel'),
          ),
          TextButton(
            onPressed: () => Navigator.of(dialogContext).pop(true),
            child: Text('OK'),
          ),
        ],
      );
    },
  ).then((result) {
    if (result == true) {
      print('Confirmed');
    }
  });
}
```

**Solution 2: Handle barrier dismiss**

```dart
import 'package:flutter/material.dart';

void showNonDismissibleDialog(BuildContext context) {
  showDialog(
    context: context,
    barrierDismissible: false,
    builder: (BuildContext dialogContext) {
      return AlertDialog(
        title: Text('Important'),
        content: Text('You must acknowledge this.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(dialogContext).pop(),
            child: Text('OK'),
          ),
        ],
      );
    },
  );
}
```

**Solution 3: Return values from dialogs**

```dart
import 'package:flutter/material.dart';

Future<String?> showInputDialog(BuildContext context) {
  TextEditingController controller = TextEditingController();
  
  return showDialog<String>(
    context: context,
    builder: (BuildContext dialogContext) {
      return AlertDialog(
        title: Text('Enter Name'),
        content: TextField(
          controller: controller,
          decoration: InputDecoration(hintText: 'Name'),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(dialogContext).pop(),
            child: Text('Cancel'),
          ),
          TextButton(
            onPressed: () => Navigator.of(dialogContext).pop(controller.text),
            child: Text('OK'),
          ),
        ],
      );
    },
  );
}
```

**Solution 4: Show dialog safely after async operations**

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
      
      showDialog(
        context: context,
        builder: (context) => AlertDialog(
          content: Text('Appeared after delay'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: Text('OK'),
            ),
          ],
        ),
      );
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: _showAfterDelay,
      child: Text('Show Dialog'),
    );
  }
}
```

**Solution 5: Custom dialog with full control**

```dart
import 'package:flutter/material.dart';

Future<void> showCustomDialog(BuildContext context) async {
  await showGeneralDialog(
    context: context,
    barrierDismissible: true,
    barrierLabel: 'Dismiss',
    barrierColor: Colors.black54,
    transitionDuration: Duration(milliseconds: 300),
    pageBuilder: (context, animation, secondaryAnimation) {
      return Center(
        child: Card(
          margin: EdgeInsets.all(32),
          child: Padding(
            padding: EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text('Custom Dialog', style: TextStyle(fontSize: 20)),
                SizedBox(height: 16),
                ElevatedButton(
                  onPressed: () => Navigator.of(context).pop(),
                  child: Text('Close'),
                ),
              ],
            ),
          ),
        ),
      );
    },
    transitionBuilder: (context, animation, secondaryAnimation, child) {
      return ScaleTransition(
        scale: CurvedAnimation(parent: animation, curve: Curves.easeOut),
        child: child,
      );
    },
  );
}
```

## Examples

`showDialog` returns a `Future<T?>` that completes when the dialog is dismissed. Use `Navigator.of(context).pop(value)` to close the dialog and return a result.

## Related Errors

- [Flutter Bottom Sheet Error](/languages/dart/flutter-bottom-sheet-error/)
- [Flutter Navigator Push Error](/languages/dart/flutter-navigator-push-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
