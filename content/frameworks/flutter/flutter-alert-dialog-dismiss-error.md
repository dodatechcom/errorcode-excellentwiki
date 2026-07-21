---
title: "[Solution] Flutter AlertDialog Dismiss Error"
description: "Fix Flutter AlertDialog errors when the dialog cannot be dismissed by tapping outside or the close button fails."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An AlertDialog dismiss error in Flutter occurs when the dialog cannot be closed by the user because `barrierDismissible` is set to `false` without an alternative close mechanism, or `Navigator.pop` is called with the wrong context.

## Common Causes

- `barrierDismissible: false` set but no close button provided
- `Navigator.pop(context)` called with stale context
- Dialog returned from `showDialog` but not awaited
- Multiple dialogs stacked and pop removes the wrong one
- `WillPopScope` inside dialog prevents dismissal

## How to Fix

1. Always provide a close mechanism:

```dart
Future<void> showConfirmation(BuildContext context) {
  return showDialog(
    context: context,
    builder: (ctx) => AlertDialog(
      title: const Text('Confirm'),
      content: const Text('Are you sure?'),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(ctx),
          child: const Text('Cancel'),
        ),
        TextButton(
          onPressed: () {
            performAction();
            Navigator.pop(ctx);
          },
          child: const Text('Confirm'),
        ),
      ],
    ),
  );
}
```

2. Use `barrierDismissible` appropriately:

```dart
// Allow tapping outside to dismiss
showDialog(
  context: context,
  barrierDismissible: true, // Default is true
  builder: (ctx) => AlertDialog(...),
);

// Prevent dismissing for critical confirmations
showDialog(
  context: context,
  barrierDismissible: false,
  builder: (ctx) => AlertDialog(
    actions: [
      TextButton(
        onPressed: () => Navigator.pop(ctx),
        child: const Text('OK'),
      ),
    ],
  ),
);
```

3. Handle dialog result with `Navigator.pop`:

```dart
final result = await showDialog<bool>(
  context: context,
  builder: (ctx) => AlertDialog(
    title: const Text('Delete?'),
    actions: [
      TextButton(onPressed: () => Navigator.pop(ctx, false), child: Text('No')),
      TextButton(onPressed: () => Navigator.pop(ctx, true), child: Text('Yes')),
    ],
  ),
);

if (result == true) {
  deleteItem();
}
```

## Examples

```dart
// Bug: barrierDismissible false, no close button
showDialog(
  context: context,
  barrierDismissible: false,
  builder: (ctx) => AlertDialog(
    content: Text('You must restart the app'),
    // No actions -- user is stuck
  ),
);

// Fixed: add close action
showDialog(
  context: context,
  barrierDismissible: false,
  builder: (ctx) => AlertDialog(
    content: Text('You must restart the app'),
    actions: [
      TextButton(
        onPressed: () => Navigator.pop(ctx),
        child: Text('OK'),
      ),
    ],
  ),
);
```

```text
Navigator operation requested with a context that does not include a Navigator.
```
