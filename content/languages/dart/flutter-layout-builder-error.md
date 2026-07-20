---
title: "[Solution] Flutter LayoutBuilder Error — BoxConstraints infinite, maxWidth"
description: "Fix Flutter LayoutBuilder errors from infinite constraints, maxWidth issues, and incorrect layout decisions."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 155
---

LayoutBuilder errors occur when constraints are infinite (unbounded), leading to layout overflow or rendering failures.

## Common Causes

1. Using `LayoutBuilder` inside an unbounded parent (e.g., `ListView` without `shrinkWrap`).
2. Returning a widget with unbounded height from `LayoutBuilder`.
3. `maxWidth` or `maxHeight` being `double.infinity`.
4. Not handling different constraint ranges in responsive layouts.
5. Using `SizedBox.expand` inside an unbounded parent.

## How to Fix It

**Solution 1: Handle infinite constraints**

```dart
import 'package:flutter/material.dart';

class ResponsiveWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth == double.infinity) {
          return Text('Unbounded width');
        }
        
        if (constraints.maxWidth > 600) {
          return _buildWideLayout();
        } else {
          return _buildNarrowLayout();
        }
      },
    );
  }
  
  Widget _buildWideLayout() => Row(children: [Text('Wide')]);
  Widget _buildNarrowLayout() => Column(children: [Text('Narrow')]);
}
```

**Solution 2: Use LayoutBuilder in bounded containers**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Scaffold(
    body: Container(
      width: 300,
      height: 300,
      child: LayoutBuilder(
        builder: (context, constraints) {
          return Text(
            'Width: ${constraints.maxWidth}\n'
            'Height: ${constraints.maxHeight}',
          );
        },
      ),
    ),
  );
}
```

**Solution 3: Avoid infinite height in scrollable parents**

```dart
import 'package:flutter/material.dart';

// Wrong: LayoutBuilder inside ListView has infinite height
Widget wrong() {
  return ListView(
    children: [
      LayoutBuilder(
        builder: (context, constraints) {
          return Text('Height: ${constraints.maxHeight}'); // infinity!
        },
      ),
    ],
  );
}

// Correct: wrap in SizedBox with bounded height
Widget correct() {
  return ListView(
    children: [
      SizedBox(
        height: 200,
        child: LayoutBuilder(
          builder: (context, constraints) {
            return Text('Height: ${constraints.maxHeight}');
          },
        ),
      ),
    ],
  );
}
```

**Solution 4: Create responsive grid with LayoutBuilder**

```dart
import 'package:flutter/material.dart';

class ResponsiveGrid extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        int crossAxisCount;
        if (constraints.maxWidth > 1200) {
          crossAxisCount = 4;
        } else if (constraints.maxWidth > 800) {
          crossAxisCount = 3;
        } else if (constraints.maxWidth > 600) {
          crossAxisCount = 2;
        } else {
          crossAxisCount = 1;
        }
        
        return GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: crossAxisCount,
          ),
          itemCount: 20,
          itemBuilder: (context, index) => Card(
            child: Center(child: Text('Item $index')),
          ),
        );
      },
    );
  }
}
```

**Solution 5: Use ConstrainedBox within LayoutBuilder**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return LayoutBuilder(
    builder: (context, constraints) {
      double targetWidth = constraints.maxWidth * 0.8;
      
      return Center(
        child: ConstrainedBox(
          constraints: BoxConstraints(maxWidth: targetWidth),
          child: Card(
            child: Padding(
              padding: EdgeInsets.all(16),
              child: Text('Centered content'),
            ),
          ),
        ),
      );
    },
  );
}
```

## Examples

`LayoutBuilder` provides `BoxConstraints` that describe the parent's constraints. If the parent has unbounded constraints, `maxWidth` or `maxHeight` will be `double.infinity`.

## Related Errors

- [Flutter MediaQuery Error](/languages/dart/flutter-media-query-error/)
- [Flutter Custom Paint Error](/languages/dart/flutter-custom-paint-error/)
- [Flutter Grid View Error](/languages/dart/flutter-grid-view-error/)
