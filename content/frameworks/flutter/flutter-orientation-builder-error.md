---
title: "[Solution] Flutter OrientationBuilder Error"
description: "Fix Flutter OrientationBuilder errors when layout does not rebuild when device orientation changes."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An OrientationBuilder error in Flutter occurs when the widget does not rebuild when the device orientation changes from portrait to landscape, because it is not placed correctly in the widget tree or its parent prevents rebuilds.

## Common Causes

- `OrientationBuilder` placed above `MaterialApp` in the widget tree
- `OrientationBuilder` inside a `SizedBox` with fixed height
- Parent widget does not allow layout changes
- `MediaQuery.of(context).orientation` used instead of `OrientationBuilder`
- State is cached and not rebuilt on orientation change

## How to Fix

1. Place OrientationBuilder inside the Scaffold:

```dart
Scaffold(
  body: OrientationBuilder(
    builder: (context, orientation) {
      return orientation == Orientation.portrait
        ? _buildPortraitLayout()
        : _buildLandscapeLayout();
    },
  ),
);
```

2. Use OrientationBuilder with GridView:

```dart
OrientationBuilder(
  builder: (context, orientation) {
    return GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: orientation == Orientation.portrait ? 2 : 4,
        mainAxisSpacing: 8,
        crossAxisSpacing: 8,
      ),
      itemBuilder: (context, index) => Card(child: Center(child: Text('Item $index'))),
    );
  },
);
```

3. Combine with MediaQuery for screen size:

```dart
OrientationBuilder(
  builder: (context, orientation) {
    final screenWidth = MediaQuery.of(context).size.width;
    final columns = orientation == Orientation.portrait
      ? (screenWidth > 600 ? 3 : 2)
      : 4;

    return GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: columns),
      itemCount: items.length,
      itemBuilder: (context, index) => ItemCard(item: items[index]),
    );
  },
);
```

## Examples

```dart
// Bug: OrientationBuilder outside MaterialApp
OrientationBuilder(
  builder: (context, orientation) {
    return MaterialApp(home: HomeScreen()); // Does not rebuild
  },
);

// Fixed: place inside Scaffold body
MaterialApp(
  home: Scaffold(
    body: OrientationBuilder(
      builder: (context, orientation) {
        return orientation == Orientation.portrait
          ? PortraitLayout()
          : LandscapeLayout();
      },
    ),
  ),
);
```

```text
OrientationBuilder widgets must be placed below WidgetsApp or MaterialApp
```
