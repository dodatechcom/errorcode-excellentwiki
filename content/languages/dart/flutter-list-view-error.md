---
title: "[Solution] Flutter ListView Error — builder, itemCount, itemExtent, shrinkWrap"
description: "Fix Flutter ListView errors from builder configuration, itemCount, itemExtent, shrinkWrap, and scroll physics."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 170
---

ListView errors occur when `itemCount` is missing, `shrinkWrap` is used incorrectly, or scroll configuration conflicts arise.

## Common Causes

1. `ListView.builder` missing `itemCount` for non-lazy loading.
2. `shrinkWrap: true` in a `ListView` inside `CustomScrollView`.
3. `itemExtent` causing layout issues with variable-height items.
4. `ListView` inside a `Column` without proper expansion.
5. `ScrollPhysics` conflict with parent scrollable.

## How to Fix It

**Solution 1: Basic ListView.builder**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return ListView.builder(
    itemCount: 100,
    itemBuilder: (context, index) {
      return ListTile(
        leading: CircleAvatar(child: Text('${index + 1}')),
        title: Text('Item ${index + 1}'),
        subtitle: Text('Subtitle for item ${index + 1}'),
      );
    },
  );
}
```

**Solution 2: Use shrinkWrap correctly**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Column(
    children: [
      Text('Header'),
      // shrinkWrap allows ListView to size itself based on content
      ListView.builder(
        shrinkWrap: true,
        physics: NeverScrollableScrollPhysics(),
        itemCount: 10,
        itemBuilder: (context, index) => ListTile(
          title: Text('Item $index'),
        ),
      ),
    ],
  );
}
```

**Solution 3: Use itemExtent for fixed-height items**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return ListView.builder(
    itemExtent: 80, // Each item is exactly 80 pixels tall
    itemCount: 50,
    itemBuilder: (context, index) {
      return Container(
        color: index.isEven ? Colors.grey[200] : Colors.white,
        alignment: Alignment.center,
        child: Text('Item $index'),
      );
    },
  );
}
```

**Solution 4: ListView.separated for dividers**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return ListView.separated(
    itemCount: 20,
    separatorBuilder: (context, index) => Divider(height: 1),
    itemBuilder: (context, index) {
      return ListTile(title: Text('Item $index'));
    },
  );
}
```

**Solution 5: Handle empty list**

```dart
import 'package:flutter/material.dart';

class DataList extends StatelessWidget {
  final List<String> items;
  
  const DataList({super.key, required this.items});
  
  @override
  Widget build(BuildContext context) {
    if (items.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.inbox, size: 64, color: Colors.grey),
            SizedBox(height: 16),
            Text('No items found'),
          ],
        ),
      );
    }
    
    return ListView.builder(
      itemCount: items.length,
      itemBuilder: (context, index) => ListTile(
        title: Text(items[index]),
      ),
    );
  }
}
```

## Examples

`ListView.builder` lazily builds items as they scroll into view. Use `ListView.custom` with `SliverChildBuilderDelegate` for advanced control. `ListView` inside a `Column` needs `Expanded` or `shrinkWrap: true`.

## Related Errors

- [Flutter Grid View Error](/languages/dart/flutter-grid-view-error/)
- [Flutter Custom Scroll Error](/languages/dart/flutter-custom-scroll-error/)
- [Flutter Scroll Controller Error](/languages/dart/flutter-scroll-controller-error/)
