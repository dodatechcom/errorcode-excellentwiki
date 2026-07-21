---
title: "[Solution] Flutter ScrollPhysics Error"
description: "Fix Flutter ScrollPhysics errors when scroll behavior does not match the expected snapping or bouncing behavior."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A ScrollPhysics error in Flutter occurs when the scroll behavior of a `ListView`, `GridView`, or `CustomScrollView` does not work as expected, causing items to not snap, bounce, or stop at the correct positions.

## Common Causes

- `ClampingScrollPhysics` used on iOS where `BouncingScrollPhysics` is expected
- Scroll controller not attached to the scroll widget
- `NeverScrollableScrollPhysics` accidentally applied to a scrollable widget
- PageView physics set to `AlwaysScrollableScrollPhysics` preventing page snapping
- Custom physics not compatible with the scroll widget type

## How to Fix

1. Set platform-appropriate scroll physics:

```dart
ListView.builder(
  physics: Theme.of(context).platform == TargetPlatform.iOS
    ? const BouncingScrollPhysics()
    : const ClampingScrollPhysics(),
  itemBuilder: (context, index) => ListTile(title: Text('Item $index')),
);
```

2. Use `ScrollPageScrollPhysics` for PageView:

```dart
PageView.builder(
  physics: const PageScrollPhysics(), // Snaps to pages
  itemCount: pages.length,
  itemBuilder: (context, index) => pages[index],
);
```

3. Disable scrolling when needed:

```dart
ListView(
  physics: const NeverScrollableScrollPhysics(),
  children: items.map((item) => ListTile(title: Text(item))).toList(),
);
```

## Examples

```dart
// Bug: ClampingScrollPhysics on iOS gives wrong feel
ListView.builder(
  physics: const ClampingScrollPhysics(), // Always clamps
  itemCount: 100,
  itemBuilder: (context, index) => Text('Item $index'),
);

// Fixed: platform-aware physics
ListView.builder(
  physics: const BouncingScrollPhysics(), // Bounces on iOS
  itemCount: 100,
  itemBuilder: (context, index) => Text('Item $index'),
);
```

```text
ScrollController not attached to any scroll views.
```
