---
title: "[Solution] Flutter Card Elevation Error"
description: "Fix Flutter Card elevation errors when cards appear flat or have incorrect shadow rendering."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Card elevation error in Flutter occurs when `Card` widgets render with incorrect or missing shadows, making them appear flat or visually broken, especially in dark mode or with custom themes.

## Common Causes

- `elevation` set to 0 making the card appear flat
- `Card` inside a `Material` widget that overrides the elevation
- Dark theme not configured with proper surface colors
- `clipBehavior` set to `Clip.none` causing shadow overflow
- `color` on Card not matching the theme surface color

## How to Fix

1. Set appropriate elevation values:

```dart
Card(
  elevation: 2, // Default elevation
  child: Padding(
    padding: const EdgeInsets.all(16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('Card Title', style: Theme.of(context).textTheme.titleMedium),
        const SizedBox(height: 8),
        Text('Card content goes here'),
      ],
    ),
  ),
);
```

2. Customize elevation for different states:

```dart
Card(
  elevation: _isHovered ? 8 : 2,
  shadowColor: Colors.black26,
  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
  child: InkWell(
    onTap: () {},
    onHover: (hovering) => setState(() => _isHovered = hovering),
    child: Padding(
      padding: const EdgeInsets.all(16),
      child: Text('Interactive card'),
    ),
  ),
);
```

3. Handle elevation in dark mode:

```dart
Card(
  elevation: Theme.of(context).brightness == Brightness.dark ? 4 : 2,
  color: Theme.of(context).colorScheme.surface,
  child: Padding(
    padding: const EdgeInsets.all(16),
    child: content,
  ),
);
```

## Examples

```dart
// Bug: Card inside Material widget with zero elevation
Material(
  elevation: 0,
  child: Card(
    elevation: 4, // Overridden by parent
    child: Text('Flat card'),
  ),
);

// Fixed: remove or set parent elevation
Card(
  elevation: 4,
  child: Text('Elevated card'),
);
```

```text
Cards require a Material ancestor widget
```
