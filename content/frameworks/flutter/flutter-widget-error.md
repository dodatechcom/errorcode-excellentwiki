---
title: "RenderFlex overflowed"
description: "Flutter throws a RenderFlex overflow error when a flex widget has more content than it can display"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a `Row`, `Column`, or `Flex` widget contains children that exceed the available space. Flutter renders yellow/black warning stripes on the overflow side.

## Common Causes

- `Row` or `Column` contains text or widgets wider than the screen
- Not using `Expanded` or `Flexible` to constrain child sizes
- Fixed-width widgets summing to more than available space
- Dynamic content (text from API) exceeding layout bounds

## How to Fix

1. Use `Expanded` or `Flexible` for resizable children:

```dart
Row(
  children: [
    Expanded(
      child: Text('This text will wrap to fit available space'),
    ),
    Icon(Icons.arrow_forward),
  ],
)
```

2. Allow text to wrap using `Flexible`:

```dart
Row(
  children: [
    Flexible(
      child: Text(
        'A very long text that might overflow the row',
        overflow: TextOverflow.ellipsis,
      ),
    ),
  ],
)
```

3. Use `Wrap` for dynamic content:

```dart
Wrap(
  spacing: 8.0,
  children: tags.map((tag) => Chip(label: Text(tag))).toList(),
)
```

4. Set overflow handling:

```dart
Text(
  'Long text here',
  overflow: TextOverflow.ellipsis, // or TextOverflow.fade
  maxLines: 2,
)
```

## Examples

```dart
Row(
  children: [
    Text('A very long text that definitely overflows the row width'),
    Icon(Icons.star),
  ],
)
// RenderFlex overflowed by 123 pixels on the right
```

## Related Errors

- [Widget error]({{< relref "/frameworks/flutter/widget-error" >}})
- [Platform error]({{< relref "/frameworks/flutter/platform-error" >}})
