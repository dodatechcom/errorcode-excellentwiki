---
title: "[Solution] Flutter GridView Error — crossAxisCount, childAspectRatio, delegate"
description: "Fix Flutter GridView errors from crossAxisCount, childAspectRatio, delegate configuration, and layout issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 171
---

GridView errors occur when `crossAxisCount` is invalid, `childAspectRatio` causes overflow, or delegate configuration is incorrect.

## Common Causes

1. `crossAxisCount` set to 0 or negative.
2. `childAspectRatio` causing items to overflow their bounds.
3. Using `GridView` without `Expanded` in a `Column`.
4. `SliverGridDelegate` not matching the available width.
5. `GridView.builder` missing `itemCount`.

## How to Fix It

**Solution 1: Basic GridView.builder**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return GridView.builder(
    gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
      crossAxisCount: 3,
      crossAxisSpacing: 8,
      mainAxisSpacing: 8,
      childAspectRatio: 0.75,
    ),
    itemCount: 12,
    itemBuilder: (context, index) {
      return Card(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.image, size: 48),
            SizedBox(height: 8),
            Text('Item ${index + 1}'),
          ],
        ),
      );
    },
  );
}
```

**Solution 2: Responsive grid with LayoutBuilder**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return LayoutBuilder(
    builder: (context, constraints) {
      int crossAxisCount = (constraints.maxWidth / 200).floor();
      if (crossAxisCount < 1) crossAxisCount = 1;
      
      return GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: crossAxisCount,
          childAspectRatio: 1.0,
        ),
        itemCount: 20,
        itemBuilder: (context, index) => Card(
          child: Center(child: Text('Item $index')),
        ),
      );
    },
  );
}
```

**Solution 3: Use SliverGridDelegateWithMaxCrossAxisExtent**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return GridView.builder(
    gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
      maxCrossAxisExtent: 250,
      childAspectRatio: 2 / 3,
      crossAxisSpacing: 10,
      mainAxisSpacing: 10,
    ),
    itemCount: 20,
    itemBuilder: (context, index) => Card(
      child: Center(child: Text('${index + 1}')),
    ),
  );
}
```

**Solution 4: GridView.count and GridView.extent**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  // GridView.count — specify number of columns
  return GridView.count(
    crossAxisCount: 2,
    children: List.generate(10, (index) {
      return Card(
        child: Center(child: Text('Item $index')),
      );
    }),
  );
}

// GridView.extent — specify max width per item
Widget buildExtent(BuildContext context) {
  return GridView.extent(
    maxCrossAxisExtent: 200,
    childAspectRatio: 1.5,
    children: List.generate(12, (index) {
      return Card(child: Center(child: Text('Item $index')));
    }),
  );
}
```

**Solution 5: Wrap GridView in Expanded**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Scaffold(
    appBar: AppBar(title: Text('Grid')),
    body: Column(
      children: [
        Text('Filters'),
        Expanded(
          child: GridView.builder(
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 3,
            ),
            itemCount: 20,
            itemBuilder: (context, index) => Card(
              child: Center(child: Text('Item $index')),
            ),
          ),
        ),
      ],
    ),
  );
}
```

## Examples

`SliverGridDelegateWithFixedCrossAxisCount` calculates item size based on the number of columns. `SliverGridDelegateWithMaxCrossAxisExtent` calculates columns based on the maximum item width.

## Related Errors

- [Flutter List View Error](/languages/dart/flutter-list-view-error/)
- [Flutter Layout Builder Error](/languages/dart/flutter-layout-builder-error/)
- [Flutter Custom Scroll Error](/languages/dart/flutter-custom-scroll-error/)
