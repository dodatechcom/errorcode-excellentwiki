---
title: "[Solution] Flutter ListView ShrinkWrap Error"
description: "Fix Flutter ListView shrinkWrap errors when nested scrollable widgets cause unbounded height or performance issues."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A ListView shrinkWrap error in Flutter occurs when a `ListView` is placed inside another scrollable widget without `shrinkWrap: true`, causing an unbounded height error, or when `shrinkWrap` causes performance issues with large lists.

## Common Causes

- `ListView` inside `Column` inside `SingleChildScrollView` without `shrinkWrap`
- `shrinkWrap: true` on a large list causing all items to be laid out at once
- `ListView` inside a `TabBarView` without proper scroll physics
- Nested `ListView` with `NeverScrollableScrollPhysics` missing on inner list
- `ListView.builder` with `shrinkWrap` defeating lazy loading

## How to Fix

1. Use shrinkWrap with physics for nested scrollable:

```dart
SingleChildScrollView(
  child: Column(
    children: [
      Text('Header'),
      ListView.builder(
        shrinkWrap: true,
        physics: const NeverScrollableScrollPhysics(),
        itemCount: items.length,
        itemBuilder: (context, index) => ListTile(title: Text(items[index])),
      ),
    ],
  ),
);
```

2. Replace ListView in Column with a proper scroll view:

```dart
// Instead of Column + ListView, use CustomScrollView
CustomScrollView(
  slivers: [
    SliverToBoxAdapter(child: Text('Header')),
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, index) => ListTile(title: Text('Item $index')),
        childCount: items.length,
      ),
    ),
  ],
);
```

3. Use `ListView` with `primary: false` for nested contexts:

```dart
Column(
  children: [
    Container(height: 100, child: Text('Fixed header')),
    Expanded(
      child: ListView.builder(
        itemCount: 1000,
        itemBuilder: (context, index) => ListTile(title: Text('Item $index')),
      ),
    ),
  ],
);
```

## Examples

```dart
// Bug: unbounded height
Column(
  children: [
    Text('Title'),
    ListView.builder( // Error: ListView has unbounded height
      itemCount: 100,
      itemBuilder: (context, index) => Text('Item $index'),
    ),
  ],
);

// Fixed: use Expanded
Column(
  children: [
    Text('Title'),
    Expanded(
      child: ListView.builder(
        itemCount: 100,
        itemBuilder: (context, index) => Text('Item $index'),
      ),
    ),
  ],
);
```

```text
RenderFlex children have non-zero flex but incoming height constraints are unbounded.
```
