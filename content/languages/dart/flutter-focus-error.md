---
title: "[Solution] Flutter FocusNode Error — request, unfocus, FocusScope, nextFocus"
description: "Fix Flutter FocusNode errors from requestFocus, unfocus, FocusScope misuse, and focus traversal issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 161
---

FocusNode errors occur when focus is requested on disposed nodes, `FocusScope` is used incorrectly, or focus traversal fails.

## Common Causes

1. Calling `requestFocus` on a disposed `FocusNode`.
2. Using `FocusScope.of(context).unfocus()` incorrectly.
3. `FocusNode` not being disposed, causing memory leaks.
4. Circular focus dependencies.
5. `FocusScope` not being in the widget tree when accessed.

## How to Fix It

**Solution 1: Manage FocusNode lifecycle**

```dart
import 'package:flutter/material.dart';

class FocusDemo extends StatefulWidget {
  @override
  State<FocusDemo> createState() => _FocusDemoState();
}

class _FocusDemoState extends State<FocusDemo> {
  final FocusNode _focusNode = FocusNode();
  
  @override
  void dispose() {
    _focusNode.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return TextField(
      focusNode: _focusNode,
      decoration: InputDecoration(labelText: 'Focus here'),
    );
  }
}
```

**Solution 2: Request and unfocus safely**

```dart
import 'package:flutter/material.dart';

class FocusControls extends StatefulWidget {
  @override
  State<FocusControls> createState() => _FocusControlsState();
}

class _FocusControlsState extends State<FocusControls> {
  final FocusNode _node1 = FocusNode();
  final FocusNode _node2 = FocusNode();
  
  @override
  void dispose() {
    _node1.dispose();
    _node2.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextField(focusNode: _node1),
        TextField(focusNode: _node2),
        Row(
          children: [
            ElevatedButton(
              onPressed: () => _node1.requestFocus(),
              child: Text('Focus 1'),
            ),
            ElevatedButton(
              onPressed: () => _node2.requestFocus(),
              child: Text('Focus 2'),
            ),
            ElevatedButton(
              onPressed: () {
                FocusScope.of(context).unfocus();
              },
              child: Text('Unfocus'),
            ),
          ],
        ),
      ],
    );
  }
}
```

**Solution 3: Use FocusTraversalGroup for ordered focus**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return FocusTraversalGroup(
    child: Column(
      children: [
        TextField(),
        TextField(),
        TextField(),
      ],
    ),
  );
}
```

**Solution 4: Listen for focus changes**

```dart
import 'package:flutter/material.dart';

class FocusListener extends StatefulWidget {
  @override
  State<FocusListener> createState() => _FocusListenerState();
}

class _FocusListenerState extends State<FocusListener> {
  final FocusNode _focusNode = FocusNode();
  bool _isFocused = false;
  
  @override
  void initState() {
    super.initState();
    _focusNode.addListener(() {
      setState(() {
        _isFocused = _focusNode.hasFocus;
      });
    });
  }
  
  @override
  void dispose() {
    _focusNode.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          color: _isFocused ? Colors.blue : Colors.grey,
          width: 2,
        ),
      ),
      child: TextField(focusNode: _focusNode),
    );
  }
}
```

**Solution 5: Autofocus with delay**

```dart
import 'package:flutter/material.dart';

class AutoFocusField extends StatefulWidget {
  @override
  State<AutoFocusField> createState() => _AutoFocusFieldState();
}

class _AutoFocusFieldState extends State<AutoFocusField> {
  final FocusNode _focusNode = FocusNode();
  
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _focusNode.requestFocus();
    });
  }
  
  @override
  void dispose() {
    _focusNode.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return TextField(
      focusNode: _focusNode,
      autofocus: false,
    );
  }
}
```

## Examples

`FocusScope` is a `FocusNode` that manages a group of focusable widgets. Use `FocusScope.of(context)` to access the nearest focus scope. `requestFocus` on a `FocusNode` moves focus to that node.

## Related Errors

- [Flutter TextEditingController Error](/languages/dart/flutter-text-editing-controller-error/)
- [Flutter Form Validation Error](/languages/dart/flutter-form-validation-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
