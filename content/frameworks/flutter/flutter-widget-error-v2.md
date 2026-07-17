---
title: "RenderFlex overflowed"
description: "Flutter throws RenderFlex overflowed error when a flex widget's children exceed available space"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The RenderFlex overflowed error occurs when a Row, Column, or Flex widget has children that collectively exceed the available space along the main axis. Flutter renders a yellow/black striped warning stripe indicating the overflow amount.

## Common Causes

- Long text content without wrapping in a Row
- Too many children in a Column without scrolling
- Fixed-size widgets that do not adapt to screen width
- Using Row with Text children that do not have Expanded or Flexible
- Not accounting for different screen sizes

## How to Fix

1. Wrap overflowing Row children with Expanded or Flexible:

```dart
Row(
  children: [
    Expanded(
      child: Text('This is a very long text that will wrap instead of overflow'),
    ),
    Icon(Icons.arrow_forward),
  ],
)
```

2. Use SingleChildScrollView for vertical overflow:

```dart
SingleChildScrollView(
  child: Column(
    children: [
      // unlimited children
      for (var item in items)
        ListTile(title: Text(item)),
    ],
  ),
)
```

3. Allow text to wrap instead of staying on one line:

```dart
Row(
  crossAxisAlignment: CrossAxisAlignment.start,
  children: [
    Flexible(
      child: Text(
        'Long text that will wrap to next line',
        overflow: TextOverflow.visible,
      ),
    ),
  ],
)
```

4. Use Wrap widget for dynamic content:

```dart
Wrap(
  spacing: 8.0,
  children: tags.map((tag) => Chip(label: Text(tag))).toList(),
)
```

5. Constrain text with maxLines and overflow:

```dart
Text(
  'Very long content here',
  maxLines: 2,
  overflow: TextOverflow.ellipsis,
)
```

## Examples

```dart
// This will overflow
Row(
  children: [
    Text('This is a very long label that exceeds the screen width'),
    Icon(Icons.check),
  ],
)

// Fix: use Expanded
Row(
  children: [
    Expanded(
      child: Text('This is a very long label that exceeds the screen width'),
    ),
    Icon(Icons.check),
  ],
)
```

## Related Errors

- [State error]({{< relref "/frameworks/flutter/flutter-state-error-v2" >}})
- [Widget error]({{< relref "/frameworks/flutter/flutter-widget-error-v2" >}})
