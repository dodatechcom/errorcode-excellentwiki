---
title: "[Solution] Flutter Form Validation Error"
description: "Form validation not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

Form validation not working.

## Common Causes

No validators.

## How to Fix

Add validators.

## Example

```dart
TextFormField(
  validator: (v) => v == null || v.isEmpty ? 'Required' : null,
)
```
