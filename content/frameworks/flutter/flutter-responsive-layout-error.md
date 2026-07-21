---
title: "[Solution] Flutter Responsive Layout Error"
description: "Fix Flutter responsive layout errors when widgets do not adapt to different screen sizes and orientations."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A responsive layout error in Flutter occurs when widgets do not adapt to different screen sizes, causing overflow on small screens or excessive whitespace on large screens. This is common when fixed pixel values are used instead of relative sizing.

## Common Causes

- Fixed `height` or `width` values instead of `MediaQuery` or `LayoutBuilder`
- `Row` with too many children causing overflow on narrow screens
- Font sizes not scaled for different screen sizes
- `GridView` column count not responsive to screen width
- `Scaffold` body does not use `SafeArea` for notch/status bar

## How to Fix

1. Use `LayoutBuilder` for responsive sizing:

```dart
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth > 600) {
      return _buildWideLayout();
    } else {
      return _buildNarrowLayout();
    }
  },
);

Widget _buildWideLayout() {
  return Row(
    children: [
      Expanded(flex: 1, child: Sidebar()),
      Expanded(flex: 3, child: Content()),
    ],
  );
}

Widget _buildNarrowLayout() {
  return Column(
    children: [Content()],
  );
}
```

2. Use `MediaQuery` for screen dimensions:

```dart
final screenWidth = MediaQuery.of(context).size.width;
final columns = screenWidth > 1200 ? 4 : screenWidth > 800 ? 3 : 2;

GridView.builder(
  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
    crossAxisCount: columns,
    mainAxisSpacing: 8,
    crossAxisSpacing: 8,
  ),
  itemBuilder: (context, index) => Card(child: Center(child: Text('Item $index'))),
);
```

3. Wrap with `SafeArea` and `SingleChildScrollView`:

```dart
SafeArea(
  child: SingleChildScrollView(
    padding: const EdgeInsets.all(16),
    child: Column(
      children: [
        Text('Title', style: Theme.of(context).textTheme.headlineMedium),
        const SizedBox(height: 16),
        // Content here
      ],
    ),
  ),
);
```

## Examples

```dart
// Bug: Row overflows on narrow screens
Row(
  children: [
    ElevatedButton(onPressed: () {}, child: Text('Save')),
    ElevatedButton(onPressed: () {}, child: Text('Cancel')),
    ElevatedButton(onPressed: () {}, child: Text('Delete')),
    ElevatedButton(onPressed: () {}, child: Text('Export')),
  ],
);

// Fixed: wrap in Wrap widget
Wrap(
  spacing: 8,
  runSpacing: 8,
  children: [
    ElevatedButton(onPressed: () {}, child: Text('Save')),
    ElevatedButton(onPressed: () {}, child: Text('Cancel')),
    ElevatedButton(onPressed: () {}, child: Text('Delete')),
    ElevatedButton(onPressed: () {}, child: Text('Export')),
  ],
);
```

```text
A RenderFlex overflowed by 120 pixels on the right.
```
