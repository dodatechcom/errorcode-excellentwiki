---
title: "[Solution] Flutter Sliver Layout Error"
description: "Fix Flutter sliver layout errors when CustomScrollView children do not render or overflow the viewport."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A sliver layout error in Flutter occurs when `Sliver` widgets inside a `CustomScrollView` do not lay out correctly, causing visual glitches, overflow errors, or empty areas in the scroll view.

## Common Causes

- Mixing `Sliver` and non-sliver widgets inside `CustomScrollView`
- `SliverList` missing `SliverChildBuilderDelegate` or `SliverChildListDelegate`
- `SliverGrid` delegate returns incorrect child count
- `SliverToBoxAdapter` used for non-sliver widgets but not wrapped properly
- `CustomScrollView` `slivers` list contains invalid widget types

## How to Fix

1. Ensure all children of `CustomScrollView` are slivers:

```dart
CustomScrollView(
  slivers: [
    SliverAppBar(
      title: const Text('App Bar'),
      floating: true,
    ),
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, index) => ListTile(title: Text('Item $index')),
        childCount: 20,
      ),
    ),
  ],
);
```

2. Wrap non-sliver widgets with `SliverToBoxAdapter`:

```dart
CustomScrollView(
  slivers: [
    SliverToBoxAdapter(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Text('Header', style: Theme.of(context).textTheme.headlineSmall),
      ),
    ),
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, index) => Card(child: ListTile(title: Text('Item $index'))),
        childCount: items.length,
      ),
    ),
  ],
);
```

3. Use `SliverGrid` with proper delegate:

```dart
SliverGrid(
  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
    crossAxisCount: 2,
    mainAxisSpacing: 8,
    crossAxisSpacing: 8,
  ),
  delegate: SliverChildBuilderDelegate(
    (context, index) => Container(
      color: Colors.blue,
      child: Center(child: Text('Item $index')),
    ),
    childCount: 20,
  ),
);
```

## Examples

```dart
// Bug: non-sliver widget in CustomScrollView
CustomScrollView(
  slivers: [
    Text('Header'), // Error: This widget requires a Sliver layout parent
    SliverList(...),
  ],
);

// Fixed: wrap with SliverToBoxAdapter
CustomScrollView(
  slivers: [
    SliverToBoxAdapter(child: Text('Header')),
    SliverList(...),
  ],
);
```

```text
Incorrect use of ParentDataWidget.
```
