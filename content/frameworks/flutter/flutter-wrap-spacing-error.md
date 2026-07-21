---
title: "[Solution] Flutter Wrap Spacing Error"
description: "Fix Flutter Wrap spacing errors when wrapped children overlap or have incorrect gaps between items."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Wrap spacing error in Flutter occurs when children in a `Wrap` widget overlap, have inconsistent gaps, or overflow the available width because `spacing` and `runSpacing` are not configured correctly.

## Common Causes

- `spacing` set to 0 causing children to touch
- Children have different sizes causing alignment issues
- `runSpacing` not set causing vertical overlap
- `Wrap` inside a constrained width container
- `alignment` property not set for uneven rows

## How to Fix

1. Configure spacing and alignment:

```dart
Wrap(
  spacing: 8, // Horizontal spacing between items
  runSpacing: 8, // Vertical spacing between rows
  alignment: WrapAlignment.start,
  children: items.map((item) => Chip(
    label: Text(item),
    deleteIcon: const Icon(Icons.close, size: 16),
    onDeleted: () => removeItem(item),
  )).toList(),
);
```

2. Control alignment for each run:

```dart
Wrap(
  spacing: 8,
  runSpacing: 12,
  alignment: WrapAlignment.center,
  runAlignment: WrapAlignment.center,
  crossAxisAlignment: WrapCrossAlignment.center,
  children: [
    ElevatedButton(onPressed: () {}, child: Text('Save')),
    OutlinedButton(onPressed: () {}, child: Text('Cancel')),
    TextButton(onPressed: () {}, child: Text('Delete')),
  ],
);
```

3. Handle dynamic content in Wrap:

```dart
Wrap(
  spacing: 8,
  runSpacing: 8,
  children: tags.map((tag) => ActionChip(
    label: Text(tag),
    onPressed: () => selectTag(tag),
  )).toList(),
)
```

## Examples

```dart
// Bug: no spacing -- chips overlap
Wrap(
  children: [
    Chip(label: Text('Flutter')),
    Chip(label: Text('Dart')),
    Chip(label: Text('Firebase')),
  ],
);

// Fixed: add spacing
Wrap(
  spacing: 8,
  runSpacing: 8,
  children: [
    Chip(label: Text('Flutter')),
    Chip(label: Text('Dart')),
    Chip(label: Text('Firebase')),
  ],
);
```

```text
RenderFlex children have non-zero flex but incoming width constraints are unbounded
```
