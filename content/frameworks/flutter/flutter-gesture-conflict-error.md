---
title: "[Solution] Flutter Gesture Conflict Error"
description: "Fix Flutter gesture conflict errors when multiple gesture detectors compete for the same touch events."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A gesture conflict error in Flutter occurs when multiple `GestureDetector` or `InkWell` widgets compete for the same touch event, causing one or both to fail to respond. This happens because Flutter's gesture arena resolves conflicts by choosing one recognizer.

## Common Causes

- Nested `GestureDetector` widgets with overlapping tap targets
- `InkWell` inside a `ListTile` that is also inside a `GestureDetector`
- Horizontal `ListView` inside a vertical `PageView`
- `Dismissible` inside a `ListView` with its own scroll physics
- Multiple gesture recognizers attached to the same area

## How to Fix

1. Use `HitTestBehavior` to control event propagation:

```dart
GestureDetector(
  behavior: HitTestBehavior.translucent,
  onTap: () => print('Background tapped'),
  child: Column(
    children: [
      GestureDetector(
        onTap: () => print('Button tapped'),
        child: ElevatedButton(onPressed: () {}, child: Text('Tap me')),
      ),
    ],
  ),
);
```

2. Use `Listener` for low-level pointer events:

```dart
Listener(
  onPointerDown: (event) => print('Pointer down at ${event.position}'),
  child: Container(
    width: 200,
    height: 200,
    color: Colors.blue,
  ),
);
```

3. Resolve conflicts with `GestureRecognizerFactoryWithHandlers`:

```dart
GestureDetector(
  behavior: HitTestBehavior.opaque,
  onHorizontalDragUpdate: (details) {
    // Handle horizontal drag
  },
  child: ListView.builder(
    scrollDirection: Axis.vertical,
    itemBuilder: (context, index) => ListTile(title: Text('Item $index')),
  ),
);
```

## Examples

```dart
// Bug: horizontal scroll inside vertical scroll -- conflict
PageView(
  children: [
    ListView.builder(
      scrollDirection: Axis.horizontal,
      itemBuilder: (context, index) => Container(width: 100, child: Text('H$index')),
    ),
  ],
);

// Fixed: use Scrollable.ensureVisible or NestedScrollView
NestedScrollView(
  headerSliverBuilder: (context, innerBoxIsScrolled) => [],
  body: ListView.builder(
    itemBuilder: (context, index) => Text('Item $index'),
  ),
);
```

```text
Gesture arena winner not determined for horizontal drag
```
