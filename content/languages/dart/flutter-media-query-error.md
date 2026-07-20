---
title: "[Solution] Flutter MediaQuery Error — orientation, size, padding"
description: "Fix Flutter MediaQuery errors from incorrect orientation handling, size access, padding issues, and safe area."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 154
---

MediaQuery errors occur when accessing device metrics that are not available, orientation handling is incorrect, or padding is not accounted for.

## Common Causes

1. Using `MediaQuery.of(context).size` before the first frame.
2. Not handling orientation changes in layout.
3. Ignoring `viewPadding` for safe area insets.
4. `MediaQuery.of(context)` returning stale data.
5. Accessing MediaQuery in a dialog or overlay with unexpected values.

## How to Fix It

**Solution 1: Access MediaQuery safely**

```dart
import 'package:flutter/material.dart';

class ResponsiveLayout extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;
    Orientation orientation = MediaQuery.of(context).orientation;
    
    return Container(
      width: screenSize.width,
      height: screenSize.height,
      child: orientation == Orientation.portrait
          ? _buildPortrait(context)
          : _buildLandscape(context),
    );
  }
  
  Widget _buildPortrait(BuildContext context) {
    return Column(children: [Text('Portrait')]);
  }
  
  Widget _buildLandscape(BuildContext context) {
    return Row(children: [Text('Landscape')]);
  }
}
```

**Solution 2: Handle safe area padding**

```dart
import 'package:flutter/material.dart';

class SafeAreaLayout extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    EdgeInsets padding = MediaQuery.of(context).padding;
    
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.only(
          top: padding.top,
          bottom: padding.bottom,
        ),
        child: Center(child: Text('Safe content')),
      ),
    );
  }
}
```

**Solution 3: Use MediaQuery for responsive design**

```dart
import 'package:flutter/material.dart';

class ResponsiveText extends StatelessWidget {
  final String text;
  
  const ResponsiveText({super.key, required this.text});
  
  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    
    double fontSize;
    if (screenWidth < 600) {
      fontSize = 14;
    } else if (screenWidth < 1200) {
      fontSize = 18;
    } else {
      fontSize = 22;
    }
    
    return Text(
      text,
      style: TextStyle(fontSize: fontSize),
    );
  }
}
```

**Solution 4: Listen for MediaQuery changes**

```dart
import 'package:flutter/material.dart';

class MediaQueryListener extends StatefulWidget {
  @override
  State<MediaQueryListener> createState() => _MediaQueryListenerState();
}

class _MediaQueryListenerState extends State<MediaQueryListener> {
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        return Text(
          'Width: ${constraints.maxWidth}, '
          'Height: ${constraints.maxHeight}',
        );
      },
    );
  }
}
```

**Solution 5: Handle keyboard insets**

```dart
import 'package:flutter/material.dart';

class KeyboardAwareWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    double viewInsets = MediaQuery.of(context).viewInsets.bottom;
    bool isKeyboardVisible = viewInsets > 0;
    
    return Scaffold(
      body: Column(
        children: [
          Expanded(
            child: ListView(
              children: [Text('Content')],
            ),
          ),
          if (isKeyboardVisible)
            Padding(
              padding: EdgeInsets.only(bottom: viewInsets),
              child: TextField(),
            ),
        ],
      ),
    );
  }
}
```

## Examples

`MediaQuery.of(context)` returns the nearest `MediaQuery` ancestor. Wrap your `MaterialApp` with a `MediaQuery` to override defaults. Use `MediaQuery.textScaleFactorOf(context)` for accessibility text scaling.

## Related Errors

- [Flutter Layout Builder Error](/languages/dart/flutter-layout-builder-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
- [Flutter Scroll Controller Error](/languages/dart/flutter-scroll-controller-error/)
