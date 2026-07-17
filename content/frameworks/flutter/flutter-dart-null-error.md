---
title: "Null check operator used on null value"
description: "Dart throws null check operator error when the ! operator is used on a variable that is currently null"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The "null check operator used on null value" error occurs in Dart when the `!` (bang) operator is applied to a nullable variable that holds `null` at runtime. This is a common error in Flutter apps that have not fully adopted null safety or use `!` without null checks.

## Common Causes

- Using `!` on a nullable variable without checking for null first
- Widget `context` accessed after the widget is disposed
- Route arguments accessed without null check
- State variables not initialized before use
- Future results accessed with `!` without null check

## How to Fix

1. Replace `!` with null-safe alternatives:

```dart
// Bad: null check operator
final name = user!.name;

// Good: null check or default
final name = user?.name ?? 'Guest';
```

2. Use null checks before accessing:

```dart
if (user != null) {
  final name = user!.name;
}
```

3. Use pattern matching (Dart 3+):

```dart
final name = switch (user) {
  User() => user.name,
  _ => 'Guest',
};
```

4. Safely access widget context:

```dart
@override
Widget build(BuildContext context) {
  final args = ModalRoute.of(context)?.settings.arguments as Map?;
  final id = args?['id'] as String?;
  return Text(id ?? 'No ID');
}
```

5. Initialize state variables properly:

```dart
class _MyWidgetState extends State<MyWidget> {
  String name = 'default'; // initialized with default

  @override
  void initState() {
    super.initState();
    name = widget.initialName ?? 'default';
  }
}
```

## Examples

```dart
// Error: null check operator used on null value
class ProfileScreen extends StatelessWidget {
  final String? userId;

  ProfileScreen({this.userId});

  @override
  Widget build(BuildContext context) {
    return Text(userId!.length.toString()); // userId could be null
  }
}

// Fix: handle null case
class ProfileScreen extends StatelessWidget {
  final String? userId;

  ProfileScreen({this.userId});

  @override
  Widget build(BuildContext context) {
    return Text(userId?.length.toString() ?? 'Unknown');
  }
}
```

## Related Errors

- [Type error]({{< relref "/frameworks/flutter/flutter-dart-type-error" >}})
- [State error]({{< relref "/frameworks/flutter/flutter-state-error-v2" >}})
