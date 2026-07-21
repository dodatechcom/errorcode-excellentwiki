---
title: "[Solution] Flutter TextField Decoration Error"
description: "Fix Flutter TextField decoration errors when input labels, hints, or borders do not display correctly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A TextField decoration error in Flutter occurs when the `InputDecoration` properties are misconfigured, causing labels to overlap, hints to disappear, or borders to render incorrectly.

## Common Causes

- `hintText` and `labelText` used together causing visual conflict
- `border` not defined for focused or enabled states
- `filled: true` set without `fillColor` specified
- `prefixIcon` or `suffixIcon` overlapping with text
- `contentPadding` too small for the text size

## How to Fix

1. Configure InputDecoration with proper states:

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Email',
    hintText: 'you@example.com',
    border: OutlineInputBorder(),
    focusedBorder: OutlineInputBorder(
      borderSide: BorderSide(color: Colors.blue, width: 2),
    ),
    enabledBorder: OutlineInputBorder(
      borderSide: BorderSide(color: Colors.grey, width: 1),
    ),
    errorBorder: OutlineInputBorder(
      borderSide: BorderSide(color: Colors.red, width: 1),
    ),
    filled: true,
    fillColor: Colors.grey.shade50,
    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
  ),
);
```

2. Use prefix and suffix icons correctly:

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Search',
    prefixIcon: const Icon(Icons.search),
    suffixIcon: IconButton(
      icon: const Icon(Icons.clear),
      onPressed: () => _controller.clear(),
    ),
  ),
);
```

3. Handle focused and error states:

```dart
TextFormField(
  decoration: InputDecoration(
    labelText: 'Password',
    hintText: 'Enter password',
    prefixIcon: const Icon(Icons.lock),
    suffixIcon: Icon(_obscure ? Icons.visibility : Icons.visibility_off),
    border: const UnderlineInputBorder(),
  ),
  obscureText: _obscure,
);
```

## Examples

```dart
// Bug: labelText and hintText overlap
TextField(
  decoration: InputDecoration(
    labelText: 'Email',
    hintText: 'you@example.com', // Overlaps when label is floating
  ),
);

// Fixed: use only labelText (hint shows when focused)
TextField(
  decoration: InputDecoration(
    labelText: 'Email',
  ),
);

// Or use suffixText for inline hint
TextField(
  decoration: InputDecoration(
    labelText: 'Amount',
    suffixText: 'USD',
  ),
);
```

```text
InputDecoration's floating label animates incorrectly when switching focus
```
