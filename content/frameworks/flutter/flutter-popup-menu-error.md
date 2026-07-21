---
title: "[Solution] Flutter Popover PopupMenu Error"
description: "Fix Flutter PopupMenu errors when the popup menu does not appear or returns null on item selection."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A PopupMenu error in Flutter occurs when the `showMenu` or `PopupMenuButton` does not display correctly, or the selected value is not captured because the `onSelected` callback is missing or the items have null values.

## Common Causes

- `PopupMenuButton` has no `itemBuilder` defined
- `onSelected` callback not handling the returned value
- `itemBuilder` returns empty list
- Popup positioned off-screen due to insufficient space
- `value` on `PopupMenuItem` does not match the expected type

## How to Fix

1. Define PopupMenuButton with proper items:

```dart
PopupMenuButton<String>(
  icon: const Icon(Icons.more_vert),
  onSelected: (String value) {
    switch (value) {
      case 'edit':
        editItem();
        break;
      case 'delete':
        deleteItem();
        break;
      case 'share':
        shareItem();
        break;
    }
  },
  itemBuilder: (BuildContext context) => [
    const PopupMenuItem(value: 'edit', child: Text('Edit')),
    const PopupMenuItem(value: 'delete', child: Text('Delete')),
    const PopupMenuItem(value: 'share', child: Text('Share')),
  ],
);
```

2. Use enum values for type safety:

```sharp
enum MenuAction { edit, delete, share }

PopupMenuButton<MenuAction>(
  onSelected: (MenuAction action) {
    handleMenuAction(action);
  },
  itemBuilder: (context) => [
    const PopupMenuItem(value: MenuAction.edit, child: Text('Edit')),
    const PopupMenuItem(value: MenuAction.delete, child: Text('Delete')),
    const PopupMenuItem(value: MenuAction.share, child: Text('Share')),
  ],
);
```

3. Handle null result from cancelled selection:

```dart
final result = await showMenu<String>(
  context: context,
  position: RelativeRect.fill,
  items: [
    const PopupMenuItem(value: 'yes', child: Text('Yes')),
    const PopupMenuItem(value: 'no', child: Text('No')),
  ],
);

if (result != null) {
  // User made a selection
  processResult(result);
}
// result is null if user tapped outside the menu
```

## Examples

```dart
// Bug: no onSelected handler
PopupMenuButton<String>(
  itemBuilder: (context) => [
    PopupMenuItem(value: 'a', child: Text('Option A')),
    PopupMenuItem(value: 'b', child: Text('Option B')),
  ],
  // onSelected missing -- selection has no effect
);

// Fixed: handle selection
PopupMenuButton<String>(
  onSelected: (value) => print('Selected: $value'),
  itemBuilder: (context) => [
    PopupMenuItem(value: 'a', child: Text('Option A')),
    PopupMenuItem(value: 'b', child: Text('Option B')),
  ],
);
```

```text
A non-null String must be provided to PopupMenuButton
```
