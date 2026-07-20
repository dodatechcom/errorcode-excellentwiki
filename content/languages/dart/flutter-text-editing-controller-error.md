---
title: "[Solution] Flutter TextEditingController Error — dispose, listener, selection"
description: "Fix Flutter TextEditingController errors from disposal, listener management, selection issues, and text updates."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 160
---

TextEditingController errors occur when controllers are not disposed, listeners cause loops, or text is set incorrectly.

## Common Causes

1. Not disposing `TextEditingController`, causing memory leaks.
2. Adding a listener that triggers `setState` in a loop.
3. Setting `text` while the field has focus, disrupting cursor position.
4. Accessing `selection` before the controller is attached to a field.
5. Modifying controller in `build()` method causing rebuilds.

## How to Fix It

**Solution 1: Initialize and dispose properly**

```dart
import 'package:flutter/material.dart';

class MyForm extends StatefulWidget {
  @override
  State<MyForm> createState() => _MyFormState();
}

class _MyFormState extends State<MyForm> {
  final TextEditingController _controller = TextEditingController();
  
  @override
  void initState() {
    super.initState();
    _controller.text = 'Initial value';
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return TextField(controller: _controller);
  }
}
```

**Solution 2: Add listeners safely**

```dart
import 'package:flutter/material.dart';

class SearchField extends StatefulWidget {
  @override
  State<SearchField> createState() => _SearchFieldState();
}

class _SearchFieldState extends State<SearchField> {
  final TextEditingController _controller = TextEditingController();
  
  @override
  void initState() {
    super.initState();
    _controller.addListener(_onTextChanged);
  }
  
  void _onTextChanged() {
    // Debounce or validate without setState if possible
    print('Text: ${_controller.text}');
  }
  
  @override
  void dispose() {
    _controller.removeListener(_onTextChanged);
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return TextField(controller: _controller);
  }
}
```

**Solution 3: Set text with selection control**

```dart
import 'package:flutter/material.dart';

class SmartField extends StatefulWidget {
  @override
  State<SmartField> createState() => _SmartFieldState();
}

class _SmartFieldState extends State<SmartField> {
  final TextEditingController _controller = TextEditingController();
  
  void _autoFormat() {
    String text = _controller.text;
    int cursorPos = _controller.selection.baseOffset;
    
    // Apply formatting
    String formatted = text.toUpperCase();
    
    _controller.value = TextEditingValue(
      text: formatted,
      selection: TextSelection.collapsed(
        offset: cursorPos.clamp(0, formatted.length),
      ),
    );
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _controller,
      onChanged: (_) => _autoFormat(),
    );
  }
}
```

**Solution 4: Clear text field safely**

```dart
import 'package:flutter/material.dart';

class ClearableField extends StatefulWidget {
  @override
  State<ClearableField> createState() => _ClearableFieldState();
}

class _ClearableFieldState extends State<ClearableField> {
  final TextEditingController _controller = TextEditingController();
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _controller,
      decoration: InputDecoration(
        hintText: 'Type here...',
        suffixIcon: IconButton(
          icon: Icon(Icons.clear),
          onPressed: () {
            _controller.clear();
          },
        ),
      ),
    );
  }
}
```

**Solution 5: Use TextEditingController with validator**

```dart
import 'package:flutter/material.dart';

class ValidatedField extends StatefulWidget {
  @override
  State<ValidatedField> createState() => _ValidatedFieldState();
}

class _ValidatedFieldState extends State<ValidatedField> {
  final TextEditingController _controller = TextEditingController();
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            controller: _controller,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter text';
              }
              return null;
            },
          ),
          ElevatedButton(
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                print('Valid: ${_controller.text}');
              }
            },
            child: Text('Submit'),
          ),
        ],
      ),
    );
  }
}
```

## Examples

`TextEditingController` extends `ValueNotifier<TextEditingValue>`. When you add a listener, it fires on every text change — be careful not to trigger infinite rebuilds.

## Related Errors

- [Flutter Form Validation Error](/languages/dart/flutter-form-validation-error/)
- [Flutter Focus Error](/languages/dart/flutter-focus-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
