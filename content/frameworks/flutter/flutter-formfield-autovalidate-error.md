---
title: "[Solution] Flutter FormField Autovalidate Error"
description: "Fix Flutter FormField autovalidate errors when validation messages appear before the user interacts with the field."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An autovalidate error in Flutter occurs when `AutovalidateMode` causes validation errors to display immediately on screen load, before the user has entered any data, creating a poor user experience.

## Common Causes

- `autovalidateMode: AutovalidateMode.always` shows errors on empty fields
- `validator` returns error for empty values when `autovalidateMode` is always
- `autovalidate` property (deprecated) set to `true`
- Validation triggered by `FormState.validate()` while `autovalidateMode` is also active
- `onUserInteraction` mode not working because form is not being interacted with

## How to Fix

1. Use `onUserInteraction` for better UX:

```dart
TextFormField(
  autovalidateMode: AutovalidateMode.onUserInteraction,
  validator: (value) {
    if (value == null || value.isEmpty) {
      return 'This field is required';
    }
    return null;
  },
  decoration: const InputDecoration(
    labelText: 'Email',
    border: OutlineInputBorder(),
  ),
);
```

2. Only validate on submit:

```dart
final _formKey = GlobalKey<FormState>();

Form(
  key: _formKey,
  child: Column(
    children: [
      TextFormField(
        autovalidateMode: AutovalidateMode.disabled, // Default
        validator: (value) {
          if (value == null || value.isEmpty) return 'Required';
          return null;
        },
      ),
      ElevatedButton(
        onPressed: () {
          if (_formKey.currentState!.validate()) {
            submitForm();
          }
        },
        child: const Text('Submit'),
      ),
    ],
  ),
);
```

3. Combine modes for progressive validation:

```dart
TextFormField(
  autovalidateMode: AutovalidateMode.onUserInteraction,
  validator: (value) {
    if (value == null || value.isEmpty) {
      return 'Email is required';
    }
    if (!value.contains('@')) {
      return 'Enter a valid email';
    }
    return null;
  },
);
```

## Examples

```dart
// Bug: shows error immediately on empty field
TextFormField(
  autovalidate: true, // Deprecated and shows error on load
  validator: (v) => v.isEmpty ? 'Required' : null,
);

// Fixed: only validate after user interaction
TextFormField(
  autovalidateMode: AutovalidateMode.onUserInteraction,
  validator: (v) {
    if (v == null || v.isEmpty) return 'Required';
    return null;
  },
);
```

```text
AutovalidateMode.always is deprecated -- use onUserInteraction instead
```
