---
title: "[Solution] Flutter Dismissible Swipe Error"
description: "Fix Flutter Dismissible swipe errors when items cannot be dismissed or confirmDismiss callback fails."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Dismissible swipe error in Flutter occurs when the `Dismissible` widget fails to dismiss an item, either because `confirmDismiss` returns `false`, the `Key` is not unique, or the dismiss direction does not match user gestures.

## Common Causes

- `confirmDismiss` returns `false` without showing feedback
- `Key` is not unique across the list causing incorrect dismissal
- `direction` set to `DismissDirection.startToEnd` but user swipes left
- Background widget not visible during swipe
- List modified externally while dismissal animation is in progress

## How to Fix

1. Provide unique keys and a confirmDismiss callback:

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    final item = items[index];
    return Dismissible(
      key: Key(item.id), // Unique ID per item
      direction: DismissDirection.endToStart,
      background: Container(
        color: Colors.red,
        alignment: Alignment.centerRight,
        padding: const EdgeInsets.only(right: 16),
        child: const Icon(Icons.delete, color: Colors.white),
      ),
      confirmDismiss: (direction) async {
        return await showDialog<bool>(
          context: context,
          builder: (ctx) => AlertDialog(
            title: const Text('Confirm'),
            content: const Text('Delete this item?'),
            actions: [
              TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
              TextButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('Delete')),
            ],
          ),
        );
      },
      onDismissed: (direction) {
        setState(() => items.removeAt(index));
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('${item.name} deleted')),
        );
      },
      child: ListTile(title: Text(item.name)),
    );
  },
);
```

2. Handle both swipe directions:

```dart
Dismissible(
  key: Key(item.id),
  direction: DismissDirection.horizontal,
  background: Container(
    color: Colors.green,
    alignment: Alignment.centerLeft,
    child: const Icon(Icons.archive, color: Colors.white),
  ),
  secondaryBackground: Container(
    color: Colors.red,
    alignment: Alignment.centerRight,
    child: const Icon(Icons.delete, color: Colors.white),
  ),
  onDismissed: (direction) {
    if (direction == DismissDirection.startToEnd) {
      archiveItem(item);
    } else {
      deleteItem(item);
    }
  },
  child: ListTile(title: Text(item.name)),
);
```

## Examples

```dart
// Bug: key is the index -- wrong item dismissed on reorder
ListView.builder(
  itemBuilder: (context, index) {
    return Dismissible(
      key: Key('$index'), // Wrong: index changes on reorder
      onDismissed: (_) => items.removeAt(index),
      child: ListTile(title: Text(items[index].name)),
    );
  },
);

// Fixed: use unique item ID
Dismissible(
  key: Key(item.id),
  onDismissed: (_) {
    setState(() => items.removeWhere((i) => i.id == item.id));
  },
  child: ListTile(title: Text(item.name)),
);
```

```text
A dismissed Dismissible widget is still part of the widget tree.
```
