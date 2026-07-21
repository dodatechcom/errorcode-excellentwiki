---
title: "[Solution] Flutter ClipRRect Border Radius Error"
description: "Fix Flutter ClipRRect errors when rounded corners do not display or cause rendering issues with images."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A ClipRRect border radius error in Flutter occurs when `ClipRRect` does not properly clip its child because the border radius is too large, the child has an unconstrained size, or `ClipRRect` is used in a context where hardware acceleration fails.

## Common Causes

- Border radius larger than half the widget's width or height
- `ClipRRect` child is a `ListView` or `GridView` that needs to be clipped differently
- `borderRadius` uses `BorderRadius.circular` with a very large value
- `ClipRRect` inside a `RepaintBoundary` causing layer issues
- Image widget not clipped because it loads asynchronously

## How to Fix

1. Calculate safe border radius:

```dart
ClipRRect(
  borderRadius: BorderRadius.circular(12),
  child: Container(
    width: 200,
    height: 200,
    color: Colors.blue,
    child: Center(child: Text('Clipped')),
  ),
);
```

2. Clip network images after they load:

```dart
ClipRRect(
  borderRadius: BorderRadius.circular(16),
  child: Image.network(
    imageUrl,
    width: 200,
    height: 200,
    fit: BoxFit.cover,
    gaplessPlayback: true, // Prevents flash during reload
  ),
);
```

3. Use ClipRRect with Stack for complex layouts:

```dart
ClipRRect(
  borderRadius: BorderRadius.circular(12),
  child: Stack(
    children: [
      Image.network(url, fit: BoxFit.cover, width: 300, height: 200),
      Positioned(
        bottom: 0,
        left: 0,
        right: 0,
        child: Container(
          color: Colors.black54,
          padding: EdgeInsets.all(8),
          child: Text('Title', style: TextStyle(color: Colors.white)),
        ),
      ),
    ],
  ),
);
```

## Examples

```dart
// Bug: border radius larger than widget
ClipRRect(
  borderRadius: BorderRadius.circular(100), // 100 > half of 50px width
  child: Container(width: 50, height: 50, color: Colors.red),
);

// Fixed: radius <= half the smaller dimension
ClipRRect(
  borderRadius: BorderRadius.circular(25), // 25 == half of 50
  child: Container(width: 50, height: 50, color: Colors.red),
);
```

```text
A borderRadius can only be given for uniform boxes
```
