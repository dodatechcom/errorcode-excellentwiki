---
title: "[Solution] Flutter Tooltip Show Error"
description: "Fix Flutter tooltip errors when tooltips do not appear on long press or display at incorrect positions."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Tooltip show error in Flutter occurs when the tooltip does not appear on long press, appears at the wrong position, or is clipped by screen edges because the tooltip content is too long for the available space.

## Common Causes

- `Tooltip` wraps a widget with no tappable area
- `message` is empty or null
- `Tooltip` positioned near screen edge causing overflow
- `waitDuration` too long for user interaction pattern
- Parent widget absorbs the long-press gesture

## How to Fix

1. Wrap interactive widgets with Tooltip:

```dart
Tooltip(
  message: 'Delete this item',
  child: IconButton(
    icon: const Icon(Icons.delete),
    onPressed: () => deleteItem(),
  ),
);
```

2. Use rich tooltip with custom content:

```dart
Tooltip(
  richMessage: TextSpan(
    text: 'Status: ',
    style: DefaultTextStyle.of(context).style,
    children: [
      TextSpan(
        text: 'Active',
        style: TextStyle(fontWeight: FontWeight.bold, color: Colors.green),
      ),
    ],
  ),
  child: Chip(label: Text('User status')),
);
```

3. Customize tooltip appearance and behavior:

```dart
Tooltip(
  message: 'Settings',
  preferBelow: false, // Show above the widget
  verticalOffset: 20,
  waitDuration: const Duration(milliseconds: 500),
  showDuration: const Duration(seconds: 2),
  decoration: BoxDecoration(
    color: Colors.blue.shade800,
    borderRadius: BorderRadius.circular(8),
  ),
  textStyle: const TextStyle(color: Colors.white),
  child: const Icon(Icons.settings),
);
```

## Examples

```dart
// Bug: Tooltip wraps a non-interactive widget
Tooltip(
  message: 'Info',
  child: Text('Hover over me'), // Text does not trigger tooltip on desktop
);

// Fixed: wrap with a tappable widget
Tooltip(
  message: 'Info',
  child: GestureDetector(
    onTap: () {},
    child: Text('Tap for info'),
  ),
);
```

```text
Tooltip message must not be empty
```
