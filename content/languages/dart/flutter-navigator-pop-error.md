---
title: "[Solution] Flutter Navigator.pop Error — result, canPop, maybePop"
description: "Fix Flutter Navigator.pop errors from popping with results, canPop checks, maybePop, and root navigator."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 166
---

Navigator pop errors occur when popping from the root route, returning incorrect types, or not handling `canPop` properly.

## Common Causes

1. Calling `Navigator.pop` on the root route (no route to pop to).
2. Popping with a result type that the caller does not expect.
3. Using `Navigator.of(context).pop()` when `canPop` is false.
4. Forgetting to pop dialogs before popping the page.
5. Using `maybePop` when `pop` is more appropriate.

## How to Fix It

**Solution 1: Pop with a result**

```dart
import 'package:flutter/material.dart';

class SelectionPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Select')),
      body: ListView(
        children: [
          ListTile(
            title: Text('Option A'),
            onTap: () => Navigator.pop(context, 'A'),
          ),
          ListTile(
            title: Text('Option B'),
            onTap: () => Navigator.pop(context, 'B'),
          ),
        ],
      ),
    );
  }
}

// Caller
void openSelection(BuildContext context) async {
  final result = await Navigator.push<String>(
    context,
    MaterialPageRoute(builder: (_) => SelectionPage()),
  );
  
  if (result != null) {
    print('Selected: $result');
  }
}
```

**Solution 2: Check canPop before popping**

```dart
import 'package:flutter/material.dart';

class SafePopWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            if (Navigator.canPop(context)) {
              Navigator.pop(context);
            } else {
              // Handle no-route case
              print('Cannot pop — root route');
            }
          },
        ),
      ),
      body: Center(child: Text('Page')),
    );
  }
}
```

**Solution 3: Use maybePop for conditional navigation**

```dart
import 'package:flutter/material.dart';

class UnsavedChangesPage extends StatefulWidget {
  @override
  State<UnsavedChangesPage> createState() => _UnsavedChangesPageState();
}

class _UnsavedChangesPageState extends State<UnsavedChangesPage> {
  bool _hasUnsavedChanges = true;
  
  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: !_hasUnsavedChanges,
      onPopInvokedWithResult: (didPop, result) {
        if (!didPop && _hasUnsavedChanges) {
          _showDiscardDialog(context);
        }
      },
      child: Scaffold(
        appBar: AppBar(title: Text('Edit')),
        body: TextField(
          onChanged: (_) => setState(() => _hasUnsavedChanges = true),
        ),
      ),
    );
  }
  
  void _showDiscardDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Discard changes?'),
        content: Text('Unsaved changes will be lost.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text('Cancel'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context); // Close dialog
              Navigator.pop(context); // Go back
            },
            child: Text('Discard'),
          ),
        ],
      ),
    );
  }
}
```

**Solution 4: Pop the root navigator from a nested navigator**

```dart
import 'package:flutter/material.dart';

void popRootNavigator(BuildContext context) {
  Navigator.of(context, rootNavigator: true).pop();
}
```

**Solution 5: Handle pop with default value**

```dart
import 'package:flutter/material.dart';

void openAndHandleResult(BuildContext context) async {
  String? result = await Navigator.push<String>(
    context,
    MaterialPageRoute(builder: (_) => SelectionPage()),
  );
  
  // Handle null result (user pressed back without selecting)
  String selected = result ?? 'Default';
  print('Result: $selected');
}

class SelectionPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ElevatedButton(
          onPressed: () => Navigator.pop(context, 'chosen'),
          child: Text('Select'),
        ),
      ),
    );
  }
}
```

## Examples

`PopScope` (Flutter 3.16+) replaces the deprecated `WillPopScope`. Use `canPop` to control whether `Navigator.pop` is allowed, and `onPopInvokedWithResult` to handle the result.

## Related Errors

- [Flutter Navigator Push Error](/languages/dart/flutter-navigator-push-error/)
- [Flutter Route Generator Error](/languages/dart/flutter-route-generator-error/)
- [Flutter Dialog Error](/languages/dart/flutter-dialog-error/)
