---
title: "[Solution] Flutter Form Validation Error — FormState validate, autovalidate"
description: "Fix Flutter form validation errors from FormState validate, GlobalKey<FormState>, autovalidateMode, and validator patterns."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 168
---

Form validation errors occur when `FormState.validate` is called without proper validators, `GlobalKey<FormState>` is reused incorrectly, or auto-validation triggers unexpectedly.

## Common Causes

1. `FormState.validate()` called when form key is not attached to a `Form`.
2. Validator returning `null` when it should return an error message.
3. `GlobalKey<FormState>` reused across multiple forms.
4. `AutovalidateMode.always` showing errors before user interaction.
5. Not calling `FormState.save()` to collect field values.

## How to Fix It

**Solution 1: Create a validated form**

```dart
import 'package:flutter/material.dart';

class LoginForm extends StatefulWidget {
  @override
  State<LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  
  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            controller: _emailController,
            decoration: InputDecoration(labelText: 'Email'),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter email';
              }
              if (!value.contains('@')) {
                return 'Invalid email format';
              }
              return null;
            },
          ),
          TextFormField(
            controller: _passwordController,
            obscureText: true,
            decoration: InputDecoration(labelText: 'Password'),
            validator: (value) {
              if (value == null || value.length < 6) {
                return 'Password must be at least 6 characters';
              }
              return null;
            },
          ),
          ElevatedButton(
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                print('Email: ${_emailController.text}');
                print('Password: ${_passwordController.text}');
              }
            },
            child: Text('Login'),
          ),
        ],
      ),
    );
  }
}
```

**Solution 2: Use AutovalidateMode correctly**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Form(
    child: Column(
      children: [
        TextFormField(
          autovalidateMode: AutovalidateMode.onUserInteraction,
          validator: (value) {
            if (value == null || value.isEmpty) {
              return 'Required';
            }
            return null;
          },
          decoration: InputDecoration(labelText: 'Name'),
        ),
      ],
    ),
  );
}
```

**Solution 3: Save form data**

```dart
import 'package:flutter/material.dart';

class DataForm extends StatefulWidget {
  @override
  State<DataForm> createState() => _DataFormState();
}

class _DataFormState extends State<DataForm> {
  final _formKey = GlobalKey<FormState>();
  String _name = '';
  
  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            onSaved: (value) => _name = value ?? '',
            validator: (value) =>
                value?.isEmpty ?? true ? 'Required' : null,
          ),
          ElevatedButton(
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                _formKey.currentState!.save();
                print('Saved name: $_name');
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

**Solution 4: Multiple forms with unique keys**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Column(
    children: [
      Form(
        key: GlobalKey<FormState>(),
        child: TextFormField(
          validator: (v) => v?.isEmpty ?? true ? 'Required' : null,
        ),
      ),
      Form(
        key: GlobalKey<FormState>(),
        child: TextFormField(
          validator: (v) => v?.isEmpty ?? true ? 'Required' : null,
        ),
      ),
    ],
  );
}
```

**Solution 5: Cross-field validation**

```dart
import 'package:flutter/material.dart';

class PasswordForm extends StatefulWidget {
  @override
  State<PasswordForm> createState() => _PasswordFormState();
}

class _PasswordFormState extends State<PasswordForm> {
  final _formKey = GlobalKey<FormState>();
  
  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            obscureText: true,
            decoration: InputDecoration(labelText: 'Password'),
            validator: (value) {
              if (value == null || value.length < 6) return 'Too short';
              return null;
            },
          ),
          TextFormField(
            obscureText: true,
            decoration: InputDecoration(labelText: 'Confirm'),
            validator: (value) {
              // Cross-field validation
              String password = '';
              _formKey.currentState?.save();
              if (value != password) return 'Passwords do not match';
              return null;
            },
          ),
          ElevatedButton(
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                print('Valid');
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

`FormState.validate()` calls each `TextFormField`'s validator. If any validator returns a non-null string, validation fails. Return `null` to indicate success.

## Related Errors

- [Flutter TextEditingController Error](/languages/dart/flutter-text-editing-controller-error/)
- [Flutter Dropdown Error](/languages/dart/flutter-dropdown-error/)
- [Flutter Focus Error](/languages/dart/flutter-focus-error/)
