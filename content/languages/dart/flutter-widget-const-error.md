---
title: "[Solution] Flutter const Widget Error — const Constructor, Ambient Creation"
description: "Fix Flutter const widget errors from missing const constructors, const context issues, and performance implications."
languages: ["dart"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 150
---

const widget errors occur when widgets are marked as `const` but their constructors are not const-compatible, or when const is used incorrectly in the widget tree.

## Common Causes

1. Widget constructor not declared as `const`.
2. Using `const` with a widget that has non-const parameters.
3. Forgetting `const` in widget trees, causing unnecessary rebuilds.
4. `const` widget containing a `Key` that is not const.
5. Mixing `const` and non-const constructors in the same expression.

## How to Fix It

**Solution 1: Make widget constructors const-compatible**

```dart
import 'package:flutter/material.dart';

class GreetingCard extends StatelessWidget {
  final String name;
  
  // Const constructor
  const GreetingCard({super.key, required this.name});
  
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Text('Hello, $name!'),
      ),
    );
  }
}

// Usage
Widget build(BuildContext context) {
  return const GreetingCard(name: 'Alice'); // Works
}
```

**Solution 2: Use const in widget trees**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Column(
    children: const [
      Text('Line 1'),
      Text('Line 2'),
      Text('Line 3'),
    ],
  );
}
```

**Solution 3: Use const with Keys**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return const GreetingCard(
    key: ValueKey('greeting'),
    name: 'Bob',
  );
}
```

**Solution 4: Remove const when parameters are dynamic**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  String dynamicName = getUserName();
  
  // Cannot use const here — dynamicName is not const
  return GreetingCard(name: dynamicName);
  
  // But children of Column can be const if they don't depend on dynamic data
  return Column(
    children: [
      GreetingCard(name: dynamicName), // Not const
      const Text('Static label'),       // Const
    ],
  );
}

String getUserName() => 'Charlie';
```

**Solution 5: Use `const` constructors in collections**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return ListView(
    children: const [
      ListTile(title: Text('Item 1')),
      ListTile(title: Text('Item 2')),
      ListTile(title: Text('Item 3')),
    ],
  );
}
```

## Examples

Using `const` in the widget tree tells Flutter that the widget will never change, so it can skip rebuilds. This is a significant performance optimization for static content.

## Related Errors

- [Flutter Key Error](/languages/dart/flutter-key-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
- [Flutter Widget Lifecycle Error](/languages/dart/dart-widget-lifecycle-error/)
