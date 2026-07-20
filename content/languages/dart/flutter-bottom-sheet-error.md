---
title: "[Solution] Flutter Bottom Sheet Error — showBottomSheet, DraggableScrollableSheet, snap"
description: "Fix Flutter bottom sheet errors from showBottomSheet, DraggableScrollableSheet, snap behavior, and controller issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 163
---

Bottom sheet errors occur when sheets are not properly dismissed, `DraggableScrollableSheet` snap behavior is misconfigured, or controllers are not disposed.

## Common Causes

1. `showBottomSheet` called without a `Scaffold` ancestor.
2. `DraggableScrollableController` not disposed.
3. `snap` sizes not being monotonically increasing.
4. Bottom sheet not dismissed when navigating away.
5. `showModalBottomSheet` barrier not handling back button.

## How to Fix It

**Solution 1: Show a modal bottom sheet**

```dart
import 'package:flutter/material.dart';

void showModal(BuildContext context) {
  showModalBottomSheet(
    context: context,
    builder: (BuildContext context) {
      return Container(
        height: 200,
        child: Column(
          children: [
            ListTile(
              leading: Icon(Icons.photo),
              title: Text('Photo'),
              onTap: () => Navigator.pop(context),
            ),
            ListTile(
              leading: Icon(Icons.file_copy),
              title: Text('File'),
              onTap: () => Navigator.pop(context),
            ),
          ],
        ),
      );
    },
  );
}
```

**Solution 2: Use DraggableScrollableSheet**

```dart
import 'package:flutter/material.dart';

void showDraggableSheet(BuildContext context) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    builder: (BuildContext context) {
      return DraggableScrollableSheet(
        initialChildSize: 0.4,
        minChildSize: 0.2,
        maxChildSize: 0.8,
        builder: (context, scrollController) {
          return Container(
            color: Colors.white,
            child: ListView.builder(
              controller: scrollController,
              itemCount: 20,
              itemBuilder: (context, index) => ListTile(
                title: Text('Item $index'),
              ),
            ),
          );
        },
      );
    },
  );
}
```

**Solution 3: Control DraggableScrollableController**

```dart
import 'package:flutter/material.dart';

class ControlledSheet extends StatefulWidget {
  @override
  State<ControlledSheet> createState() => _ControlledSheetState();
}

class _ControlledSheetState extends State<ControlledSheet> {
  final DraggableScrollableController _controller =
      DraggableScrollableController();
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  void _snapToTop() {
    _controller.animateTo(
      0.8,
      duration: Duration(milliseconds: 300),
      curve: Curves.easeOut,
    );
  }
  
  @override
  Widget build(BuildContext context) {
    return DraggableScrollableSheet(
      controller: _controller,
      initialChildSize: 0.4,
      minChildSize: 0.2,
      maxChildSize: 0.8,
      builder: (context, scrollController) {
        return Container(
          color: Colors.white,
          child: ListView(
            controller: scrollController,
            children: [
              Center(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: Text('Drag me'),
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
```

**Solution 4: Non-modal persistent bottom sheet**

```dart
import 'package:flutter/material.dart';

class PersistentSheet extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Persistent Sheet')),
      body: Center(child: Text('Content')),
      bottomSheet: Container(
        height: 60,
        color: Colors.blue,
        child: Center(
          child: Text(
            'Persistent Bottom Sheet',
            style: TextStyle(color: Colors.white),
          ),
        ),
      ),
    );
  }
}
```

**Solution 5: Handle snap semantics**

```dart
import 'package:flutter/material.dart';

void showSnappingSheet(BuildContext context) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    builder: (BuildContext context) {
      return DraggableScrollableSheet(
        initialChildSize: 0.5,
        minChildSize: 0.25,
        maxChildSize: 0.75,
        snap: true,
        snapSizes: [0.25, 0.5, 0.75],
        builder: (context, scrollController) {
          return Container(
            decoration: BoxDecoration(
              borderRadius: BorderRadius.vertical(top: Radius.circular(16)),
              color: Colors.white,
            ),
            child: ListView(
              controller: scrollController,
              children: List.generate(
                30,
                (i) => ListTile(title: Text('Item $i')),
              ),
            ),
          );
        },
      );
    },
  );
}
```

## Examples

`DraggableScrollableSheet` snaps to the nearest `snapSize` when the user releases. `snapSizes` must be in ascending order and within `[minChildSize, maxChildSize]`.

## Related Errors

- [Flutter Dialog Error](/languages/dart/flutter-dialog-error/)
- [Flutter Scroll Controller Error](/languages/dart/flutter-scroll-controller-error/)
- [Flutter Snackbar Error](/languages/dart/flutter-snackbar-error/)
