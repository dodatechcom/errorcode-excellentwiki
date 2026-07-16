---
title: "RenderFlex Overflowed"
description: "Flutter displays a yellow/black striped overflow warning when a Flex widget exceeds its bounds"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["warning"]
tags: ["layout", "overflow", "flex", "rendering"]
weight: 5
---

## What This Error Means

The RenderFlex overflow error occurs when a Row, Column, or Flex widget contains children that exceed the available space along the main axis. Flutter renders a yellow and black striped banner to indicate the overflow.

## Common Causes

- Text content that is too long for a fixed-width container
- Using Row/Column without proper sizing constraints
- Missing Expanded or Flexible widgets around children
- Not wrapping scrollable content in SingleChildScrollView

## How to Fix

**Use Expanded or Flexible for dynamic content:**

```dart
Row(
  children: [
    Expanded(
      child: Text('This text will wrap instead of overflow'),
    ),
  ],
)
```

**Wrap in a scrollable widget:**

```dart
SingleChildScrollView(
  child: Column(
    children: [
      Text('Long content here'),
      Text('More content'),
    ],
  ),
)
```

## Examples

```dart
// This triggers the overflow error:
Row(
  children: [
    Text('Very long text that will not fit in the available space'),
  ],
)

// Fixed version:
Row(
  children: [
    Expanded(
      child: Text('Very long text that will not fit in the available space'),
    ),
  ],
)
```

## Related Errors

- [Null Check Error]({{< relref "/frameworks/flutter/null-check-error" >}})
