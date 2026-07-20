---
title: "[Solution] Flutter CustomScrollView Error — SliverList, SliverGrid, SliverAppBar"
description: "Fix Flutter CustomScrollView errors from sliver configuration, SliverList/SliverGrid nesting, and SliverAppBar usage."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 172
---

CustomScrollView errors occur when slivers are used outside of `CustomScrollView`, nested scrollables conflict, or `SliverAppBar` is misconfigured.

## Common Causes

1. Using `ListView` or `GridView` directly inside `CustomScrollView`.
2. Missing `Expanded` or `Flexible` for nested scrollable content.
3. `SliverAppBar` without `FlexibleSpaceBar` or `pinned`/`floating` configuration.
4. Multiple scrollables competing for scroll events.
5. `SliverToBoxAdapter` not used for non-sliver widgets.

## How to Fix It

**Solution 1: Basic CustomScrollView with slivers**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return CustomScrollView(
    slivers: [
      SliverAppBar(
        title: Text('Custom Scroll'),
        pinned: true,
        expandedHeight: 200,
        flexibleSpace: FlexibleSpaceBar(
          title: Text('Expanded Title'),
          background: Container(color: Colors.blue),
        ),
      ),
      SliverList(
        delegate: SliverChildBuilderDelegate(
          (context, index) => ListTile(title: Text('Item $index')),
          childCount: 50,
        ),
      ),
    ],
  );
}
```

**Solution 2: Combine SliverList and SliverGrid**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return CustomScrollView(
    slivers: [
      SliverAppBar(title: Text('Mixed Layout'), pinned: true),
      SliverList(
        delegate: SliverChildBuilderDelegate(
          (context, index) => Card(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Text('List Item $index'),
            ),
          ),
          childCount: 5,
        ),
      ),
      SliverGrid(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 3,
          childAspectRatio: 1.0,
        ),
        delegate: SliverChildBuilderDelegate(
          (context, index) => Card(
            child: Center(child: Text('Grid $index')),
          ),
          childCount: 12,
        ),
      ),
    ],
  );
}
```

**Solution 3: SliverToBoxAdapter for non-sliver widgets**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return CustomScrollView(
    slivers: [
      SliverToBoxAdapter(
        child: Padding(
          padding: EdgeInsets.all(16),
          child: Text('Header Section', style: TextStyle(fontSize: 20)),
        ),
      ),
      SliverList(
        delegate: SliverChildBuilderDelegate(
          (context, index) => ListTile(title: Text('Item $index')),
          childCount: 20,
        ),
      ),
    ],
  );
}
```

**Solution 4: Nested scrollable with NestedScrollView**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return NestedScrollView(
    headerSliverBuilder: (context, innerBoxIsScrolled) {
      return [
        SliverAppBar(
          title: Text('Nested'),
          pinned: true,
          forceElevated: innerBoxIsScrolled,
        ),
      ];
    },
    body: TabBarView(
      children: [
        ListView.builder(
          itemCount: 30,
          itemBuilder: (context, index) => ListTile(title: Text('Tab 1: $index')),
        ),
        ListView.builder(
          itemCount: 30,
          itemBuilder: (context, index) => ListTile(title: Text('Tab 2: $index')),
        ),
      ],
    ),
  );
}
```

**Solution 5: SliverAppBar with tabs**

```dart
import 'package:flutter/material.dart';

class TabbedScroll extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: CustomScrollView(
        slivers: [
          SliverAppBar(
            title: Text('Tabbed'),
            pinned: true,
            bottom: TabBar(
              tabs: [
                Tab(text: 'Posts'),
                Tab(text: 'Comments'),
              ],
            ),
          ),
          SliverFillRemaining(
            child: TabBarView(
              children: [
                Center(child: Text('Posts content')),
                Center(child: Text('Comments content')),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
```

## Examples

`CustomScrollView` only accepts sliver widgets. Use `SliverToBoxAdapter` to include regular widgets. `SliverFillRemaining` fills the remaining space after slivers.

## Related Errors

- [Flutter List View Error](/languages/dart/flutter-list-view-error/)
- [Flutter Grid View Error](/languages/dart/flutter-grid-view-error/)
- [Flutter Scroll Controller Error](/languages/dart/flutter-scroll-controller-error/)
