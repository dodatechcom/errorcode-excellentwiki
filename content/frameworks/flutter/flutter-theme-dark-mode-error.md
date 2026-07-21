---
title: "[Solution] Flutter Theme Dark Mode Error"
description: "Fix Flutter dark mode theme errors when the app does not switch themes or uses incorrect colors in dark mode."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A dark mode theme error in Flutter occurs when the application does not properly switch between light and dark themes, causing hard-coded colors to appear incorrectly when the system theme changes.

## Common Causes

- Colors hard-coded instead of using `Theme.of(context)` colors
- `themeDark` not defined in `MaterialApp`
- `themeMode` property not set on `MaterialApp`
- `ColorScheme.fromSeed` does not include dark mode variant
- Custom widgets ignore the current theme brightness

## How to Fix

1. Define both light and dark themes:

```dart
MaterialApp(
  theme: ThemeData(
    colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
    brightness: Brightness.light,
  ),
  darkTheme: ThemeData(
    colorScheme: ColorScheme.fromSeed(
      seedColor: Colors.blue,
      brightness: Brightness.dark,
    ),
    brightness: Brightness.dark,
  ),
  themeMode: ThemeMode.system, // Follows system setting
);
```

2. Use theme colors instead of hard-coded values:

```dart
// Wrong: hard-coded colors
Container(color: Colors.white)
Text('Hello', style: TextStyle(color: Colors.black))

// Fixed: use theme
Container(color: Theme.of(context).colorScheme.surface)
Text('Hello', style: TextStyle(color: Theme.of(context).colorScheme.onSurface))
```

3. Create theme-aware custom widgets:

```dart
class MyCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Card(
      color: theme.colorScheme.surface,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Text(
          'Card content',
          style: theme.textTheme.bodyLarge?.copyWith(
            color: theme.colorScheme.onSurface,
          ),
        ),
      ),
    );
  }
}
```

## Examples

```dart
// Bug: hard-coded white background -- invisible in dark mode
Scaffold(
  backgroundColor: Colors.white, // Always white
  body: Text('Hello', style: TextStyle(color: Colors.black)),
);

// Fixed: theme-aware colors
Scaffold(
  backgroundColor: Theme.of(context).scaffoldBackgroundColor,
  body: Text('Hello', style: Theme.of(context).textTheme.bodyLarge),
);
```

```text
Looking up a deactivated widget's ancestor is unsafe.
```
