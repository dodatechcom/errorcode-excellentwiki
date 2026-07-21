---
title: "[Solution] Flutter Badge Count Error"
description: "Fix Flutter Badge errors when the notification badge count is not displayed or shows incorrect values."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Badge count error in Flutter occurs when the `Badge` widget does not display the notification count, shows the wrong number, or fails to hide when the count is zero.

## Common Causes

- `Badge` `label` property not set or set to null
- `isLabelVisible` not toggled when count reaches zero
- `Badge` wrapping a widget that does not support overlay positioning
- Count updated but `setState` not called
- `smallSize`, `largeSize`, or `textStyle` causing the badge to overflow

## How to Fix

1. Use Badge with proper count display:

```dart
Badge(
  label: Text(_notificationCount > 99 ? '99+' : '$_notificationCount'),
  isLabelVisible: _notificationCount > 0,
  child: IconButton(
    icon: const Icon(Icons.notifications),
    onPressed: () => openNotifications(),
  ),
);
```

2. Wrap BottomNavigationBarItem with Badge:

```dart
BottomNavigationBar(
  items: [
    const BottomNavigationBarItem(
      icon: Icon(Icons.home),
      label: 'Home',
    ),
    BottomNavigationBarItem(
      icon: Badge(
        label: Text('$_unreadMessages'),
        isLabelVisible: _unreadMessages > 0,
        child: const Icon(Icons.mail),
      ),
      label: 'Messages',
    ),
    const BottomNavigationBarItem(
      icon: Icon(Icons.settings),
      label: 'Settings',
    ),
  ],
);
```

3. Animate badge changes:

```dart
AnimatedSwitcher(
  duration: const Duration(milliseconds: 200),
  child: Badge(
    key: ValueKey(_count),
    label: Text('$_count'),
    isLabelVisible: _count > 0,
    child: const Icon(Icons.shopping_cart),
  ),
);
```

## Examples

```dart
// Bug: Badge always visible even with 0 count
Badge(
  label: Text('$_count'), // Shows "0"
  child: Icon(Icons.mail),
);

// Fixed: hide when zero
Badge(
  label: Text('$_count'),
  isLabelVisible: _count > 0,
  child: Icon(Icons.mail),
);
```

```text
Badge label must be a widget, not null when visible
```
