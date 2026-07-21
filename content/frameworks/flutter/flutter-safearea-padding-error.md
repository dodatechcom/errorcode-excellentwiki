---
title: "[Solution] Flutter SafeArea Padding Error"
description: "Fix Flutter SafeArea padding errors when content is hidden behind notches, status bars, or system UI elements."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A SafeArea padding error in Flutter occurs when content is rendered behind device notches, status bars, or navigation bars because `SafeArea` is not used or is applied incorrectly.

## Common Causes

- `SafeArea` not wrapping the main content widget
- `SafeArea` applied to a widget that already has padding from `Scaffold`
- `MediaQuery.of(context).padding` not used for custom spacing
- `AppBar` used instead of `SafeArea` on screens without an AppBar
- `bottom` parameter of `SafeArea` not set for bottom navigation

## How to Fix

1. Wrap the body of Scaffold with SafeArea:

```dart
Scaffold(
  appBar: AppBar(title: Text('Title')), // AppBar handles top padding
  body: SafeArea(
    child: ListView(
      children: items.map((item) => ListTile(title: Text(item))).toList(),
    ),
  ),
);
```

2. Use MediaQuery padding directly for custom layouts:

```dart
final topPadding = MediaQuery.of(context).padding.top;
final bottomPadding = MediaQuery.of(context).padding.bottom;

CustomScrollView(
  slivers: [
    SliverPadding(
      padding: EdgeInsets.only(top: topPadding),
      sliver: SliverList(...),
    ),
  ],
);
```

3. Apply SafeArea selectively:

```dart
Scaffold(
  body: Column(
    children: [
      SafeArea(
        bottom: false, // Only handle top padding
        child: CustomHeader(),
      ),
      Expanded(child: Content()),
      SafeArea(
        top: false, // Only handle bottom padding
        child: BottomBar(),
      ),
    ],
  ),
);
```

## Examples

```dart
// Bug: content behind the notch
Scaffold(
  body: Column(
    children: [
      Text('Title'), // Hidden behind notch on iPhone X+
      Expanded(child: ListView(...)),
    ],
  ),
);

// Fixed: wrap with SafeArea
Scaffold(
  body: SafeArea(
    child: Column(
      children: [
        Text('Title'),
        Expanded(child: ListView(...)),
      ],
    ),
  ),
);
```

```text
Bottom overflowed by 34 pixels (the notch area)
```
