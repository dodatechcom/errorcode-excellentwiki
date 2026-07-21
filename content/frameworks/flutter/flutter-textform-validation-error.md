---
title: "[Solution] Flutter TextFormField Validation Error"
description: "Fix Flutter TextFormField validation errors when the validator does not display error messages correctly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A TextFormField validation error in Flutter occurs when the `validator` function does not return the expected error string, or when `GlobalKey<FormState>` is not used correctly to trigger validation.

## Common Causes

- `validator` returns `null` on valid input but does not return error string on invalid
- `Form` widget missing from the widget tree above the `TextFormField`
- `FormState.validate()` not called on submit
- `GlobalKey<FormState>` recreated on every build
- `TextEditingController` and `validator` conflict

## How to Fix

1. Use a GlobalKey for FormState and validate on submit:

```dart
class _FormScreenState extends State<FormScreen> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            decoration: const InputDecoration(labelText: 'Email'),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Email is required';
              }
              if (!value.contains('@')) {
                return 'Enter a valid email';
              }
              return null; // Valid
            },
          ),
          ElevatedButton(
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                // Form is valid -- submit
                _submitForm();
              }
            },
            child: const Text('Submit'),
          ),
        ],
      ),
    );
  }
}
```

2. Validate individual fields on change:

```dart
TextFormField(
  onChanged: (value) {
    // Real-time validation
    if (value.length < 6) {
      _passwordError = 'Password must be at least 6 characters';
    } else {
      _passwordError = null;
    }
    setState(() {});
  },
  validator: (value) {
    if (value == null || value.length < 6) {
      return 'Password must be at least 6 characters';
    }
    return null;
  },
);
```

3. Auto-validate mode for instant feedback:

```dart
TextFormField(
  autovalidateMode: AutovalidateMode.onUserInteraction,
  validator: (value) {
    if (value == null || value.isEmpty) return 'Required';
    if (!RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$').hasMatch(value)) {
      return 'Invalid email';
    }
    return null;
  },
);
```

## Examples

```dart
// Bug: GlobalKey created in build -- recreated every frame
Widget build(BuildContext context) {
  final formKey = GlobalKey<FormState>(); // Wrong: new key every rebuild
  return Form(key: formKey, child: TextFormField(...));
}

// Fixed: GlobalKey in State
final _formKey = GlobalKey<FormState>();

Widget build(BuildContext context) {
  return Form(key: _formKey, child: TextFormField(...));
}
```

```text
The form for a Form widget must have at least one FormField descendant.
```
