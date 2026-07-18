---
title: "[Solution] Dart Missing Override Annotation - Method Does Not Override"
description: "Fix Dart missing @override annotation error. Learn why the analyzer warns about unannotated overrides and how to use the override annotation correctly."
languages: ["dart"]
error-types: ["compile-time-error"]
severities: ["warning"]
weight: 3
---

## What This Error Means

The Dart analyzer warns that a method in your subclass has the same name and signature as a method in the parent class, but it is not annotated with `@override`. This is not a runtime crash but a compile-time warning that can mask bugs if the parent method signature changes.

## Why It Happens

When you define a method in a subclass that matches a parent class method, Dart considers it an override. The `@override` annotation is optional but strongly recommended because it tells the analyzer your intent is to override, not shadow. Without it, if the parent method changes its signature, your method silently becomes a separate method instead of an override, and the parent behavior is restored without warning.

The warning also appears when you misspell the method name. If you write `onInit` instead of `onInitState`, the analyzer flags it as a missing override because the edit distance suggests you intended to override a parent method.

```dart
class MyWidget extends StatelessWidget {
  // Missing @override annotation
  Widget build(BuildContext context) {
    return Container();
  }
}
```

## How to Fix It

Add the `@override` annotation above any method that overrides a parent class method:

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const Text('Hello');
  }
}
```

Use IDE code generation to add missing overrides. In VS Code, hover over the warning and select "Add @override annotation". In IntelliJ, use the quick fix shortcut.

Verify that the method signature matches the parent exactly:

```dart
class Animal {
  void makeSound(String volume) {}
}

class Dog extends Animal {
  @override
  void makeSound(String volume) {
    print('Woof at $volume');
  }
}
```

If the method should not override the parent, rename it to avoid confusion:

```dart
class Dog extends Animal {
  @override
  void makeSound(String volume) {
    print('Woof at $volume');
  }

  // Intentionally different method, not an override
  void fetchItem(String item) {
    print('Fetching $item');
  }
}
```

Enable strict override checking in `analysis_options.yaml`:

```yaml
analyzer:
  errors:
    missing_override: warning
```

## Common Mistakes

- Ignoring the missing override warning, allowing silent behavior changes when parent signatures evolve
- Misspelling the method name which causes the override to not connect
- Overriding with a different signature which hides the parent method instead of overriding it
- Forgetting `@override` on `toString`, `hashCode`, or `==` which are frequently overridden
- Not adding `super.methodName()` calls when the parent implementation should still run

## Related Pages

- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart Cast Error](/languages/dart/dart-cast-error/)
- [Dart Async Error](/languages/dart/dart-async-error/)
- [Dart Widget Rebuild](/languages/dart/dart-widget-rebuild/)
- [Dart Plugin Error](/languages/dart/dart-plugin-error/)
